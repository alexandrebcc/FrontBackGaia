import Router from "vue-router";
import Home from '../views/home';
import Login from "../views/login";
import Cadastrar from "../views/cadastrar";
import FazerDoacao from "../views/fazerdoacao";
import Instituicoes from "../views/instituicoes";
import Apresentacao from "../views/apresentacao";
import Contato from "../views/contato";



export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/login",
      name: "Login",
      component: Login
    },
    {
      path: "/cadastrar",
      name: "Cadastrar",
      component: Cadastrar
    },
    {
      path: "/fazerdoacao",
      name: "FazerDoacao",
      component: FazerDoacao
    },
    {
      path: "/instituicoes",
      name: "Instituicoes",
      component: Instituicoes
    },
    {
      path: "/apresentacao",
      name: "Apresentacao",
      component: Apresentacao
    },
    {
      path: "/contato",
      name: "Contato",
      component: Contato
    }
    ]
});
