import { defineStore } from "pinia";

// Store 实体
export const useStore = defineStore({
  id: "myGlobalState",
  // state: 返回对象的函数
  state: () => ({
    userProfile: {},
    basicInfoData: {},
    expectionData: {},
    interest: {},
    readingData: {}

  }),
});
