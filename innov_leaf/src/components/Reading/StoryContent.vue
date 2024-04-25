<template>
    <div class="story-content">
        <!-- 接受父组件中传来的文字内容 -->
        <div class="text">{{ content }}</div>
    </div>
</template>

<script>

// 父组件传给子组件
export default {
    props: {
        content: {
            type: String,
        }
    },
    watch: {
        content() {
            this.$forceUpdate();
        }
    },
    created() {
        console.log("接受到的content："+this.content);
    },
}

</script>

<style>
.story-content {
    /* 文章居中 */
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(249, 246, 246, 0.8);
    padding: 20px;
    width: 60vw;
    height: 40vh;
    border-radius: 20px;
}

.text{
    font-size: 24px;
    text-align: center;
    line-height: 1.5;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
</style>