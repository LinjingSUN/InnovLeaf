<template>
  <div id="app">
    <router-view></router-view>
    <div class="setting">
      set
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
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

.set{
  position: absolute;
  top: 0;
  right: 0;
}
</style>