<template>
  <Principal>
<body>
  <div class="py-5 text-center cover d-flex flex-column bg-dark">
    <div class="container my-auto">
      <div class="row">
        <div class="mx-auto col-lg-6 col-md-8">
          <h1 class="display-1 mb-0 mt-5 big-title">NOME DA INSTITUICAO</h1>
          <h3 class="mb-4"><b>A hell of a team at your disposal</b></h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.&nbsp;</p>
        </div>
      </div>
    </div>
    
    <div class="container mt-auto">
      <div class="row">
        <div class="mx-auto col-lg-6 col-md-8 col-10">
          <a href="#mission"><i class="d-block fa fa-angle-down fa-2x"></i></a>
        </div>
      </div>
    </div>
  </div>
  <div class="py-5 filter-dark cover bg-fixed" style="background-image: url('assets/team/planes.jpg');background-position:center bottom;background-size:cover;" id="mission">
    <div class="container my-auto">
      <div class="row">
        <div class="col-md-8 p-3 text-white">
          <h2 class="mb-4">Our Smission</h2>
          <p class="lead"><i>Lorem ipsum dolor sit amet,&nbsp;<br>consectetur adipisici elit,&nbsp;<br>sed eiusmod tempor incidunt&nbsp;<br>ut labore et dolore magna aliqua.</i></p>
        </div>
      </div>
    </div>
  </div>
  
</body>
  </Principal>
</template>

<script>
/* eslint-disable */ 
import Principal from "../layouts/principal";

export default {
  name: "app",
  components: {
    Principal
  },
  data() {
    return {
      logo:require('../assets/logo.png'),
      institutions: []
    }
  },

  methods: {

  created() {
    
    this.obterInstituicoes();
  },
  mounted() {
    this.obterInstituicoes();
    /*this.postIstituicoes();*/
    /*this.putInstituicoes();
    this.delInstituicoes();*/
  },
  updated() {
  }}
};
</script>

