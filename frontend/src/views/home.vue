<template>
  <Principal id=home>
  <div class="estilo" style="min-height:510px; margin-bottom:0px !important" id="ola"></div>
   <!-- <img src="../assets/imgs/FundoGaia2.png"  alt="fundo" height="510px" width="1500px"> --> 
  </Principal>
</template>

<script>
import Principal from "../layouts/principal"

export default {
  name: 'app',
  components: { 
    Principal
  }
}
</script>

<style scoped>

.estilo{
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-image: url(../assets/imgs/FundoGaia2.png);
}

 #home {
    background: none;
    background-size: 50%;
    background-position: 50% 50%;
    background-repeat: no-repeat;
}   

.texto{
  margin-top: 50px;
  margin-left: 100px;
  color: white;
  font-size: 100px
}

img.img-banner {
 position: fixed;
 height: 100%;
 width: 100%;
}

  
</style>
