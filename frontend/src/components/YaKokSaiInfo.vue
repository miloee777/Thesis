<template>
  <div class="content-container">
    <nav class="navbar">
      <router-link to="/" class="home-button">หน้าแรก</router-link>
    </nav>

    <h1 class="title">หญ้ากกทราย</h1>

    <div class="info-container">
      <p class="scientific-name"><strong>ชื่อวิทยาศาสตร์</strong> Cyperus iria L.</p>
      <p><strong>ชื่ออื่นๆ:</strong> หญ้าไม้วาด, หญ้าเล็ก</p>
      <p><strong>เป็นวัชพืชประเภท:</strong> กก</p>
      <p><strong>อายุ:</strong> เพียงปีเดียว</p>
      <p class="characteristics"><strong>มีลักษณะทางชีววิทยา</strong></p>
      <p>ลำต้นมีลักษณะเป็นสามเหลี่ยมไม่มีข้อปล้อง ใบไม่แยกเป็นก้านใบและแผ่นใบ  ก้านชูดอกสูง 20-60 ซ.ม.  ช่อดอกแตกแขนงจากจุด</p>
      <p>เดียวกัน 3-8 แขนง  ดอกย่อยอัดกันแน่นบนก้านช่อดอกย่อยเป็น 2 แถว  ประกอบด้วยดอกจำนวน 6-24 ดอก ออกดอกตลอดปีเมื่ออายุ  2-3 เดือน</p>
      <p>ขึ้นในที่แห้งและชื้น ชอบขึ้นในดินเหนียวปนทรายและชื้น ไม่งอกใต้น้ำในสภาพนาหว่านน้ำตมจะงอกหลังข้าว เมื่องอกแล้วเจริญได้ในที่น้ำขัง</p>
      <p></p>

      <div class="image-placeholder">
        <img src="@\assets\yakoksaiInfo1.jpg" alt="">
      </div>

      <div class="image-placeholder">
        <img src="@\assets\yakoksaiInfo.jpg" alt="">
      </div>

    <div v-if="showMoreInfo" class="more-info">
      <p class="HowtoEliminate"><strong> การป้องกันและการกำจัด</strong></p>
      <p> 1) ล่อให้งอกโดยการไขน้ำเข้านาแล้วขังไว้ 3 วัน  ระบายน้ำออกทิ้งไว้ในสภาพดินชื้น 1-2 สัปดาห์ กกทรายจะงอกขึ้นมาจำนวนมาก</p>
      <p> 2) เมื่อกกทรายงอกขึ้นมาเป็นจำนวนมากแล้วจึงไถกลบทำลาย และเตรียมดิน</p>
      <p> 3) หากมีการเตรียมดินดีเรียบสม่ำเสมอ  จะสามารถเอาน้ำเข้านาได้หลังหว่าน  ข้าวงอกแล้ว 7 วัน โดยขังน้ำลึกกว่า 2 เซนติเมตร จะควบคุมไม่ให้กกทรายงอกขึ้นมาได้ แต่ที่งอกมาก่อนหน้าการขังน้ำก็ยังสามารถเจริญเติบโตได้</p>
      <p class="HowtoEliminate2"><strong>แบบสารกำจัดวัชพืชมี 2 ประเภท</strong></p>
      <p>ประเภทก่อนวัชพืชงอก เช่น เพรททิลาคลอร์, บิวทาคลอร์, ออกซาไดอะซอน
       ประเภทหลังวัชพืชงอก เช่น เมทซัลฟูรอน-เมทธิล+คลอริมูรอน-เอทธิล, 2,4-D,
       บีสไพริแบก-โซเดียม, โพรพานิล</p>
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
  name: 'YakoksaiInfo',
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
