import {HttpService} from "./HttpService";

class RegisterService extends HttpService {
    constructor(){
        super("Cadastrar")
    }
}

export const register = new RegisterService()