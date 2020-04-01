<template>
  <NavBar>
   <div class="login-container">
     <br>
    <br>
        <div class="d-flex justify-content-center h-100">
            <div class="card">
                <div class="card-header">
                    <h3>Login</h3>
                </div>
                <div class="card-body">
                    <form>
                        <div class="input-group form-group">
                            <div class="input-group-prepend">
                                <span class="fa fa-userr" aria-hidden="true"><i></i></span>
                            </div>
                            <input type="text" 
                                   placeholder="Seu Nome"
                                   v-model="email">

                        </div>
                        <div class="input-group form-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"><i class="fas fa-key"></i></span>
                            </div>
                            <input type="password" 
                                   placeholder="Sua Senha"
                                   v-model="senha">
                        </div>
                        <div class="row align-items-center remember">
                            <input type="checkbox">Lembrar Senha?
                        </div>
                        <div class="btn-login">
                            <button @click="login">Login</button>
                        </div>
                    </form>
                </div>
                <div class="card-footer">
                    <div class="d-flex justify-content-center links">
                        Não tem uma Conta?<router-link :to="{name:'Cadastrar'}">Cadastre-se</router-link>
                    </div>
                    <div class="d-flex justify-content-center">
                        <router-link :to="{name:'Cadastrar'}">Esqueceu Sua Senha</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </NavBar>
</template>

<script>
/* eslint-disable */ 
import NavBar from "../layouts/principal";
import firebase from "firebase";
export default {
  name: 'app',
  components: { 
      NavBar
  },
  data(){
      return{
          email: " ",
          senha: " ",
        

      };
  },
  methods: {
      login: function(){
          firebase.auth().signInWithEmailAndPassword(this.email, this.senha).then(
          (user) => {
              this.$router.replace("/")
              alert(`Bem vindo , ${{email}}`)
          },
          (err) => {
              alert('Não foi possível realizar o login.' + err.message)
          }
          );
        }
      }/*,
       async obterLogin(){
     
     this.login = await this.$services.login.getAll();
      console.log(this.login);
    },
    async postLogin(){
      let login = {
        usuario: "lulamolusco",
        senha:3030
    }
      let response = await this.$services.login.post(login);
      console.log(response);
    },
    async putLogin(){
      let refresh = {
        usuario: "lulaMolusco",
        senha:3030
      }
      let response = await this.$services.login.put(4,refresh)
    },
    async delLogin(){
     let dados = this.getAll()
     let response = await this.$services.login.delete()
    }
  },
   created() {
    
  },
  mounted() {
    this.obterLogin();
    this.postLogin();
    this.obterLogin();
    this.putLogin();
    this.obterLogin();
    this.delLogin();
    this.obterLogin();
  },
  updated() {

  }*/
}
</script>

<style>

.login-container {
    background-color: black;
    background-repeat: no-repeat;
    height: 100%;
    font-family: 'Numans', sans-serif;
    height: 100%;
    align-content: center;
}

.card {
    height: 370px;
    margin-top: 100px;
    margin-bottom: 500px;
    width: 400px;
    background-color: rgba(0, 0, 0, 0.5) !important;
}

.social_icon span {
    font-size: 60px;
    margin-left: 10px;
    color: #FFC312;
}

.social_icon span:hover {
    color: white;
    cursor: pointer;
}

.card-header h3 {
    color: white;
}

.social_icon {
    position: absolute;
    right: 20px;
    top: -45px;
}

.input-group-prepend span {
    width: 50px;
    background-color: #FFC312;
    color: black;
    border: 0 !important;
}

input:focus {
    outline: 0 0 0 0 !important;
    box-shadow: 0 0 0 0 !important;
}

.remember {
    color: white;
}

.remember input {
    width: 20px;
    height: 20px;
    margin-left: 15px;
    margin-right: 5px;
}

.login_btn {
    color: black;
    background-color: #FFC312;
    width: 100px;
}

.login_btn:hover {
    color: black;
    background-color: white;
}

.links {
    color: white;
}

.links a {
    margin-left: 4px;
}
  
</style>

