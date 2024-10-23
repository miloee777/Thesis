<template>
  
  <div class="content-container">
    <div class="homepage">
      <header class="header">
        <!-- Hamburger Menu Button -->
        <button class="hamburger" @click="toggleMenu">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </button>
  
        <!-- Navigation Menu -->
        <nav :class="{ 'nav': true, 'nav-open': isMenuOpen }">
          <ul>
            <li><router-link to="/" exact-active-class="active-link">หน้าแรก</router-link></li>
            <li><router-link to="/about">เกี่ยวกับเรา</router-link></li>
            <li><router-link to="/contact">ติดต่อเรา</router-link></li>
            <li><router-link to="/product">ข้อเสนอแนะ</router-link></li>
          </ul>
        </nav>
      </header>
      <div class="text-container">
        <h1>ระบบตรวจจับวัชพืชในนาข้าว</h1>
        <h2>Weeds Detection in rice field</h2>
        <p>
          การพัฒนาระบบตรวจจับวัชพืชในนาข้าวขึ้นมาเพื่อลดปัญหาในการแก้ไขปัญหา
          ให้กับชาวเกษตรกรที่ปลูกข้าว ที่ต้องพบปัญหาวัชพืชและวิธีกำจัดที่มากมาย
        </p>
        <button @click="goToDetection">เริ่มต้นตรวจจับ <i class="bi bi-search"></i></button>
        <div class="Topic">
          <p>เกี่ยวกับหญ้า <i class="bi bi-arrow-down-circle"></i> </p>
        </div>
        <div class="card-wrapper">
          <div class="card-container">
            <div class="card">
              <img src="@\assets\kaonokcard.jpg" alt="" style="width:100%">
              <div class="container">
                <h5><b>หญ้าข้าวนก</b></h5>
                <h5><router-link :to="'/ya-khao-nok-info'"><b>อ่านเพิ่มเติม</b></router-link></h5>
              </div>
            </div>
            <div class="card">
              <img src="@\assets\yakoksaiInfo.jpg" alt="" style="width:100%">
              <div class="container">
                <h5><b>หญ้ากกทราย</b></h5>
                <h5><router-link :to="'/ya-kok-sai-info'"><b>อ่านเพิ่มเติม</b></router-link></h5>
              </div>
            </div>
            <div class="card">
              <img src="@\assets\nuadpladukcard.jpg" alt="" style="width:100%">
              <div class="container">
                <h5><b>หญ้าหนวดปลาดุก</b></h5>
                <h5><router-link :to="'Nuad-PlaDuk-Info'"><b>อ่านเพิ่มเติม</b></router-link></h5>
              </div>
            </div>
            <div class="card">
              <img src="@\assets\phakpodnacard.jpg" alt="" style="width:100%">
              <div class="container">
                <h5><b>ผักปอดนา</b></h5>
                <h5><router-link :to="'/phak-pod-na-info'"><b>อ่านเพิ่มเติม</b></router-link></h5>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="image-container">
        <img src="@/assets/bg1.png" alt="Rice field">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      hasScrolled: false,
      isMenuOpen: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    goToDetection() {
      this.$router.push({ name: 'Detection' });

      // ลบข้อมูลที่เก็บไว้ใน localStorage เมื่อกลับไปหน้า Detection
      localStorage.removeItem('detectedImage');
      localStorage.removeItem('predictions');
      localStorage.removeItem('imageWidth');
      localStorage.removeItem('imageHeight');
    },
    handleScroll() {
      if (!this.hasScrolled && window.scrollY > 10) { // 10px scroll threshold
        this.hasScrolled = true;
        const cardWrapper = document.querySelector('.card-wrapper');
        if (cardWrapper) {
          cardWrapper.classList.add('visible');
        }
      }
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>

.header {
  z-index: 2; /* ปรับให้ header อยู่เหนือทุกสิ่ง */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #f8f8f8;
  width: 30%;
  position: fixed; /* แปะ header ติดกับขอบบน */
  top: 0; /* แปะที่ขอบบนสุด */
  left: 10;
}

.nav {
  display: flex;
}

.nav ul {
  list-style-type: none;
  display: flex;
  gap: 30px;
  margin: 0;
  padding: 0;
}

.nav ul li {
  font-size: 1em;
}

.nav ul li a {
  text-decoration: none;
  color: #666;
}

.nav ul li a.active-link {
  color: #6a9c46;
  font-weight: bold;
  font: 1em sans-serif;
}

/* Hamburger Menu Button */
.hamburger {
  position: absolute;
  top: 10px;
  left: 10px;
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 25px;
  background: transparent;
  border: none;
  cursor: pointer;
  z-index: 20;
}

.hamburger .bar {
  height: 3px;
  width: 100%;
  background-color: #333;
  border-radius: 10px;
}

.content-container {
  background-color: #f8f8f8;
  display: flex;
  flex-direction: column;
  width: 100vw;
  min-height: 100vh;
}
/* Styles for the main content */
.homepage {
  z-index: 2;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100vw;
  height: 120vh;
  background-color: #f8f8f8;
}

.text-container {
  flex: 1;
  padding: 20px;
  display: flex;
  margin-top: 17%;
  flex-direction: column;
  justify-content: center;
  background-color: #f8f8f8;
  z-index:1 ;
  text-align: right;
  
}

h1 {
  font-size: 2.5em;
  color: #333;
  margin-bottom: 0;
}

h2 {
  font-size: 1.5em;
  color: #6a9c46;
  margin-top: 0.1em;
}

h5 {
  color: #2a4913;
  text-align: center;
}

h5 a {
  display: inline-block;
  padding: 5px 15px;
  background-color: #6a9c46; /* สีเขียว */
  color: white;
  border-radius: 10px;
  text-decoration: none; /* เอาขีดเส้นใต้ของลิงก์ออก */
  font-size: 16px;
  transition: background-color 0.3s ease;
}

h5 a:hover {
  background-color: #5a8c36; /* สีเมื่อ hover */
}

p {
  font-size: 1.5em;
  line-height: 1.5;
  color: #666;
  text-align: left;
  margin-top: 2;
}

button {
  width: 23%;
  padding: 2%;
  font-size: 20px;
  color: white;
  background-color: #6a9c46;
  border: none;
  border-radius: 30px 30px 5px 30px;
  cursor: pointer;
}

button:hover {
  background-color: #5a8c36;
}

.Topic p {
  background-color: #B2967D;
  border-radius: 10px;
  padding: 10px;
  width: 22%;
  margin-top: 5%;
  margin-bottom: 0;
  text-align: center;
  font-size: 20px;
  color: rgb(245, 245, 245);
}

.image-container {
  flex: 1;
  display: flex;
  align-items: flex-start; /* จัดให้รูปภาพชิดกับขอบด้านบน */
  margin-left: 18px;
  z-index: 1;
  padding-top: 0; /* ลบ padding ด้านบนถ้ามี */
  height: 100vh; /* ปรับให้รูปภาพมีความสูงเต็มจอ */
  margin-top: 0; /* ลบ margin ด้านบน */
}

.image-container img {
  width: 100%;
  height: 120vh; /* ปรับให้รูปภาพมีความสูงเต็มจอ */
  object-fit: cover; /* ให้รูปภาพขยายตาม container */
  border-radius: 10px;
  margin: 0; /* ลบ margin ของรูปภาพ */
}

.card-container {
  display: flex;
  gap: 45px;
  margin-top: 10px;
  flex-wrap: wrap;
  justify-content: center; /* จัดให้การ์ดอยู่ตรงกลาง */
  align-items: center; /* จัดให้การ์ดอยู่ตรงกลาง */
}

.card {
  background-color: #f8f8f8;
  margin-top: 3%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  width: 20%;
  border-radius: 10px;
}

.card img {
  width: 100%;
  height: 60%;
  border-radius: 10px;
}

.card-wrapper {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.card-wrapper.visible {
  opacity: 1;
}

/* Responsive Styles for Mobile */
@media only screen and (max-width: 768px) {
  .header {
    width: 100%;
    padding: 10px 20px;
  }

  .nav ul {
    flex-direction: column;
    align-items: center;
  }

  .nav ul li {
    font-size: 1.2em;
    margin-bottom: 10px;
  }

  .homepage {
    height: auto;
    padding: 10px;
    flex-direction: column;
  }

  .text-container {
    text-align: center;
    padding: 10px;
  }

  button {
    width: 80%;
    margin: 10px auto;
  }

  .Topic p {
    width: 80%;
    margin: 20px auto;
  }

  .card-container {
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }

  .card {
    width: 80%;
    margin-top: 10px;
  }

  .image-container {
    display: none;
  }

  .nav {
    position: absolute;
    top: 50px;
    left: 10px;
    flex-direction: column;
    align-items: flex-start;
    background-color: #f8f8f8;
    width: 200px;
    height: 0;
    overflow: hidden;
    transition: height 0.3s ease-in-out;
    z-index: 10;
  }

  .nav-open {
    height: auto;
    padding: 15px 0 0 15px;
    background-color: rgba(204, 223, 196, 0.6);
    border-radius: 20px;
  }

  .hamburger {
    display: flex;
  }
}
</style>
