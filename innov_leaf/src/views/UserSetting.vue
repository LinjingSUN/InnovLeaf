<template>
  <div class="container">
    <div class="content">
    <div class="ava-btns">
      <!-- 头像及昵称 -->
      <div class="avatar-setting">
        <avatar-setting />
      </div>

      <!-- 用户设置表单按钮 -->
      <div class="setting-buttons">
        <el-button class="setting-btn" type="primary" @click="basicInfo"
          >基本信息</el-button
        >
        <el-button class="setting-btn" type="primary" @click="basicInfo"
          >兴趣设置</el-button
        >
        <el-button class="setting-btn" type="primary" @click="basicInfo"
          >阅读习惯</el-button
        >
        <el-button class="setting-btn" type="primary" @click="basicInfo"
          >期望</el-button
        >
      </div>
    </div>
    <!-- 用户设置表单 -->
    <div class="setting-forms"></div>
</div>
  </div>
</template>

<script>
import AvatarSetting from "../components/Setting/AvatarSetting.vue";


export default {
  components: { AvatarSetting },
  name: "UserSetting",

  data() {
    return {
     
    };
  },
  methods: {
    // Your methods go here
    onSubmit() {
      console.log("Form submitted!");
      console.log(this.form);
    },
    basicInfo() {
      console.log("Basic Info");
    },
  },
  mounted() {
    // Code to run when the component is mounted
  },
};
</script>

<style scoped>

.container {
    font-family: 'Courier New', Courier, monospace;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-image: url("@/assets/background.jpg");
    background-size:cover; 
}

.content{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 80%;
    height: 80%;
    background-color: rgba(255, 255, 255, 0.6);
    border-radius: 20px;
    padding: 20px;

}

.setting-buttons {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  margin-top: 20px;
}

.setting-btn {
  margin-bottom: 10px;
}

.setting-forms {
  display: flex;
  margin-left: 20px;
  width: 60%;
  height: 500px;
  background-color: aquamarine;
}
</style>