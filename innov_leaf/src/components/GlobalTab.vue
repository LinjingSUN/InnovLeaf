<template>
  <div class="floating-icons">
    <el-button link @click="goIndex()">
      <el-icon :size="30" class="icon">
        <HomeFilled />
      </el-icon>
    </el-button>

    <el-button link @click="goHistory()">
      <el-icon :size="30" class="icon"><StarFilled /></el-icon>
    </el-button>
    <el-button link @click="goSetting()">
      <el-icon :size="30" class="icon"><SetUp /></el-icon>
    </el-button>
  </div>
</template>

<script>
import { StarFilled, SetUp } from "@element-plus/icons-vue";
import {HomeFilled} from "@element-plus/icons-vue";
import axios from "axios";
import { useStore } from "@/store/index.js";
import { ElMessage } from "element-plus";
export default {
  components: {
    StarFilled,
    SetUp,
    HomeFilled,
  },
  methods: {
    goHistory() {
      this.$router.push({ name: "StoryPreview" });
    },
    goIndex() {
      this.$router.push({ name: "index" });
    },
    goSetting() {
      axios
        .get("http://127.0.0.1:5000/user")
        .then((response) => {
          if (response.data != null) {
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
<style>
.floating-icons {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 9999;
}

.icon {
  width: 30px;
  height: 30px;
  margin-right: 20px;
}
</style>