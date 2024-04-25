<template>
  <div class="reading-page">
    <div class="image-container">
      <img :src="image" alt="Image" />
    </div>
    <div class="text-container">
      <p class="text">Your text goes here</p>
    </div>
  </div>
</template>

<script>
// import { useStore } from '@/store/index.js';

export default {
  created() {
   
  },
  data() {
    return {
      text: '',
      image:""
    };
  },
};
</script>

<style>
.reading-page {
  font-family: "Courier New", Courier, monospace;
  display: flex;
  flex-direction: row;
  padding: 10%;
  box-sizing: border-box;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url("@/assets/background.jpg");
  background-size: cover;
}

.image-container {
  flex: 1;
}

.text-container {
  flex: 1;
  text-align: right;
}

.text {
  font-size: 24px;
}
</style>