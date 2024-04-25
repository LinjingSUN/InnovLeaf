<template>
  <!-- 设置页面 -->
  <div class="container">
    <!-- 页面的主要内容 -->
    <div class="content">

      <div>

        <!-- 头像及昵称 -->
        <div class="avatar-setting">
          <avatar-setting />
        </div>

        <!-- 用户设置表单按钮 -->
        <div class="setting-buttons">
          <el-button
            class="setting-btn"
            :type="isSettingBasicInfo ? 'primary' : 'default'"
            @click="settingBasicInfo()"
            >基本信息</el-button
          >
          <el-button
            :type="isSettingInterest ? 'primary' : 'default'"
            class="setting-btn"
            @click="settingInterest()"
            >兴趣设置</el-button
          >
          <el-button
            class="setting-btn"
            :type= "isSettingReadingHabit ? 'primary' : 'default'"
            @click="settingReadingHabit()"
            >阅读习惯</el-button
          >
          <el-button
            class="setting-btn"
            :type="isSettingExpectation ? 'primary' : 'default'"
            @click="settingExpectation()"
            >期望</el-button
          >
        </div>
      </div>
      <!-- 用户设置表单 -->
      <div class="setting-forms">
        <basic-info-setting v-if="isSettingBasicInfo" />
        <interest-setting v-if="isSettingInterest" />
        <reading-habit-setting v-if="isSettingReadingHabit" />
        <expectation-setting v-if="isSettingExpectation" />
      </div>
    </div>
  </div>
</template>

<script>
import AvatarSetting from "../components/Setting/AvatarSetting.vue";
import BasicInfoSetting from "../components/Setting/BasicInfoSetting.vue";
import InterestSetting from "../components/Setting/InterestSetting.vue";
import ReadingHabitSetting from "../components/Setting/ReadingHabitSetting.vue";
import ExpectationSetting from "../components/Setting/ExpectionSetting.vue";
// import axios from "axios";
// import { useStore } from "@/store/index.js";

export default {
  components: {
    AvatarSetting,
    BasicInfoSetting,
    InterestSetting,
    ReadingHabitSetting,
    ExpectationSetting,
  },
  name: "UserSetting",

  data() {
    return {
      isSettingBasicInfo: true,
      isSettingInterest: false,
      isSettingReadingHabit: false,
      isSettingExpectation: false,
    };
  },
  // before create, request data from the serve

  
  methods: {
   

    settingBasicInfo() {
      this.isSettingBasicInfo = true;
      this.isSettingInterest = false;
      this.isSettingReadingHabit = false;
      this.isSettingExpectation = false;
    },
    settingInterest() {
      this.isSettingBasicInfo = false;
      this.isSettingInterest = true;
      this.isSettingReadingHabit = false;
      this.isSettingExpectation = false;
    },
    settingReadingHabit() {
      this.isSettingBasicInfo = false;
      this.isSettingInterest = false;
      this.isSettingReadingHabit = true;
      this.isSettingExpectation = false;
    },
    settingExpectation() {
      this.isSettingBasicInfo = false;
      this.isSettingInterest = false;
      this.isSettingReadingHabit = false;
      this.isSettingExpectation = true;
    },
  },
  mounted() {
    // Code to run when the component is mounted
  },
};
</script>

<style scoped>
.container {
  font-family: "Courier New", Courier, monospace;
  display: flex;
  flex-direction: row;
  /*居中*/
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url("@/assets/background.jpg");
  background-size: cover;
}

.content {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 80%;
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 20px;
  padding: 20px;
}

.setting-buttons {
  display: flex;
  flex-direction: column;
  margin-top: 10%;
}

.setting-btn {
  margin-bottom: 10px;
  width: 80%;
  padding: 0;
  margin-top: 10px;
}

.setting-buttons button:first-child {
  margin-left: 5%;
  padding-left: 0;
}
.setting-forms {
  display: flex;
  flex-direction: column;
  align-content: center;
  margin-left: 10px;
  height: 500px;
  width:60%;
}


</style>