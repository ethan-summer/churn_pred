<template>
  <div v-if="csvData.length > 0" class="container-fluid mt-4" style="max-height: 800px; overflow: auto;">
    <h5>CSV文件内容：</h5>
    <table class="table">
      <thead>
        <tr>
          <th scope="col" v-for="(header, index) in csvHeaders" :key="index">{{ header }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, rowIndex) in csvData" :key="rowIndex">
          <td v-for="(value, colIndex) in row" :key="colIndex">{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import Papa from 'papaparse';

export default {
  props: ['file'],
  data() {
    return {
      csvData: [],
      csvHeaders: [],
    };
  },
  watch: {
    file(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.parseCSV();
      }
    }
  },
  methods: {
    parseCSV() {
  if (!this.file) return;
  Papa.parse(this.file, {
    complete: (results) => {
      const dataIndex = results.data[0].indexOf('id'); // 查找'id'列的索引
      if (dataIndex !== -1) {
        // 如果找到'id'列，则从headers中移除
        this.csvHeaders = results.data[0].filter((_, index) => index !== dataIndex);
        // 同时从每行数据中移除'id'列
        this.csvData = results.data.slice(1).map(row => row.filter((_, index) => index !== dataIndex));
      } else {
        // 如果没有'id'列，直接赋值
        this.csvHeaders = results.data[0];
        this.csvData = results.data.slice(1);
      }
    },
    header: false
  });
}
},
  mounted() {
    this.parseCSV(); // Initial parse in case the file is already set on mount
  }
}
</script>
