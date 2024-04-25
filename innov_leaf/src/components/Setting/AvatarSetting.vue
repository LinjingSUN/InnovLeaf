<template>
  <div class="avatar-setting">
    <!-- 当处于浏览模式，不可修改 -->
    <div v-if="!isEditing">
      <img
        :src="require('@/assets/' + userProfile.avatarUrl)"
        alt="Avatar"
        class="avatar"
      />

      <div class="bottom">
        <span class="nick-name">{{ userProfile.nickname }}</span>

        <el-button @click="isEditingChange()" link class="edit-btn">
          <el-icon color="#409efc"><EditPen /></el-icon
        ></el-button>
      </div>
    </div>

    <!-- 处于修改模式 -->
    <div v-else>
      <img
        :src="require('@/assets/' + userProfile.avatarUrl)"
        alt="Avatar"
        class="avatar"
      />
      <div class="bottom">
        <input
          v-model="userProfile.nickname"
          type="text"
          class="nickname-input"
        />
      </div>
      <div class="comfirm">
        <el-button @click="save()" type="success">保存</el-button>
        <el-button @click="cancel()" type="warning">放弃修改</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import { EditPen } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import { useStore } from "@/store/index.js";
import axios from "axios";

export default {
  name: "AvatarSetting",
  components: {
    EditPen,
  },

  data() {
    return {
      userProfile: {
        avatarUrl: "",
        nickname: "",
      },
      originalNickname: "蛋小粉", // 保存原始昵称
      isEditing: false, // Add a boolean property to control the editing state
    };
  },

  // 在页面渲染之前获取pinia store中的数据
  created() {
    const store = useStore();
    this.userProfile = store.$state.userProfile;
  },

  methods: {
    isEditingChange() {
      this.isEditing = !this.isEditing;
      this.originalNickname = this.userProfile.nickname;
    },

    // 保存修改信息
    save() {
      const store = useStore();
      try {
        store.$patch({
          userProfile: this.userProfile,
        });
      } catch (error) {
        this.userProfile.nickname = this.originalNickname;
        ElMessage({
          message: "保存失败",
          type: "error",
        });
      }

      axios
        .post("http://127.0.0.1:5000/user", this.userProfile)
        .then((response) => {
          if (response.status === 200) {
            ElMessage({
              message: "保存成功",
              type: "success",
            });
          }
          else {
            this.userProfile.nickname = this.originalNickname;
            ElMessage({
              message: "保存失败",
              type: "error",
            });
          }
        });
      
      this.isEditing = false;
    },

    // 取消修改
    cancel() {
      this.centerDialogVisible = true;
      this.userProfile.nickname = this.originalNickname;
      this.isEditing = false;
    },
  },
};
</script>

<style scoped>
.avatar-setting {
  font-family: "Courier New", Courier, monospace;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.edit-btn {
  font-family: "Courier New", Courier, monospace;
}

.avatar {
  width: 15vw;
  height: 40vh;
}

.bottom {
  margin-top: -10vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.comfirm {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1vh;
}
.nick-name {
  font-size: 20px;
  margin-right: 10px;
}

.nickname-input {
  font-family: "Courier New", Courier, monospace;
  opacity: 0.8;
  border-radius: 5px;
  border: none;
  font-size: 20px;
  margin-bottom: 10px;
  text-align: center;
}
</style>