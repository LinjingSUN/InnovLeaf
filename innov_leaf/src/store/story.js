import { defineStore } from "pinia";

// Store 实体
export const useStoryState = defineStore({
  id: "myGlobalState",
  // state: 返回对象的函数
  state: () => ({
      storyList: [],
      storyName: {},

  }),
});
