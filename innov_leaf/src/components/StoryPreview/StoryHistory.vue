<template>
    <el-carousel :interval="4000" type="card" height="350px">
      <el-carousel-item v-for="image in images" :key="image.id">
        <el-image
            style="width: 500px; height: 300px"
            :src="require('@/assets/' + image.src)"
            :fit="fit"></el-image>
          <div style="text-align: center;position: relative; justify-content: center;">
            <span class="demonstration" >{{image.title}}</span>
          </div>
      </el-carousel-item>
    </el-carousel>
  </template>
   
  
  
  <script>
  export default {
    data() {
      return {
        fits: ['fill', 'contain', 'cover', 'none', 'scale-down'],
        images: [
          // ... array of image objects { id: '', src: '', title: '' }
          { id: 1, src: 'test/1.png', title: '魔法之旅' },
          { id: 2, src: 'test/2.png', title: '大海的呼唤' },
          { id: 3, src: 'test/3.png', title: '森林的秘密' },
          { id: 4, src: 'test/4.png', title: '森林的秘密' },
          { id: 5, src: 'test/5.png', title: '森林的秘密' },
          { id: 6, src: 'test/6.png', title: '森林的秘密' }
        ],
        selectedIndex: 0
      };
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