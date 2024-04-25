<template>
  <div class="reading-page">
    <!-- title -->
    <div class="title">{{title}}</div>
    <div class="text-container">
        
        <story-content :content="this.text"/>
        <div class="footer">
            <el-button class="btn" type="primary" @click="preStory" :disabled="this.counter == 1"><el-icon><DArrowLeft /></el-icon>上一页</el-button>
            <el-button class="btn" type="primary" @click="nextStory" :disabled="this.counter >= this.storyList.length -1 "><el-icon><DArrowRight /></el-icon>下一页</el-button>
        </div>
    </div>
  </div>
</template>

<script>
// import { useStore } from '@/store/index.js';
import { DArrowRight, DArrowLeft } from '@element-plus/icons-vue';
import { useStoryState} from "@/store/story.js";
import StoryContent from '../components/Reading/StoryContent.vue';
export default {
  components: { StoryContent, DArrowRight, DArrowLeft},

  created() {
   const store = useStoryState();
   console.log(store.$state.storyList);
   this.title = store.$state.storyList[0];
   this.storyList = store.$state.storyList;
   this.text = store.$state.storyList[1];
  },
  data() {
    return {
      counter:1,
      title: "小白兔和小乌龟",
      text:"",
      storyList: [
        "小白兔和小乌龟",
        "小白兔和小乌龟是两个好朋友。小白兔长得白白胖胖，跑得又快又好，小乌龟长得黑黑瘦瘦，跑得又慢又不好。",
            "有一天，小白兔和小乌龟决定比赛跑步。小白兔一听，乐得直拍手：“我一定会赢的！”小乌龟却不以为然：“你跑得那么快，我怎么可能赢得了你？”",
            "比赛开始了，小白兔一马当先，跑在前面。小乌龟慢慢地爬，爬得慢慢地。小白兔看着小乌龟，忍不住哈哈大笑：“你跑得这么慢，怎么可能赢得了我？”",
            "小乌龟不理会小白兔的嘲笑，继续慢慢地爬。过了一会儿，小白兔跑到了终点，高兴地跳了起来：“我赢了！我赢了！”",
            "小乌龟还没有到终点，小白兔以为小乌龟已经放弃了比赛，就走到小乌龟面前，得意地说：“看吧，我说我一定会赢的，你不是说我跑得快吗？现在你输了，你还要不要再比赛一次？”",
            "小乌龟笑了笑，说：“我没有放弃比赛，我还在路上呢。”",
            "小白兔很惊讶，他怎么也没有想到小乌龟还会继续跑。小乌龟慢慢地爬到了终点，对小白兔说：“我知道我跑得慢，但是我坚持到了最后，我赢了！”",
            "小白兔惭愧地低下了头，他知道自己输了。小乌龟虽然跑得慢，但是他坚持到了最后，他赢得了比赛。",
            "小白兔和小乌龟成为了好朋友，他们一起玩耍，一起学习，一起成长。"
      ],
    };
  },

    methods: {
        nextStory() {
            this.counter += 1;
            this.text = this.storyList[this.counter];
            console.log(this.text);
        },
        preStory() {
            this.counter -= 1;
            this.text = this.storyList[this.counter];
        }
    },
};
</script>

<style>
.reading-page {
  font:  24px "Courier New", Courier, monospace;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url("@/assets/background.jpg");
  background-size: cover;
  position: relative;
}

.title {
  position: absolute;
  top: 10vh;
  font-size: 48px;
  color: black;
  font: bold 48px "Courier New", Courier, monospace;
}


.text {
  font-size: 24px;
}

.footer{
    display: flex;
    justify-content:space-between;
    margin-top: 5vh;
}

.btn{
    font-size: large;
}
</style>