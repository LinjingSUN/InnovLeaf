<template>
  <div class="hello">
    <h1>Hello World!</h1>
    <button @click="goView()">Click me to generate the story</button>
    <br />
    <button @click="goSetting()">Click me to setting page</button>
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
</style>
