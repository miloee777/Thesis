<template>
  <div class="content-container">
    <nav class="navbar">
      <router-link to="/" class="home-button">HOME</router-link>
    </nav>

    <h1 class="title">หญ้าข้าวนก</h1>

    <div class="info-container">
      <p class="scientific-name"><strong>ชื่อวิทยาศาสตร์</strong> Leptochloa chinensis Nees.</p>
      <p><strong>ชื่ออื่นๆ:</strong> หญ้าไม้วาด, หญ้าเล็ก</p>
      <p><strong>เป็นวัชพืชประเภท:</strong> หญ้า</p>
      <p><strong>อายุ:</strong> เพียงปีเดียว</p>
      <p class="characteristics"><strong>มีลักษณะทางชีววิทยา</strong></p>
      <p>ลำต้นตรงหรือโค้ง ความสูง 12-120 ซ.ม.</p>
      <p>ใบเรียบและปริกแหลมและเรียวยาว กาบใบเรียบ มีเยื่อกันน้ำฝนเป็นแผ่นบาง</p>
      <p>ออกดอกได้ตลอดปี ชอบขึ้นในสภาพดินแห้งถึงชื้น</p>
      <p>ไม่ชอบขึ้นในสภาพดินและไม่สามารถออกได้ในสภาพน้ำขัง แต่ไม่สามารถยืดตัวหนีน้ำได้</p>

      <div class="image-placeholder">
        <img src="@\assets\yakhaonokInfo.jpg" alt="">
      </div>
      <div class="image-placeholder">
        <img src="@\assets\yakhaonokInfo2.jpg" alt="">
      </div>
      
      
      <div v-if="showMoreInfo" class="more-info">
        <p class="HowtoEliminate"><strong> การป้องกันและการกำจัด</strong></p>
        <p> 1) ล่อให้งอกโดยการไขน้ำเข้านาแล้วขังไว้ 3 - 7 วัน ระบายน้ำออกทิ้งไว้ในสภาพดินชื้น 1-2 สัปดาห์ จะงอกขึ้นมาจำนวนมาก</p>
        <p> 2) เมื่อหญ้าข้าวนกงอกขึ้นมาเป็นจำนวนมากแล้วจึงไถกลบทำลาย
          และเตรียมดิน</p>
        <p> 3) หากมีการเตรียมดินดีเรียบสม่ำเสมอ จะสามารถเอาน้ำเข้านาได้หลังหว่านข้าวงอกแล้ว 7 วัน โดยขังน้ำลึกกว่า 2 เซนติเมตรจะควบคุมไม่ให้หญ้าข้าวนกงอกขึ้นมาได้ แต่ที่งอกมาก่อนหน้าการขังน้ำก็ยังสามารถเจริญเติบโตได้</p>
        <p class="HowtoEliminate2"><strong>แบบสารกำจัดวัชพืชมี 2 ประเภท</strong></p>
        <p>ประเภทก่อนวัชพืชงอก เช่น  เพรททิลาคลอร์, บิวทาคลอร์
         ประเภทหลังวัชพืชงอก เช่น ควินคลอแรก, ไซฮาโลฟอบ-บิวทิล, บีสไพริแบก-โซเดียม,
         ฟีนอกซาพรอป-พี-เอทิล, โพรพานิล</p>
      </div>
    </div>

    <div class="button-container">
      <button @click="goBack" class="btn-back">กลับ</button>
      <button class="btn-action" @click="toggleMoreInfo">กำจัด</button>
    </div>
  </div>
</template>


<script>
export default {
  name: 'YakhaonokInfo',
  data() {
    return {
      showMoreInfo: false, // สถานะสำหรับแสดง/ซ่อนเนื้อหาเพิ่มเติม
    };
  },
  methods: {  
    goBack() {
      this.$router.go(-1);
    },
    mounted() {
    window.scrollTo(0, 0);
  },
  toggleMoreInfo() {
      this.showMoreInfo = !this.showMoreInfo; // เมื่อคลิกปุ่มกำจัดจะแสดง/ซ่อนเนื้อหาเพิ่มเติม
    },
  }
}
</script>

<style scoped>
.content-container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
  background-color: #f5f5f5;
  border-radius: 10px;
  display: block;
  vertical-align: top;
}

.navbar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 20px;
}

.home-button {
  background-color: #6a9c46;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: bold;
}

.title {
  font-size: 1.5em;
  color: #333;
  margin-top: 0.1em;
}

.info-container {
  background-color: #ebebeb;
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
}

.scientific-name {
  color: #388e3c;
}

.characteristics {
  color: #388e3c;
}

.image-placeholder {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 350px;
  
  margin-top: 20px;
  border-radius: 10px;
}

.image-placeholder img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; 
  border-radius: 10px;
}

.more-info {
  margin-top: 20px;
  background-color: #ebd2b5;
  padding: 15px;
  border-radius: 10px;
}

.button-container {
  display: flex;
  justify-content: space-between;
}

.btn-back {
  background-color: #6a9c46;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-action {
  background-color: #f44336;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-back:hover {
  background-color: #7cb342;
}

.btn-action:hover {
  background-color: #e53935;
}

.HowtoEliminate{
  background-color: #B2967D;
  border-radius: 10px;
  padding: 10px;
  width: 50%;
  margin-top: 0%;
  margin-bottom: 0;
  text-align: center;
  font-size: 20px;
  color: rgb(255, 255, 255);
}
.HowtoEliminate2{
  background-color: #B2967D;
  border-radius: 10px;
  padding: 10px;
  width: 60%;
  margin-top: 0%;
  margin-bottom: 0;
  text-align: center;
  font-size: 20px;
  color: rgb(255, 255, 255);
}
@media (max-width: 768px) {
  .content-container {
    padding: 15px;
    max-width: 100%;
  }

  .title {
    font-size: 1.2em;
    text-align: center;
  }

  .navbar {
    justify-content: center;
  }

  .home-button {
    padding: 8px 16px;
    font-size: 14px;
  }

  .image-placeholder {
    height: 200px;
  }

  .more-info {
    font-size: 14px;
  }

  .HowtoEliminate, .HowtoEliminate2 {
    width: 100%;
    padding: 8px;
    font-size: 16px;
  }

  .button-container {
    flex-direction: column;
    align-items: center;
  }

  .btn-back, .btn-action {
    width: 100%;
    margin-bottom: 10px;
  }
}
</style>

