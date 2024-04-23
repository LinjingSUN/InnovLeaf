<template>
    <div class="reading-habit">
        <el-form ref="form" :model="form" label-width="120px">
            <el-form-item label="Name">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="Email">
                <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm">Submit</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: '',
                email: ''
            }
        };
    },
    methods: {
        submitForm() {
            this.$refs.form.validate((valid) => {
                if (valid) {
                    // Form is valid, perform form submission logic here
                    console.log('Form submitted');
                } else {
                    // Form is invalid, handle validation errors here
                    console.log('Form validation failed');
                }
            });
        }
    }
};
</script>

<style>
/* Add your custom styles here */

</style>