<template>
  <div class="detect-container">
    <div class="detection">
      <h1 class="rainbow-text">Weeds Detection System </h1>
      <input type="file" @change="onFileChange" class="file-input">

      <!-- ปุ่มสำหรับอัปโหลดและเปิดกล้อง -->
      <!-- ปุ่มสำหรับอัปโหลดและเปิด/ปิดกล้อง -->
      <div class="button-group">
        <button class="btn-detect" @click="submitImage">Detect</button>
        <button class="btn-detect-cam" @click="toggleCamera">
          {{ cameraOpened ? 'ปิดกล้อง' : 'เปิดกล้อง' }}
        </button>
      </div>
      <div>
        <h5>** ปิดกล้อง ก่อนเลือกไฟล์ **</h5>
      </div>
      <!-- แสดงกล้องถ้าเปิดแล้ว -->
      <div v-show="cameraOpened" class="video-container">
        <video ref="video" autoplay></video>
        <button class="btn-detect-cap" @click="captureImage">ถ่ายรูป</button>
      </div>

      <!-- แสดงภาพที่ตรวจจับแล้ว -->
      <div v-if="detectedImage">
        <h2>Detected Image:</h2>
        <div class="image-container">
          <img :src="detectedImage" alt="Detected Image" ref="detectedImage" @load="isImageLoaded = true">
          <div v-for="(box, index) in predictions" :key="index" :style="getBoundingBoxStyle(box)" class="bounding-box">
            <div class="label">
              {{ box.class }} ({{ (box.confidence * 100).toFixed(2) }}%)
            </div>
          </div>
        </div>

        <div class="detected-classes" v-if="predictions.length > 0">
          <h3>Detected Classes: </h3>
          <ul>
            <li v-for="(box, index) in predictions" :key="index">
              <router-link :to="getClassLink(box.class).name">
                {{ getClassLink(box.class).displayName }} ({{ (box.confidence * 100).toFixed(2) }}%)
              </router-link>
            </li>
          </ul>
        </div>

        <div class="no-detections" v-else>
          <h3>ไม่พบการตรวจจับ หรือ ลองใหม่อีกครั้ง</h3>
        </div>
      </div>

      <!-- ปุ่มย้อนกลับ -->
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
      cameraOpened: false,  // สำหรับตรวจสอบว่ากล้องเปิดหรือไม่
      capturedImage: null  // สำหรับเก็บภาพที่ถ่ายจากกล้อง
    };
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
      if (!this.imageFile && !this.capturedImage) {
        alert("กรุณาเลือกหรือถ่ายภาพก่อน.");
        return;
      }

      let formData = new FormData();
      formData.append('file', this.imageFile || this.capturedImage);

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

          localStorage.setItem('detectedImage', this.detectedImage);
          localStorage.setItem('predictions', JSON.stringify(this.predictions));
          localStorage.setItem('imageWidth', this.imageWidth);
          localStorage.setItem('imageHeight', this.imageHeight);
        };
        reader.readAsDataURL(this.imageFile || this.capturedImage);

      } catch (error) {
        console.error("Error during detection:", error);
        alert("Detection failed. Please try again.");
      }
    },
    toggleCamera() {
      if (this.cameraOpened) {
        // ปิดกล้อง
        let videoElement = this.$refs.video;
        let stream = videoElement.srcObject;
        let tracks = stream.getTracks();

        tracks.forEach(track => track.stop());
        videoElement.srcObject = null;
        this.cameraOpened = false;
      } else {
        // เปิดกล้อง
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
              const videoElement = this.$refs.video; // อ้างอิงถึง video element
              if (videoElement) {
                videoElement.srcObject = stream; // ตั้งค่า srcObject ให้กับ video
                this.cameraOpened = true;
              } else {
                console.error("Video element not found.");
                alert("ไม่สามารถหาวิดีโอสำหรับแสดงผลได้");
              }
            })
            .catch(error => {
              console.error("Cannot open camera", error);
              alert("ไม่สามารถเปิดกล้องได้: " + error.message);
            });
        } else {
          alert("เบราว์เซอร์นี้ไม่รองรับการใช้งานกล้อง");
        }
      }
    },
    captureImage() {
      const video = this.$refs.video;
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const context = canvas.getContext('2d');
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      canvas.toBlob(blob => {
        this.capturedImage = blob;
        this.cameraOpened = false;  // ปิดกล้องหลังจากถ่ายรูปแล้ว
      });
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
        return { name: 'Nuad-PlaDuk-Info', displayName: 'หญ้าหนวดปลาดุก' };
      } else if (className === 'ya-kok-sai') {
        return { name: 'ya-kok-sai-info', displayName: 'หญ้ากกทราย' };
      } else if (className === 'ya-khao-nok') {
        return { name: 'ya-khao-nok-info', displayName: 'หญ้าข้าวนก' };
      } else if (className === 'phak-pod-na') {
        return { name: 'PhakPodNaInfo', displayName: 'หญ้าผักปอดนา' };
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

html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

.rainbow-text {
  font-size: 2.5em;
  font-weight: bold;
  background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red, indigo, rgb(17, 121, 206));
  -webkit-background-clip: text;
  color: transparent;
  background-size: 300% 300% ; /* ขยายแบ็คกราวน์เพื่อให้สามารถเลื่อนได้ */
  animation: rainbow-animation 5s linear infinite;
}

