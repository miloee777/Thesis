<template>
  <div class="detect-container">
    <div class="detection">
      <h1>Image Detection</h1>
      <input type="file" @change="onFileChange">
      <button class="btn-detect" @click="submitImage">Detect</button>
      <div v-if="detectedImage">
        <h2>Detected Image:</h2>
        <div class="image-container">
          <img :src="detectedImage" alt="Detected Image" ref="detectedImage" @load="isImageLoaded = true">
          <div v-for="(box, index) in predictions" :key="index" :style="getBoundingBoxStyle(box)" class="bounding-box">
            <div class="label">
              {{ box.class }} ({{ (box.confidence * 100).toFixed(2) }}%)
            </div>
          </div>

          <div class="detected-classes" v-if="predictions.length > 0">
            <h3>Detected Classes: </h3>
            <ul>
              <li v-for="(box, index) in predictions" :key="index">
                <router-link :to="getClassLink(box.class)">
                  {{ box.class }} ({{ (box.confidence * 100).toFixed(2) }}%)
                </router-link>
              </li>
            </ul>
          </div>
          <div class="no-detections" v-else>
            <h3>ไม่พบการตรวจจับ หรือ ลองใหม่อีกครั้ง</h3>
          </div>
        </div>
      </div>
      <button class="btn-back" @click="goBack">ย้อนกลับ</button>
    </div>
  </div>
</template>




<script>
import axios from 'axios';

export default {
  name: 'DetectionPage',
  data() {
    return {
      imageFile: null,
      detectedImage: null,
      predictions: [],
      imageWidth: 0,
      imageHeight: 0,
      isImageLoaded: false,
    };
  },
  created() {
    const savedImage = localStorage.getItem('detectedImage');
    const savedPredictions = localStorage.getItem('predictions');
    const savedWidth = localStorage.getItem('imageWidth');
    const savedHeight = localStorage.getItem('imageHeight');

    if (savedImage && savedPredictions && savedWidth && savedHeight) {
      this.detectedImage = savedImage;
      this.predictions = JSON.parse(savedPredictions);
      this.imageWidth = parseFloat(savedWidth);
      this.imageHeight = parseFloat(savedHeight);
    }
  },
  methods: {
    onFileChange(event) {
      this.imageFile = event.target.files[0];
      localStorage.removeItem('detectedImage');
      localStorage.removeItem('predictions');
      localStorage.removeItem('imageWidth');
      localStorage.removeItem('imageHeight');
      this.isImageLoaded = false;
    },
    async submitImage() {
      if (!this.imageFile) {
        alert("Please select an image.");
        return;
      }

      let formData = new FormData();
      formData.append('file', this.imageFile);

      try {
        const response = await axios.post('http://localhost:5000/detect', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        this.predictions = response.data.predictions;
        this.imageWidth = response.data.image_width;
        this.imageHeight = response.data.image_height;

        const reader = new FileReader();
        reader.onload = (e) => {
          this.detectedImage = e.target.result;
          this.isImageLoaded = true;

          // บันทึกข้อมูลใน localStorage
          localStorage.setItem('detectedImage', this.detectedImage);
          localStorage.setItem('predictions', JSON.stringify(this.predictions));
          localStorage.setItem('imageWidth', this.imageWidth);
          localStorage.setItem('imageHeight', this.imageHeight);
        };
        reader.readAsDataURL(this.imageFile);

      } catch (error) {
        console.error("Error during detection:", error);
        alert("Detection failed. Please try again.");
      }
    },
    goBack() {
      this.$router.go(-1);
    },
    getBoundingBoxStyle(box) {
      if (!this.$refs.detectedImage || !this.isImageLoaded) {
        return {};
      }

      const imageElement = this.$refs.detectedImage;
      const scaleX = imageElement.clientWidth / this.imageWidth;
      const scaleY = imageElement.clientHeight / this.imageHeight;
      return {
        left: `${(box.x - box.width / 2) * scaleX}px`,
        top: `${(box.y - box.height / 2) * scaleY}px`,
        width: `${box.width * scaleX}px`,
        height: `${box.height * scaleY}px`,
        position: 'absolute',
        border: '2px solid FireBrick',
        color: 'black',
        backgroundColor: 'rgba(255, 255, 255, 0.3)',
        padding: '2px',
        boxSizing: 'border-box'
      };
    },
    getClassLink(className) {
      if (className === 'nuad-pla-duk') {
        return { name: 'NuadPlaDukInfo' };
      } else if (className === 'ya-kok-sai') {
        return { name: 'YaKokSaiInfo' };
      } else if (className === 'ya-khao-nok') {
        return { name: 'YaKhaoNokInfo' };
      } else if (className === 'phak-pod-na') {
        return { name: 'PhakPodNaInfo' };
      }
      return '/';
    }
  }
}
</script>


<style scoped>
* {

  box-sizing: border-box;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

.detect-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url('D:\Detection-app\frontend\src\assets\nature_bg.jpg');
  background-size: cover; /* ให้ภาพพื้นหลังครอบคลุมทั้ง container */
  background-position: center; /* จัดตำแหน่งภาพให้อยู่ตรงกลาง */
  background-repeat: no-repeat; /* ไม่ให้ภาพซ้ำ */
}

.detection {
  text-align: center;
  padding: 20px;
  width: 100%;
  max-width: 800px;
  /* กำหนด max-width เพื่อไม่ให้เนื้อหากว้างเกินไป */
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
  opacity: 0.9;

  /* จัดให้เนื้อหาอยู่ตรงกลางในแนวนอน */
}


.btn-detect {
  font-size: 17px;
  color: white;
  background-color: #6a9c46;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  padding: 15px 30px;
  margin-left: 20px;

}
.btn-back {
  font-size: 17px;
  color: white;
  background-color: #000000;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  padding: 15px 15px;
  margin-left: 15px;
}
.btn-detect:hover {
  background-color: #5a8c36;
}
.btn-back:hover {
  background-color: #32362f;
}

img {
  width: 320px;
  height: auto;
}

.image-container {
  position: relative;
  display: inline-block;
}

.bounding-box {
  position: absolute;
  border: 2px solid green;
  /* สีขอบเป็นสีเขียว */
  box-sizing: border-box;
}

.label {
  position: absolute;
  top: -20px;
  left: 0;
  background-color: rgba(255, 255, 255, 0.7);
  color: black;
  padding: 2px 4px;
  font-size: 12px;
  white-space: nowrap;
}

.result {
  margin-top: 10px;
}

.detected-classes {
  margin-top: 20px;
}

.detected-classes ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  /* แสดงผลในรูปแบบแถวเดียว */
  gap: 10px;
  /* เพิ่มช่องว่างระหว่างรายการ */
}

.detected-classes li {
  font-size: 16px;
  color: #333;
}

.no-detections {
  margin-top: 15px;
  color: red;
  /* สีแดงเพื่อเน้นข้อความ */
  font-size: 16px;
}


@media (max-width: 600px) {
  .detection {
    padding: 10px;
    max-width: 90%;
    width: 100%;
  }

  .btn-detect,
  .btn-back {
    font-size: 14px;
    padding: 10px 20px;
    margin: 5px;
  }

  img {
    width: 100%;
    max-width: 100%;
  }

  .image-container {
    width: 100%;
  }
}
</style>