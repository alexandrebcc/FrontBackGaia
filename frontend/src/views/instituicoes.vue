<template>
  <Principal>
    <div>
      <div
        class="Wrapper_wrapper__28JZg BlockContentHtml_wrapper__3bo2x Wrapper_wrapper-default-width__2PRux"
        style="background-image: url(&quot;undefined&quot;);"
      >
        <div class="Wrapper_container__3c3aY Wrapper_container-default-width__2lKTA">
          <div class="HtmlMarkup_html__3sUPP">
            <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">-->
            <link href="#" rel="stylesheet" />
            <link href="#" rel="stylesheet" type="text/css" />
            <div id="page-custom">
              <div class="container max-center">
                <div class="row">
                  <div class="col-md-12">
                    <h1 class="title-line-center">INSTITUIÇÕES</h1>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-12">
                    <p
                      class="text-center"
                    >Estas são as Instituições que fazem parte do projeto Gaia.</p>
                  </div>
                </div>
              </div>

           
              <div class="container">

                <div class="row">

                  <div class="col-md-3 col-sm-6 text-center container-lines" v-for="institution in institutions" :key="institution.id">
                    <div class="container-lines">
                      <div class="img-line"></div>

                      <h2>
                        <a class="title-lines" v-bind:style="{ 'background-image': 'url(' + logo + ')' }">
                          <span class="lines">{{institution.nome}}</span>
                        </a>
                      </h2>
                    </div>
                  </div>                  
                </div>  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

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
    async obterInstituicoes(){
     
     let response = await this.$services.institutions.getAll();
     if(response){
       this.institutions = response.data;
     }
      console.log(this.institutions);
    },
    async postIstituicoes(){
      let instituicao = {
        name: "instituição 1",
        endereco: "rua x",
    }
      let response = await this.$services.institutions.post(instituicao);
      console.log(response);
    },
    async putInstituicoes(){
      let refresh = {
        name: "eu mesmo",
        endereco: "o melhor",
      }
      let response = await this.$services.institutions.put(1,refresh)
    },
    async delInstituicoes(){
     let response = await this.$services.institutions.delete(0)
    }
  },
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
  }
};
</script>

<style scopded>
#page-custom h2 {
  font-weight: 300;
}
#page-custom .container-lines,
#page-custom .img-line {
  position: relative;
  height: 27.5rem;
  margin-bottom: 30px;
}
#page-custom .container-lines:hover {
  top: -1px;
  transition: all 3s ease;
}

#page-custom .img-line {
  background-position-x: center;
  background-repeat: no-repeat;
  
}
#page-custom .title-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: rgba(0, 0, 0, 0.4);
  color: #fff;
  font-size: 1.375rem;
  text-transform: uppercase;
  font-weight: 600;
}
#page-custom .title-lines:hover {
  color: #fff;
}
#page-custom .lines {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

#page-custom h1 {
  font-size: 22px;
  text-transform: uppercase;
}
#page-custom h2 {
  font-size: 18px;
  text-transform: uppercase;
}

#page-custom p {
  padding-bottom: 30px;
}

#page-custom .title-line {
  margin: 0;
}
#page-custom .title-line:after {
  background-color: #f93;
  content: "";
  display: block;
  height: 0.125rem;
  margin: 10px 0 30px;
  width: 3.75rem;
}

#page-custom .title-line-center {
  margin: 0;
  text-align: center;
  margin: 60px 0 50px;
}
#page-custom .title-line-center:after {
  background-color: #f93;
  content: "";
  display: block;
  height: 0.125rem;
  margin: 10px auto 30px;
  width: 3.75rem;
}

/* Lists */
#page-custom ul {
  max-width: none;
  padding: 0 0 30px 0;
}

/* Lists */

/* Contents */
#page-custom .max-center {
  /*max-width: 840px;*/
  max-width: 48.75rem;
}

.btn-xyjz {
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  background-color: #f93;
  border: none;
  color: #fff !important;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  font-family: "Lato", sans-serif;
  font-size: 0.875rem;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  line-height: 1.25rem;
  max-width: 15rem;
  padding: 0.625rem 1.25rem;
  text-transform: uppercase;
  -webkit-transition: all 305ms ease;
  transition: all 305ms ease;
  white-space: nowrap;
}
.btn-xyjz:not(:disabled):hover {
  background-color: #ff7c34;
  color: #fff;
  text-decoration: none;
}

.center-xyjz {
  /* margin: 1.25rem auto 0; */
  margin: 3.25rem auto;
}
</style>
