import { HttpService } from "./HttpService"; 

class IntitutionService extends HttpService {
    constructor() {
        super("instituicoes")
    }
}

export const institutions = new IntitutionService()