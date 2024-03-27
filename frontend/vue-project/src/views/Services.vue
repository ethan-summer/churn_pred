<template>
  <div class="container-fluid" style="min-height: 100vh; margin-bottom: 30px;">
    <div class="mb-3" style="margin-top: 30px;">
      <label for="formFile" class="form-label">请上传你的数据文件</label>
      <input class="form-control" type="file" id="formFile" ref="file" @change="handleFileChange">
    </div>
    
    <!-- 模型选择框 -->
    <div class="mb-3">
      <label for="modelSelect" class="form-label">选择模型</label>
      <select class="form-select" id="modelSelect" v-model="selectedModel">
        <option disabled value="">请选择一个模型</option>
        <option value="logic">LogisticRegression</option>
        <option value="xgboost">XGBoost</option>
        <option value="random_forest"> RandomForest</option>
      </select>
    </div>

    <!-- 密钥输入框 -->
    <div class="mb-3">
      <label for="encryptionKey" class="form-label">输入密钥（8个字符）</label>
      <input type="text" class="form-control" id="encryptionKey" v-model="encryptionKey" maxlength="8" placeholder="请输入密钥">
    </div>

    <div class="container d-flex flex-column justify-content-center align-items-center" style="margin-top: 20px;">
      <button class="btn btn-primary" @click="uploadFile">上传文件</button>
    </div>

    <div v-if="uploadPercentage > 0" class="progress" style="margin-top: 20px;">
      <div class="progress-bar" role="progressbar" :style="{ width: uploadPercentage + '%' }" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">{{ uploadPercentage }}%</div>
    </div>

    <div v-if="uploadSuccess" class="alert alert-success" style="margin-top: 20px;">文件上传成功！</div>
  
    <div v-if="uploadSuccess" class="alert alert-success" style="margin-top: 20px;">
      <button class="btn btn-primary" @click="handlePredictModel" :disabled="predicting">模型预测</button>
    </div>

    <div v-if="predicting" class="progress" style="margin-top: 20px;">
      <div class="progress-bar" role="progressbar" :style="{ width: predictPercentage + '%' }" aria-valuenow="predictPercentage" aria-valuemin="0" aria-valuemax="100">{{ remainingTime }}s</div>
    </div>

    <CsvViewer :file="selectedFile"></CsvViewer>
      <CsvViewerOnline />
      <!--在这里写一个解密按钮-->
  </div>
</template>

<script>
import CsvViewer from '@/components/CsvViewer.vue';
import CsvViewerOnline from '@/components/CsvViewerOnline.vue';

import { uploadFile, predictModel } from '@/api/api';

export default {
  components: {
    CsvViewer,
    CsvViewerOnline
  },
  data() {
    return {
      uploadPercentage: 0,
      uploadSuccess: false,
      selectedFile: null,
      predicting: false,
      predictPercentage: 0,
      remainingTime: 100,
      selectedModel: '', // 添加模型选择数据
      encryptionKey: '', // 添加密钥数据
    };
  },
  methods: {
    handleFileChange() {
      const files = this.$refs.file.files;
      if (files.length > 0) {
        this.selectedFile = files[0];
      }
    },
    async uploadFile() {
      this.uploadSuccess = false;
      const formData = new FormData();
      const file = this.$refs.file.files[0];
      formData.append("file", file);
      formData.append("model", this.selectedModel); // 将模型信息添加到formData
      formData.append("key", this.encryptionKey); // 将密钥信息添加到formData

      try {
        const response = await uploadFile(formData, progressEvent => {
          this.uploadPercentage = parseInt(Math.round((progressEvent.loaded / progressEvent.total) * 100));
        });
        this.uploadSuccess = true;
        console.log('File uploaded successfully', response);
      } catch (error) {
        this.uploadSuccess = false;
        console.error('Error uploading file', error);
        alert("文件上传失败，请重试。");
      }
    },
    async handlePredictModel() {
     
      this.predicting = true;
      this.predictPercentage = 0;
      this.remainingTime = 100;

      const intervalId = setInterval(() => {
        if (this.remainingTime > 0) {
          this.remainingTime -= 1;
          this.predictPercentage = (1 - this.remainingTime / 100) * 100;
        } else {
          clearInterval(intervalId);
          this.predicting = false;
        }
      }, 960); // 假设预测耗时96秒，这里用960毫秒更新一次进度

      try {
        console.log("模型预测开始");
        // 注意：这里调用预测模型API时可能需要根据实际API要求调整，比如是否需要传递模型和密钥信息
        const response = await predictModel({ model: this.selectedModel, key: this.encryptionKey }); // 假设API需要模型和密钥信息
        console.log('Prediction response:', response);
        // 处理响应数据，这里需要根据实际返回数据结构进行处理
      } catch (error) {
        console.error('预测过程中发生错误:', error.message);
        // 处理错误
      } finally {
        this.predicting = false; // 确保预测状态被重置
        clearInterval(intervalId); // 清除计时器
      }
    },
  },
};
</script>
