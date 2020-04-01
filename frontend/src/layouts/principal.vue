<template>
  <div>
    <Navbar></Navbar>
    <router-view></router-view>
    <article style="margin:0px !important">
      <slot/>
    </article>
    <Footer/>
  </div>
</template>

<script>
import Navbar from "../components/common/Navbar";
import Footer from "../components/common/footer";
export default {
  components: {
    Navbar, Footer
  }
};
</script>

<style scoped>
  .art {
    max-height: 100px;
  }
</style>