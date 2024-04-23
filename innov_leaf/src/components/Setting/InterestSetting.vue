<template>
    <div>
        <el-form ref="interestForm" :model="interest" label-width="120px">
            <el-form-item label="Name">
                <el-input v-model="interest.name"></el-input>
            </el-form-item>
            <el-form-item label="Description">
                <el-input v-model="interest.description"></el-input>
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
                name: '',
                description: ''
            }
        };
    },
    methods: {
        saveInterest() {
            // Handle saving the interest data here
            console.log(this.interest);
        }
    }
};
</script>

<style>
/* Add your custom styles here */
</style>