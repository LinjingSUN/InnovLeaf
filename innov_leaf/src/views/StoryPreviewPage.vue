<template>
    <!-- 设置页面 -->
    <div class="container">
      <!-- 页面的主要内容 -->
        <div class="header">
            <h1>故事生成历史</h1>
        </div>
        <div class="history">
        <div class="content-header">
          <div class="history-show-type">
                <div style="padding-right: 10px;">
                    视图
                </div>
                <div>
                    <el-radio-group v-model="isTable">
                        <el-radio-button :label="false">
                            <el-icon><PictureFilled /></el-icon>
                        </el-radio-button>
                        <!-- <el-radio-button :label="true"> -->
                        <el-radio-button :label="false">
                            <el-icon><List /></el-icon>
                        </el-radio-button>
                    </el-radio-group>
                </div>
            </div>
        </div>

            <div class='history-show'>
                <story-history v-if="!isTable"/>
                <story-history-table v-if="isTable"/>
            </div>
        </div>

    </div>
  </template>

<script>
import StoryHistory from "../components/StoryPreview/StoryHistory.vue";
import StoryHistoryTable from "../components/StoryPreview/StoryHistoryTable.vue";
import { List } from "@element-plus/icons-vue";
import { PictureFilled } from "@element-plus/icons-vue";

export default {
  components: {
    StoryHistory,
    StoryHistoryTable,
    List,
    PictureFilled,
  },
  name: "StoryPreview",

  data() {
    return {
        isTable: false,
    };
  },
  methods: {

  },
  mounted() {
    // Code to run when the component is mounted
  },
};
</script>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  background-image: url("@/assets/background.jpg");
  background-size: cover;
}

.header {
  width: 100%;
  padding: 16px;
  text-align: center;
  /* background-color: #f5f5f5; */
}

.history {
  width: 80%;
  max-width: 1200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.content-header {
  align-self: stretch;
  display: flex;
  justify-content: flex-end;
  padding: 10px 0;
}

.history-show-type {
  display: flex;
  align-items: center;
}

.radio-group {
  margin-left: 10px;
}

.history-show {
  width: 100%;
  /* display: flex; */
  justify-content: center;
  padding: 20px 0; /* This adds padding above and below the history content */
}


</style>
