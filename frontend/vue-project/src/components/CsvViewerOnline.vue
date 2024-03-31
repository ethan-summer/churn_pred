
<template>
  <div class="container-fluid mt-4" style="max-height: 800px; overflow: auto;">
    <div class="d-flex justify-content-between">
      <h2>CSV预测展示</h2> 
      <div>
        <input type="text" v-model="decryptionKey" placeholder="输入密钥" maxlength="8" minlength="8" required class="form-control"/>
        <button @click="decryptData" class="btn btn-success" style="margin: 20px;">解密</button>
        <button @click="viewEncryptedData" class="btn btn-info" style="margin: 20px;">查看加密文件</button>
        <a :href="csvUrl" class="btn btn-primary align-self-center" download>下载</a>
      </div>
    </div>
    <p v-if="decryptFailed">解密失败，请重试。</p>
    <div v-if="csvData.length">
      <table class="table">
        <thead>
          <tr>
            <th scope="col" v-for="(header, index) in headers" :key="index">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, index) in csvData" :key="index">
            <td v-for="(value, key) in row" :key="key">{{ value }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p v-else>暂无返回的加密数据</p>
  </div>
</template>

<script>
import axios from 'axios';
import Papa from 'papaparse';

export default {
  data() {
    return {
      encryptedCsvUrl: 'http://localhost:8000/csv/churn_test_encrypt.csv',
      decryptedCsvUrl: 'http://localhost:8000/csv/churn_test_encrypt_to_decrypt.csv',
      csvUrl: '', // 当前展示的CSV文件的URL
      csvData: [],
      headers: [],
      decryptionKey: '',
      decryptFailed: false,
    };
  },
  mounted() {
    // 初始化时不自动加载数据
  },
  methods: {
    async loadCsvData(url) {
      try {
        const response = await axios.get(url, {
          responseType: 'blob'
        });
        const csvText = await response.data.text();
        const results = Papa.parse(csvText, {
          header: true
        });
        this.csvData = results.data;
        if (results.data.length > 0) {
          this.headers = Object.keys(results.data[0]);
        }
        this.csvUrl = url; // 更新当前展示的CSV文件的URL
      } catch (error) {
        console.error('Error loading CSV data:', error);
      }
    },

    viewEncryptedData() {
      this.loadCsvData(this.encryptedCsvUrl);
    },
    async decryptData() {
      try {
        const response = await axios.post('http://localhost:8000/predictss/churn_predict_decrypt/', {
          key: this.decryptionKey,
        });
        
        if (response.status === 201) {
          this.decryptFailed = false;
          setTimeout(() => {
            this.loadCsvData(this.decryptedCsvUrl); // 加载并展示解密后的数据
          }, 10000);
        } else {
          this.decryptFailed = true;
        }
      } catch (error) {
        console.error('Error decrypting data:', error);
        this.decryptFailed = true;

      }
    }
  }
}
</script>

