<template>
  <div class="container-fluid" style="max-width: 1000px;">
    <h1 class="text-center mb-4">Image Gallery</h1>
    <button @click="fetchData" class="btn btn-primary mb-4">获取三个模型训练对比图</button>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-if="images.length" class="images-container">
      <div v-for="(imageUrl, index) in images" :key="index" class="image-entry">
        <div class="image-name mb-2">{{ extractFileName(imageUrl) }}</div>
        <img :src="imageUrl" :alt="'Image ' + extractFileName(imageUrl)" class="image img-fluid">
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      images: [],
      error: null
    };
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/predictss/list_images/');
        this.images = response.data;
        this.error = null;
      } catch (error) {
        this.images = [];
        this.error = 'Error fetching images';
        console.error('Error fetching images', error);
      }
    },
    extractFileName(url) {
      // 从URL提取文件名
      return url.split('/').pop();
    }
  }
};
</script>

<style>
.images-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.image-entry {
  margin-bottom: 30px;
  text-align: center;
}
.image-name {
  font-weight: bold;
}
.image {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  box-shadow: 2px 2px 4px 0px rgba(0,0,0,0.1);
}
</style>
