<template>
  <div class="reading-habit">
    <div class="header">
      <h1>阅读习惯设置</h1>
    </div>
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="喜欢的阅读方式" class="item">
        <el-select v-model="form.readingMethod" placeholder="请选择">
          <el-option label="纸质书" value="paper"></el-option>
          <el-option label="电子书" value="ebook"></el-option>
          <el-option label="有声书" value="audiobook"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="每次阅读的时长" class="item">
        <el-select v-model="form.readingDuration" placeholder="请选择">
          <el-option label="3分钟以下" value="very short"></el-option>
          <el-option label="3-10分钟" value="short"></el-option>
          <el-option label="10分钟以上" value="medium"></el-option>
          <el-option label="10-30分钟" value="long"></el-option>
          <el-option label="能够长时间阅读" value="very long"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="是否喜欢重复" class="item">
        <el-switch v-model="form.repeatedReading"></el-switch>
      </el-form-item>
      <el-form-item label="其他阅读习惯" class="item">
        <el-input type="textarea" v-model="form.otherHabits"></el-input>
      </el-form-item>
      <el-form-item class="btn">
        <el-button type="primary" @click="submitForm">确认</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
export default {
  data() {
    return {
      form: {
        readingMethod: "",
        readingDuration: "",
        repeatedReading: false,
        otherHabits: "",
      },
    };
  },
  methods: {
    submitForm() {
      ElMessage({
        message: "保存成功",
        type: "success",
      });
      console.log(this.form);
    },
  },
};
</script>

<style scoped>
.reading-habit {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Courier New", Courier, monospace;
  position: relative;
}

.item {
  width: 35vw;
}

.header {
  font: bold 24px "Courier New", Courier, monospace;
}

.btn{
    position: absolute;
    bottom: -20%;
    right: 50%;
    transform: translateX(50%);
}
</style>