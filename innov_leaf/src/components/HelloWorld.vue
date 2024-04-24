<template>
  <div class="hello">
    <h1>Hello World!
    </h1>
    <button @click="goView()">
      Click me
    </button>

    <button @click="goSetting()">
      Click me to setting page
    </button>
  </div>
</template>

<script>
import axios from "axios";
import { useStore } from "@/store/index.js";
export default {
  name: 'HelloWorld',
  props: {
    
  },

  created() {
    axios
    .get("http://127.0.0.1:5000/user")
    .then((response) => {
      if(response.data != null) {
      console.log(response.data);
      const data = response.data;
      const store = useStore();
      store.$patch({
        readingData: data.readingData,
        interest: data.interest,
        expectionData: data.expectionData,
        userProfile: data.userProfile,
        basicInfoData: data.basicInfoData,
      });
    }
    })
    .catch((error) => {
      console.log(error);
    });
  },
  


  methods: {
    goView() {
      this.$router.push({ name: 'Reading' });
    },

    goSetting() {
      this.$router.push({ name: 'UserSetting' });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
