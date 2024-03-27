<template>
  <div class="container-fluid" style="max-width: 1000px;">
    <h1 class="text-center mb-4">Image Gallery</h1>
    <!-- Add a select dropdown for model selection -->
    <div class="mb-3">
      <label for="modelSelect" class="form-label">选择模型</label>
      <select v-model="selectedModel" class="form-select" id="modelSelect">
        <option disabled value="">请选择要查看的模型</option>
        <option >LogisticRegression</option>
        <option>XGBoost</option>
        <option>RandomForest</option>
        <option>三模型对比图</option>
      </select>
    </div>
    <button @click="fetchData" class="btn btn-primary mb-4">获取模型训练评估图</button>
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
      error: null,
      selectedModel: '' // Add a data property for the selected model
    };
  },
  methods: {
    async fetchData() {
      if (!this.selectedModel) {
        this.error = 'Please select a model before fetching images.';
        return;
      }
      try {
        // Adjust the axios call to send a POST request
        const response = await axios.post('http://localhost:8000/predictss/list_images/', {
          model: this.selectedModel
        });
        console.log(response)
        this.images = response.data;
        this.error = null;
      } catch (error) {
        this.images = [];
        this.error = 'Error fetching images';
        console.error('Error fetching images', error);
      }
    },
    extractFileName(url) {
      // Extract the file name from URL
      return url.split('/').pop();
    }
  }
};
</script>

<style>
/* No changes in the style */
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
