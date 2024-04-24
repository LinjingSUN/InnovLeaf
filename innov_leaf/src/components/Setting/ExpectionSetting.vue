<template>
  <div class="expectation-setting">
    <div class="header">
      <h1>家长期望设置</h1>
    </div>
    <el-form ref="form" :model="expectionData" label-width="120px" label-position="top">
      <el-form-item label="希望通过阅读故事达到什么目标:" class="item">
        <el-input v-model="expectionData.readingGoal"></el-input>
      </el-form-item>
      <el-form-item label="希望故事能够帮助孩子在哪些方面取得进步:" class="item">
        <el-input v-model="expectionData.improvementAreas" ></el-input>
      </el-form-item>
      <el-form-item label="对故事内容有什么特别要求:" class="item">
        <el-input v-model="expectionData.storyRequirements"></el-input>
      </el-form-item>
      <el-form-item class="btn">
        <el-button type="primary" @click="submitForm">确认</el-button>
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
      expectionData: {
        readingGoal: "",
        improvementAreas: "",
        storyRequirements: "",
      },
    };
  },

  // 在页面渲染之前获取pinia store中的数据
  created() {
    const store = useStore();
    this.expectionData = store.$state.expectionData;
  },

  methods: {
    submitForm() {
      try  {
        const store = useStore();
        store.$patch({
          expectionData: this.expectionData,
        });

        ElMessage({
          message: "保存成功",
          type: "success",
        });
        // Handle form submission
        //console.log(this.expectionData);
      } catch (error) {
        ElMessage({
          message: "保存失败",
          type: "error",
        });
      }

      axios
        .post("http://127.0.0.1:5000/user", this.expectionData)
        .then((response) => {
          if (response.status === 200) {
            ElMessage({
              message: "保存成功",
              type: "success",
            });
          }
          else {
            ElMessage({
              message: "保存失败",
              type: "error",
            });
          }
        });
      // Handle form submission
      //console.log(this.expectionData);
    },
  },
};
</script>


<style scoped>
.expectation-setting {
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

.item .el-form-item__label {
    display: block;
}

.item .el-form-item__content {
    margin-left: 0;
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