@keyframes rainbow-animation {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 100% 50%;
  }
}

.detect-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url('D:\Detection-app\frontend\src\assets\nature_bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.detection {
  text-align: center;
  padding: 20px;
  width: 100%;
  max-width: 800px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
  opacity: 0.9;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 20px 0;
}

.btn-detect {
  font-size: 17px;
  color: white;
  background-color: #6a9c46;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  padding: 18px 35px;
  transition: background-color 0.3s ease;
}

.btn-detect-cam {
  font-size: 17px;
  color: rgb(255, 255, 255);
  background-color: #b46a14;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  padding: 15px 30px;
  transition: background-color 0.3s ease;
}

.btn-detect-cap {
  font-size: 17px;
  color: rgb(255, 255, 255);
  background-color: #6a9c46;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  padding: 15px 30px;
  transition: background-color 0.3s ease;
  margin-top: 5px;
}

.video-container {
  display: flex;
  flex-direction: column;
  /* จัดเรียงแนวตั้ง */
  justify-content: center;
  align-items: center;
  /* จัดให้อยู่กึ่งกลางในแนวนอน */
  margin-bottom: 10px;
}

.btn-back {
  font-size: 17px;
  color: white;
  background-color: #000000;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  padding: 15px 30px;
  margin-top: 0
}

.btn-detect:hover {
  background-color: #5a8c36;
}

.btn-detect-cap:hover {
  background-color: #5a8c36;
}

.btn-detect-cam:hover {
  background-color: #d37d1b;
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
  margin-bottom: 0;
  text-align: center;
}

.detected-classes ul {
  list-style-type: none;
  padding: 0;
  display: inline-block;
  /* แก้จาก flex เป็น inline-block */
  text-align: center;
}

.detected-classes li {
  font-size: 16px;
  color: #333;
  margin-bottom: 10px;
}

h5 {
  text-align: center;
  width: 100%;
  /* เปลี่ยนจาก 28% เป็น 100% เพื่อให้ครอบคลุมทั้งความกว้าง */
  padding: 5px 0px;
  color: rgb(201, 5, 5);
  background-color: rgb(255, 245, 225);
  margin-top: 10px;
  /* เพิ่มระยะห่างด้านบน */
  border-radius: 10px;
}

.no-detections {
  margin-top: 15px;
  color: rgb(136, 3, 3);
  font-size: 16px;
}

@media (max-width: 600px) {
  .detection {
    padding: 10px;
    max-width: 90%;
  }

  .btn-detect,
  .btn-back {
    font-size: 14px;
    padding: 10px 20px;
  }

  img {
    width: 100%;
    max-width: 100%;
  }
}
</style>