<template>
  <div class="story-content">
    <!-- 播放声音 -->
    <el-button type="primary" @click="playAudio" link class="play">
      <el-icon><Headset /></el-icon>
      播放</el-button
    >
    <!-- 接受父组件中传来的文字内容 -->
    <div class="text">{{ content }}</div>
  </div>
</template>

<script>
import { Headset } from "@element-plus/icons-vue";

// 父组件传给子组件
export default {
  components: {
    Headset,
  },
  data() {
    return {
      text: "测试文字",
    };
  },
  props: {
    content: {
      type: String,
    },
  },
  watch: {
    content() {
      this.$forceUpdate();
      this.text = this.content;
    },
  },
  methods: {
    playAudio() {
      // 播放声音
      const that = this;
      console.log(that.content);
      try {
        this.$http({
          method: "post",
          url: "/speech",
          data: {
            text: that.content,
          },
        }).then((res) => {
          console.log(res);
        });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style>
.story-content {
  /* 文章居中 */
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(249, 246, 246, 0.8);
  padding: 20px;
  width: 60vw;
  height: 40vh;
  border-radius: 20px;
  position: relative;
}

.text {
  font-size: 24px;
  text-align: center;
  line-height: 1.5;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.play {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
}
</style>