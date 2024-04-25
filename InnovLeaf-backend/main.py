from flask import Flask, request, jsonify
from flask_cors import CORS
import vertexai
from vertexai.language_models import TextGenerationModel
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 设置Google Cloud认证文件路径
credential_path = "E:\\build\innovleaf-001-6b65825ef30c.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# 初始化数据
user_data = {
    "userProfile": {
        "avatarUrl": "dan_xiao_fen.png",
        "nickname": "蛋小粉"
    },
    "basicInfoData": {
        "age": 10,
        "language": "功能性交流阶段",
        "sex": "女",
        "sensory": ["听觉"],
        "description": ""
    },
    "expectionData": {
        "readingGoal": "",
        "improvementAreas": "",
        "storyRequirements": ""
    },
    "interest": {
        "storyType": ["童话故事", "动物故事"],
        "character": "喜欢哈利波特",
        "theme": ["简单冒险"],
        "sound": "女",
        "color": "粉色",
        "other": ""
    },
    "readingData": {
        "readingMethod": "家长陪同阅读",
        "readingDuration": "能够长时间阅读",
        "repeatedReading": False,
        "otherHabits": ""
    }
}


@app.route('/user', methods=['POST'])
def set_user_data():
    print("updated information")
    # 接收JSON格式的数据
    data = request.get_json()
    # 更新数据到字典
    user_data.update({
        'userProfile': data.get('userProfile', user_data['userProfile']),
        'basicInfoData': data.get('basicInfoData', user_data['basicInfoData']),
        'expectionData': data.get('expectionData', user_data['expectionData']),
        'interest': data.get('interest', user_data['interest']),
        'readingData': data.get('readingData', user_data['readingData']),
    })
    print(user_data)
    return jsonify({"message": "Data updated successfully"}), 200


@app.route('/user', methods=['GET'])
def get_user_data():
    # 返回存储的用户数据
    return jsonify(user_data)

#将生成的故事返回给用户
@app.route('/story', methods=['GET'])
def request_story():
    #生成返回体，包括故事本身和请求code
    return jsonify({"story": format_story(generate_story()), "code": 200})

def generatePrompt():
    # 基于用户数据生成基本信息
    userInfo = "你来充当一位有关责任心的故事讲述者，为自闭症儿童生成情节丰富的故事，通过故事情节使得儿童增加情绪表达的能力，但是不要直接教育" \
               "## 任务" \
               "我用自然语言告诉你要生成的prompt的主题，你的任务是根据我的要求生成一个故事，故事的情节需要吸引人，而不是单纯的教育，直接开始讲述故事，不要添加除了故事主体之外的其它内容" \
               "## 生成内容要求" \
               "1. 将这个故事分为多个段落，每个段落大约100字，使用空行分段即可" \
               "2. 在prompt中，调整关键字强度的等效方法是使用 () 和 []。 [keyword] 将强调的强度增加 1.1 倍。 (keyword) 将强度降低 0.9 倍" \
               "3. 故事的阅读者是自闭症儿童，所以请确保故事内容适合他们的年龄和理解能力，但是在故事中不要出现自闭症相关的描述，故事主角也不能是自闭症儿童" \
               "4. [[[着重描述与情绪相关的表达，例如表达[开心]的情绪，不要只使用一个词语，而是描述主角的语气、动作、表情等]]]" \
               "5. 必须严格参考阅读者相关的信息以及故事背景信息，生成的故事要贴合这些内容" \
               "6. 在开始的第一段，为这个故事生成一个标题。" \
               "7. [[[[[非常重要，必须遵照： 只返回故事标题本身和故事内容本身，不要包含任何其他的说明性文字]]]]],格式：" \
               "    《故事标题》" \
               "    xxxxxxxxxxxxx" \
               "    xxxxxxxxxxxxx" \
               "    ..." \
               "## 阅读者相关的信息" \
               "[年龄:" + str(user_data["basicInfoData"]["age"]) + "岁]" \
                "[语言能力:" + user_data["basicInfoData"]["language"] + "]，语言能力越弱，故事越简单" \
                "性别:" + user_data["basicInfoData"]["sex"] + "" \
                "[感官:" + "、".join(user_data["basicInfoData"]["sensory"]) + "]" + "着重描述这些感官的感受" \
                "阅读目标:" + user_data["expectionData"]["readingGoal"] + user_data["expectionData"]["improvementAreas"] + "" \
                "故事要求:" + user_data["expectionData"]["storyRequirements"] + "" \
                "[[阅读者感兴趣的故事类型:" + "、".join(user_data["interest"]["storyType"]) + "]]" \
                "阅读者感兴趣的角色:" + user_data["interest"]["character"] + "]]" \
                "[阅读者感兴趣的主题:" + "、".join(user_data["interest"]["theme"]) + "]" \
                "阅读者感兴趣的其他:" + user_data["interest"]["other"] + "" \
                "生成的故事尽量适应阅读方式:" + user_data["readingData"]["readingMethod"] + "" \
                "生成的故事尽量适应阅读时长:" + user_data["readingData"]["readingDuration"] + "" \
                "生成的故事尽量适应其他习惯:" + user_data["readingData"]["otherHabits"] + ""
    return userInfo


# 调用PaLM 2 for Text Generation生成故事
def generate_story() -> str:
    """Ideation example with a Large Language Model"""

    vertexai.init(project="innovleaf-001", location="us-central1")

    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,
        # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        generatePrompt(),
        **parameters,
    )

    return response.text

# 处理生成的故事
def format_story(story):
    # 生成的故事根据段落，生成一个列表
    story_list = story.split("\n")
    # 去除空行
    story_list = [line for line in story_list if line.strip()]
    print(story_list)
    return story_list

if __name__ == '__main__':

    app.run()
