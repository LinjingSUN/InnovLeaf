<template>
  <div class="basic-info">
    <div class="header">
      <h1>基本信息</h1>
    </div>

    <el-form class="form" ref="form" :model="basicInfoData" label-width="120px">
      <!-- 年龄 -->
      <el-form-item label="年龄" class="form-item">
        <el-input-number v-model="basicInfoData.age"></el-input-number>
      </el-form-item>

      <!-- 性别 -->
      <el-form-item label="性别" class="form-item">
        <el-select v-model="basicInfoData" placeholder="请选择性别">
          <el-option value="男">男</el-option>
          <el-option value="女">女</el-option>
        </el-select>
      </el-form-item>

      <!-- 语言能力 -->
      <el-form-item label="语言能力" class="form-item">
        <div class="select-with-icon">
          <el-select
            v-model="basicInfoData.language"
            placeholder="请选择语言能力"
          >
            <el-option
              v-for="item in languageOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
          <el-button type="text" @click="openLan()" class="select-icon">
            <el-icon><QuestionFilled /></el-icon>
          </el-button>
        </div>
      </el-form-item>

      <!-- 感官偏好 -->
      <el-form-item label="感官偏好" class="form-item">
        <el-checkbox-group v-model="basicInfoData.sensory">
          <el-checkbox value="听觉">听觉</el-checkbox>
          <el-checkbox value="视觉">视觉</el-checkbox>
          <el-checkbox value="触觉">触觉</el-checkbox>
          <el-checkbox value="味觉">味觉</el-checkbox>
        </el-checkbox-group>
      </el-form-item>

      <!-- 尽量避免的描述 -->
      <el-form-item label="尽量避免的描述" class="form-item">
        <el-input
          type="textarea"
          placeholder="请输入尽量避免的描述，如触发不良情绪的词汇、儿童本人害怕的动物等"
          v-model="basicInfoData.description"
        ></el-input>
      </el-form-item>

      <!--  -->
      <el-form-item>
        <el-button type="primary" @click="submitForm">确认</el-button>
      </el-form-item>
    </el-form>

    <!-- 弹窗 -->
    <el-dialog
      v-model="dialogVisible"
      title="语言能力参考"
      width="500"
    >
      关于自闭症患者的语言能力，可以参考以下几个阶段的分类。注意，以下分类不具有诊断级别的准确性，仅供参考。<br />
      <ul>
        <li>
          <strong>非语言阶段（Non-verbal）:</strong><br />
          在这一阶段的患者可能完全不使用口头语言进行交流。<br />
          可能使用一些非言语的交流方式，如手势、面部表情或通过辅助交流设备。
        </li>

        <li>
          <strong>单词或短语阶段（Single words or phrases）:</strong><br />
          能够使用单个词语或简短的短语来表达自己的需要和感受，但通常不构成完整的句子。<br />
          可能会有回声言语，即重复他人的话语。
        </li>

        <li>
          <strong>功能性交流阶段（Functional communication）:</strong><br />
          能够使用简单的句子进行基本的交流。<br />
          语言使用主要是为了满足具体的需求，如要求帮助、请求物品等。
        </li>

        <li>
          <strong>叙述性语言阶段（Narrative language）:</strong><br />
          能够使用更复杂的句子和语言结构来进行叙述。<br />
          在这个阶段的患者可以分享过去的经历、描述未来的计划或讲故事。
        </li>

        <li>
          <strong
            >先进的语言和抽象思维阶段（Advanced language and abstract
            thinking）:</strong
          ><br />
          语言能力接近或达到正常发展水平的个体。<br />
          能够进行抽象思维和使用复杂的语言结构进行有效的交流。
        </li>
      </ul>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="dialogVisible = false" type="success"
            >了解了！</el-button
          >
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import {ElMessage} from 'element-plus';

import { QuestionFilled } from "@element-plus/icons-vue";

export default {
  components: {
    QuestionFilled,
  },
  data() {
    return {
      basicInfoData: {
        age: 7,
        language: "",
        sex: "",
        sensory: [],
        description: "",
      },
      languageOptions: [
        { value: "non-verbal", label: "非语言阶段" },
        { value: "single-words-phrases", label: "单词或短语阶段" },
        { value: "functional-communication", label: "功能性交流阶段" },
        { value: "narrative-language", label: "叙述性语言阶段" },
        {
          value: "advanced-language-abstract-thinking",
          label: "先进的语言和抽象思维阶段",
        },
      ],

      dialogVisible: false,
    };
  },

  methods: {
    submitForm() {
      // Handle form submission
      ElMessage({
        message: "保存成功",
        type: "success",
      });
      console.log(this.basicInfoData);
    },
    openLan() {
      this.dialogVisible = true;
    },
  },
};
</script>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.basic-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Courier New", Courier, monospace;
  position: relative;
}

.header {
  font: bold 24px "Courier New", Courier, monospace;
}

.select-with-icon {
  position: relative;
  width: 100%;
}

.select-icon {
  position: absolute;
  right: -10%;
  font-size: 20px;
  top: 50%;
  transform: translateY(-50%);
}
.form-item {
    width: 35vw;
}
</style>