<template>
    <el-carousel :interval="4000" type="card" height="350px">
      <el-carousel-item v-for="image in images" :key="image.id">
        <el-image
            style="width: 500px; height: 300px"
            :src="require('@/assets/' + image.src)"
            fit="fill"></el-image>
          <div style="text-align: center;position: relative; justify-content: center;">
            <span class="demonstration" >{{image.title}}</span>
          </div>
      </el-carousel-item>
    </el-carousel>
  </template>
   
  
  
  <script>
  import axios from 'axios';
  import { ElMessage } from 'element-plus';
  import { useStoryState } from '@/store/story.js';

  export default {
    data() {
      return {
        fits: ['fill', 'contain', 'cover', 'none', 'scale-down'],
        images: [
          // ... array of image objects { id: '', src: '', title: '' }
          { id: 1, src: 'test/1.png', title: '魔法之旅' },
        ],
        selectedIndex: 0,
        historyItems: [],
      };
    },

    created() {
      axios.get("http://127.0.0.1:5000/storyHistory").then((response) => {
        if (response.code == null) {
          console.log(response.data);
          const store = useStoryState();
          store.$patch({
            storyHistory: response.data,
          });
          this.historyItems = response.data;
          this.handleHistoryItems();
        } else {
          console.log(response.code);
          ElMessage({
            message: "生成失败",
            type: "error",
          });
        }
      });
    },

    methods: {
      handleHistoryItems() {
       
        const titles = Object.keys(this.historyItems);
        for (let i = 0; i < titles.length; i++) {
          const ob = Object.keys(this.historyItems[titles[i]]);
          this.images.push({
            id: i + 2,
            src: 'test/image.png',
            title: ob[0],
          });
        }
        // this.images = jsonObj.map((item) => {
        //   return {
        //     // id 自增长
        //     id: this.images.length,
        //     src: 'test/image.png',
        //     title: item,
        //   };
        // });
      },
    },
  };
  </script>
  
  <style>

  .el-carousel__item{
    display: flex;
    flex-direction: column;
    align-items: center;
      }

    .el-carousel__item h3 {
      color: #475669;
      font-size: 14px;
      opacity: 0.75;
      line-height: 200px;
      margin: 0;
    }
    
    .el-carousel__item:nth-child(2n) {
      background-color: #99a9bf;
    }
    
    .el-carousel__item:nth-child(2n+1) {
      background-color: #d3dce6;
    }
  </style>