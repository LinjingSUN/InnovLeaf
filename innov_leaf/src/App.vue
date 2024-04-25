<template>
  <div id="app">
    
    <!-- <TopBar></TopBar> -->
    <div class="hello">
      <img class="logo left-logo" src="./assets/logo_removed.png">  
      
    <el-tabs v-model="activeName" class="tabs" type="card" @tab-click="handleClick">
      <el-tab-pane label="故事生成"></el-tab-pane>
      <el-tab-pane label="生成历史"></el-tab-pane>
      <el-tab-pane label="其他设置"></el-tab-pane>
    </el-tabs>

    <img class="logo right-logo" src="./assets/dan_xiao_fen.png" @click="goToSettings">
    </div>
    <router-view></router-view>
  </div> 
</template>

<script>


export default {
  name: 'App',
  data() {
      return {
        loading: false,
        activeName: '故事生成',
      };
    },
  methods:{
    handleClick(tab, event) {
          console.log(tab, event);
          console.log(tab.props.label);
  
           if(tab.props.label == "故事生成"){
            this.$router.push({  
                path: '/',
                name: 'index', 
            }) 
          }else if(tab.props.label == "生成历史"){
            this.$router.push({  
                path: '/history',
                name: 'StoryPreview', 
            }) 
          }else if(tab.props.label == "其他设置"){
            this.$router.push({  
                path: '/setting',
                name: 'UserSetting', 
            }) 
          }
      },
    goToSettings() {
      this.$router.push({ path: '/setting' });
    },
  }
}
</script>

<style>
.app{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  width: max-content;
  margin: 0 auto;
  height: max-content;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  /* make it relative to the parent */
  position: relative;
}

.hello {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  height: 60px;
}

.logo {
  /* Use the same class for both logos to apply common styles */
  height: 100%;
}

.left-logo {
  margin-right: auto; /* Pushes everything else to the right */
}

.right-logo {
  margin-left: auto; /* Pushes everything else to the left */
  cursor: pointer; /* Indicates this is clickable */
}

.tabs {
  /* Remove flex-grow and use justify-content: center in .hello to center tabs */
}




</style>