<template>
  <div class="interest-setting">
    <div class="header">
      <h1>兴趣爱好</h1>
    </div>
    <el-form ref="interestForm" :model="interest" label-width="120px">
      <el-form-item label="故事类型" class="item">
        <el-checkbox-group v-model="interest.storyType">
          <el-checkbox value="童话故事">童话故事</el-checkbox>
          <el-checkbox value="动物故事">动物故事</el-checkbox>
          <el-checkbox value="神话和传说">神话和传说</el-checkbox>
          <el-checkbox value="冒险故事">冒险故事</el-checkbox>
          <el-checkbox value="现实生活故事">现实生活故事</el-checkbox>
          <el-checkbox value="科幻和幻想故事">科幻和幻想故事</el-checkbox>
          <el-checkbox value="教育故事">教育故事</el-checkbox>
          <el-checkbox value="历史故事">历史故事</el-checkbox>
        </el-checkbox-group>
      </el-form-item>

      <el-form-item label="人物或角色" class="item">
        <el-input
          v-model="interest.character"
          placeholder="喜欢的故事或者现实人物"
        ></el-input>
      </el-form-item>

      <el-form-item label="主题" class="item">
        <el-checkbox-group v-model="interest.theme">
          <el-checkbox value="daily-routines">日常生活</el-checkbox>
          <el-checkbox value="animal-friends">动物朋友</el-checkbox>
          <el-checkbox value="simple-adventures">简单冒险</el-checkbox>
          <el-checkbox value="problem-solving">解决问题</el-checkbox>
          <el-checkbox value="cause-and-effect">因果关系</el-checkbox>
          <el-checkbox value="emotional-exploration">情感探索</el-checkbox>
          <el-checkbox value="historical-events">历史事件</el-checkbox>
          <el-checkbox value="science-discoveries">科学发现</el-checkbox>
        </el-checkbox-group>
      </el-form-item>
      <el-form-item label="声音类型" class="item">
        <el-select v-model="interest.sound" placeholder="请选择声音模式">
          <el-option value="cmn-CN-Wavenet-B">男</el-option>
          <el-option value="cmn-CN-Wavenet-A">女</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="颜色或图案" class="item">
        <el-input
          placeholder="和我们分享小朋友最喜欢的颜色吧！"
          v-model="interest.color"
        ></el-input>
      </el-form-item>
      <el-form-item label="其他兴趣爱好" class="item">
        <el-input
          v-model="interest.other"
          class="item"
          placeholder="或许ta对数学、运动、棋艺等等感兴趣吗？"
        ></el-input>
      </el-form-item>
      <el-form-item class="btn">
        <el-button type="primary" @click="saveInterest">确认</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import { useStore } from "@/store/index.js";
import axios from "axios";

export default {
  data() {
    return {
      interest: {
        storyType: [],
        character: "",
        theme: [],
        sound: "",
        color: "",
        other: "",
      },
    };
  },

  // 在页面渲染之前获取pinia store中的数据
  created() {
    const store = useStore();
    this.interest = store.$state.interest;
  },
  methods: {
    saveInterest() {
      try {
        const store = useStore();
        store.$patch({
          interest: this.interest,
        });
      } catch (error) {
        ElMessage({
          message: "保存失败",
          type: "error",
        });
      }

      axios
        .post("http://127.0.0.1:5000/user", this.interest)
        .then((response) => {
          if (response.status === 200) {
            ElMessage({
              message: "保存成功",
              type: "success",
            });
          } else {
            ElMessage({
              message: "保存失败",
              type: "error",
            });
          }
        });
    },
  },
};
</script>


<style scoped>
.interest-setting {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Courier New", Courier, monospace;
  position: relative;
}
.header {
  display: flex;
  align-items: center;
  font: bold 24px "Courier New", Courier, monospace;
}

.interest-setting {
  margin: 0 auto;
}
.item {
  margin-bottom: 10px;
  width: 100%;
}

.btn {
  position: absolute;
  bottom: -10%;
  right: 50%;
  transform: translateX(50%);
}
</style>