import {HttpService} from "./HttpService";

class LoginService extends HttpService {
    constructor() {
        super("Login")
    }
}

export const login = new LoginService()