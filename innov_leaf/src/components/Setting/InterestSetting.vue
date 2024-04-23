<template>
    <div class="interest-setting">
        <h1 class="header">兴趣设置</h1>
        <el-form ref="interestForm" :model="interest" label-width="120px">
            <el-form-item label="故事类型" class="item">
                <el-input v-model="interest.storyType"></el-input>
            </el-form-item>
            <el-form-item label="人物或角色" class="item">
                <el-input v-model="interest.character"></el-input>
            </el-form-item>
            <el-form-item label="情节或主题" class="item">
                <el-input v-model="interest.theme"></el-input>
            </el-form-item>
            <el-form-item label="声音类型" class="item">
                <el-input v-model="interest.sound"></el-input>
            </el-form-item>
            <el-form-item label="颜色或图案" class="item">
                <el-input v-model="interest.color"></el-input>
            </el-form-item>
            <el-form-item label="其他兴趣爱好" class="item">
                <el-input v-model="interest.other" class="item"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="saveInterest">Save</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            interest: {
                storyType: '',
                character: '',
                theme: '',
                sound: '',
                color: '',
                other: ''
            }
        };
    },
    methods: {
        saveInterest() {
            // Handle form submission
        }
    }
}
</script>


<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
}
.header {
    display: flex;
    align-items: center;
    margin-left: 20%;
    font: bold 24px "Courier New", Courier, monospace;
}

.interest-setting {
    width: 50%;
    margin: 0 auto;
}
.item {
    margin-bottom: 10px;
    width:100%;
}
</style>