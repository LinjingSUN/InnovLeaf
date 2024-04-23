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
        <span class="nick-name">{{ userProfile.nickname
        }}</span>
        
        <el-button
          @click="isEditingChange()"
          type="text"
          class="edit-btn"
        >
          <el-icon color="#409efc"><EditPen /></el-icon></el-button
        >
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
      <input v-model="userProfile.nickname" type="text" class="nickname-input" />
        </div>
        <div class="comfirm">
      <el-button @click="save()" type="success">保存</el-button>
      <el-button @click="cancel()" type="warning">放弃修改</el-button>

      <!-- 确认放弃修改的dialog -->
      <el-dialog
        title="提示"
        width="30%"
        center
      >
        <span>确定放弃修改吗？</span>
        <span class="dialog-footer">
          <el-button @click="centerDialogVisible = false" >取消</el-button>
          <el-button type="primary" @click="cancelEdit()">确定</el-button>
        </span>
      </el-dialog>
    </div>
    </div>
  </div>
</template>

<script>
import { EditPen } from "@element-plus/icons-vue"; 
import {ElMessage} from 'element-plus';

export default {
  name: "AvatarSetting",
  components: {
    EditPen,
  },
  data() {
    return {
      userProfile: {
        avatarUrl: "dan_xiao_fen.png",
        nickname: "蛋小粉",
      },
      centerDialogVisible: false,// 弹出框是否显示
      originalNickname: "蛋小粉", // 保存原始昵称
      isEditing: false, // Add a boolean property to control the editing state
    };
  },
  
  methods: {
    isEditingChange() {
      this.isEditing = !this.isEditing;
      this.originalNickname = this.userProfile.nickname;
    },

    // 保存修改信息
    save() {
      console.log(this.userProfile)
      ElMessage({
        message: "保存成功",
        type: "success",
      });
      this.isEditing = false;
    },

    // 取消修改
    cancel() {
      this.centerDialogVisible = true;
    },

    // 确认取消修改
    cancelEdit() {
      this.userProfile.nickname = this.originalNickname;
      this.isEditing = false;
    },
  }
};
</script>

<style scoped>
.avatar-setting {
  margin-top: -8vh;
  font-family: 'Courier New', Courier, monospace;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.edit-btn {
  font-family: 'Courier New', Courier, monospace;
}

.avatar {
  width: 250px;
  height: 400px;
}

.bottom{
    margin-top: -10vh;
    display: flex;
    justify-content: center;
    align-items: center;
    
}
.comfirm{
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
  font-family: 'Courier New', Courier, monospace;
  opacity: 0.8;
  border-radius: 5px;
  border: none;
  font-size: 20px;
  margin-bottom: 10px;
  text-align: center; 
}
</style>