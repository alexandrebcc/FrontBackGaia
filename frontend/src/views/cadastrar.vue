<template>
  <Principal>
  
  <div class="cadastro"> 
    <h1 id="titulo"> Cadastro </h1>
  </div>
  <form class="needs-validation" novalidate>
  <div class="form-row">
    <div class="col-md-4 mb-3">
      <label for="validationCustom01">Primeiro nome</label>
      <input type="text" class="form-control" id="validationCustom01" placeholder="Nome" value="Mark" required v-model="instituicao.nome">
      <div class="valid-feedback">
        Tudo certo!
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <label for="validationCustom02">Sobrenome</label>
      <input type="text" class="form-control" id="validationCustom02" placeholder="Sobrenome" value="Otto" required v-model="instituicao.sobrenome">
      <div class="valid-feedback">
        Tudo certo!
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <label for="validationCustomUsername">Usuário</label>
      <div class="input-group">
        <div class="input-group-prepend">
          <span class="input-group-text" id="inputGroupPrepend">@</span>
        </div>
        <input type="text" class="form-control" id="validationCustomUsername" placeholder="Usuário" aria-describedby="inputGroupPrepend" required v-model="instituicao.usuario">
        <div class="invalid-feedback">
          Por favor, escolha um nome de usuário.
        </div>
      </div>
    </div>
  </div>
  <div class="form-row">
    <div class="col-md-6 mb-3">
      <label for="validationCustom03">Cidade</label>
      <input type="text" class="form-control" id="validationCustom03" placeholder="Cidade" required v-model="instituicao.cidade">
      <div class="invalid-feedback">
        Por favor, informe uma cidade válida.
      </div>
    </div>
    <div class="col-md-3 mb-3">
      <label for="validationCustom04">Estado</label>
      <input type="text" class="form-control" id="validationCustom04" placeholder="Estado" required v-model="instituicao.estado">
      <div class="invalid-feedback">
        Por favor, informe um estado válido.
      </div>
    </div>
    <div class="col-md-3 mb-3">
      <label for="validationCustom05">CEP</label>
      <input type="text" class="form-control" id="validationCustom05" placeholder="CEP" required v-model="instituicao.cep">
      <div class="invalid-feedback">
        Por favor, informe um CEP válido.
      </div>
    </div>
  </div>
   <div class="form-row">
    <div class="form-group col-md-6">
      <label for="inputEmail4">Email</label>
      <input type="email"
             class="form-control" 
             id="inputEmail4"
             placeholder="Email" 
             v-model="email">
    </div>
    <div class="form-group col-md-6">
      <label for="inputPassword4">Senha</label>
      <input type="password" 
             class="form-control" 
             id="inputPassword4" 
             placeholder="Senha" 
             v-model="senha">
    </div>
  </div>
  <div class="form-group">
    <label for="inputAddress">Endereço</label>
    <input type="text" class="form-control" id="inputAddress" placeholder="Rua dos Bobos, nº 0" v-model="instituicao.endereco">
  </div>
  <div class="form-group">
    <label for="inputAddress2">Endereço 2</label>
    <input type="text" class="form-control" id="inputAddress2" placeholder="Apartamento, hotel, casa, etc." v-model="instituicao.endereco2">
  </div>
  <div class="form-row">
    <div class="form-group col-md-6">
      <label for="inputCity">Cidade</label>
      <input type="text" class="form-control" id="inputCity" v-model="instituicao.cidade">
    </div>
    <div class="form-group col-md-4">
      <label for="inputEstado">Estado</label>
      <select id="inputEstado" class="form-control" >
        <option selected>Escolher...</option>
        <option>...</option>
      </select>
    </div>
    <div class="form-group col-md-2">
      <label for="inputCEP">CEP</label>
      <input type="text" class="form-control" id="inputCEP" v-model="instituicao.ceep">
    </div>
  </div>
  
  <div class="form-group">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required v-model="instituicao.validade">
      <label class="form-check-label" for="invalidCheck">
        Concordo com os termos e condições
      </label>
      <div class="invalid-feedback">
        Você deve concordar, antes de continuar.
      </div>
        <button @click="SingUp" type="submit">Enviar</button>
      <span>ou retorne ao  
        <router-link to="/login" login>login.</router-link>
        </span>
    </div>
  </div>
</form>
  </Principal>
</template>

<script>
/* eslint-disable */ 
import Principal from "../layouts/principal"
import firebase from "firebase"

export default {
  name: 'app',
  components: { 
    Principal
  },
  data(){
    return{
      instituicao:{
        nome:"",
        sobrenome:"",
        usuario:"",
        cidade:"",
        estado:"",
        cep:"",
        endereco:"",
        endereco2:"",
        cidade:"",
        ceep:"",
        validade:""
      },
      email: " ",
      senha: " ",
    }
  },
  methods: {
    
    SingUp() {
      firebase.auth().createUserWithEmailAndPassword(this.email,this.senha).then(
        (user) => {
          this.$router.replace('/')
        },
        (err) => {
          alert('Aconteceu algo inesperado.' + err.message)
        }
      );
    },
    async obterCadastro(){
      this.register = await this.$services.register.getAll();
      console.log(this.register);
    },    
    async postRegistro(){
      console.log(this.instituicao);
      let response = await this.$services.register.post(this.instituicao);
      console.log(response);
    },
    async putRegistro(){
      let refresh = {
        nome: "atualiza usuario",
        idade: 20,
        email:"atualiza@gmail.com"
        
      }
      let response = await this.$services.register.put(4,refresh)
    },
    async delRegistro(){
     let response = await this.$services.register.delete(4)
    }
    
  },
   created() {
  },
    mounted(){
      /*this.obterCadastro();*/
      //this.postRegistro();
      //this.obterCadastro();
      //this.putRegistro();
      //this.obterCadastro();
      //this.delRegistro();
      
    },
    updated() {

  }

 
};

</script>

<style>
  .cadastro{
    background-color:darkgreen;
  }
  #titulo{
    color:cornsilk;
    display: inline-flex;
  }
  
</style>
