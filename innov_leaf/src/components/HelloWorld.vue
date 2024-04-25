<template>
  <div class="hello">
    <img src="@/assets/logo_removed.png" alt="logo" class="logo"/>
    <span class="slogan">创叶-用科技连接你我，用智能点亮智慧</span>
    <!-- 在页面中间生成一个大的输入框 -->
    <el-input
      type="textarea"
      :rows="2"
      placeholder="请输入你想要的故事"
      v-model="storyPrompt"
      class="story-input"
    ></el-input>
    

    <el-button type="primary" @click="goView()" :class="btn" size="large" :icon="Check">生成新故事！</el-button>
  </div>
</template>

<script>
import axios from "axios";
import { useStore } from "@/store/index.js";
import { useStoryState} from "@/store/story.js";
import { ElLoading, ElMessage } from "element-plus";
import icon from "@/assets/logo_removed.png";

export default {
  name: "HelloWorld",
  props: {},
  data() {
    return {
      loading: false,
      storyPrompt: "",
    };
  },



  methods: {
    goView() {
      this.generateStory();
    },

    updateInfo() {
      const store = useStore();
      axios
        .post("http://127.0.0.1:5000/user", store.$state)
        .then((response) => {
          if (response.status === 200) {
            // store in state
          } else {
            ElMessage({
              message: "保存失败",
              type: "error",
            });
          }
        });
    },
    generateStory() {
      this.loading = true;
      const loading = ElLoading.service({
        lock: true,
        text: "正在生成故事中...",
        spinner: icon,
        background: "rgba(0, 0, 0, 0.7)",
      });
      axios.get("http://127.0.0.1:5000/story").then((response) => {
        if (response.code == null) {
          console.log(response.data);
          const store = useStoryState();
          store.$patch({
            storyList: response.data.story,
          });
          // console.log(store.$state.storyList);
        } else {
          console.log(response.code);
          ElMessage({
            message: "生成失败",
            type: "error",
          });
        }
        loading.close();
        this.$router.push({ name: "Reading" });
      });
    },

    goSetting() {
      axios
    .get("http://127.0.0.1:5000/user")
    .then((response) => {
      if(response.data != null) {
      console.log(response.data);
      const data = response.data;
      const store = useStore();
      store.$patch({
        readingData: data.readingData,
        interest: data.interest,
        expectionData: data.expectionData,
        userProfile: data.userProfile,
        basicInfoData: data.basicInfoData,
      });
      this.$router.push({ name: "UserSetting" });
    }
    })
    .catch((error) => {
      console.log(error);
      ElMessage({
        message: "获取用户信息失败",
        type: "error",
      });
    });
     
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
  font:  24px "Courier New", Courier, monospace;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url("@/assets/background.jpg");
  background-size: cover;
  position: relative;
}
.logo{
  width: 200px;
  height: 200px;
  position: absolute;
  top: 0vh;
}
.slogan{
  font: italic 18px "Courier New", Courier, monospace;
  position: absolute;
  top: 20vh;
}
.story-input{
  width: 60vw;
  /* 文字居中 */
  text-align: center;
  font-size: 24px;
  margin: 5%;
  border-radius: 60px;
}

.el-textarea__inner, .el-input__inner{
  font-size: 24px;
  background: rgba(249, 246, 246, 0.8) !important;
}

.btn{
  margin-top: 10vh;
  font-size: 30px;
}
</style>
