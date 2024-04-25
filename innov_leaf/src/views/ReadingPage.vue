<template>
  <div class="reading-page">
    <div class="text-container">
      <p class="text">Your text goes here</p>
    </div>
  </div>
</template>

<script>
// import { useStore } from '@/store/index.js';
import { useStoryState} from "@/store/story.js";
export default {
  created() {
   const store = useStoryState();
   console.log(store.$state.storyList);
  },
  data() {
    return {
      storyList: [],
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



.text {
  font-size: 24px;
}
</style>