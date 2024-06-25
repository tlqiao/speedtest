import axios from 'axios';
import { CONFIGS } from '../config/configs'

interface ApiDetails {
        apiReq: {
                [key: string]: any;
        };
        apiRes: {
                [key: string]: any;
        };
}

interface ApiUrlList {
        apiUrlList: string[];
}

interface ApiServerList {
        server_List: string[];
}

interface TestCode {
        code: string
}
export class ApiHelper {
        async callApi(url: string, method: string = 'GET', data?: any): Promise<any> {
                try {
                        let response;
                        if (method.toUpperCase() === 'GET') {
                                if (data !== null) {
                                        response = await axios.get(url, { params: data })
                                } else
                                        response = await axios.get(url);
                        } else if (method.toUpperCase() === 'POST') {
                                response = await axios.post(url, data);
                        } else {
                                throw new Error("Unsupported HTTP method. Only 'GET' and 'POST' methods are supported.");
                        }
                        return response;
                } catch (error) {
                        console.error("Call API Error", error);
                        return null;
                }
        }

        async getServerList(): Promise<ApiServerList> {
                try {
                        let apiUrl = CONFIGS.url.backendBase + CONFIGS.url.getServerList;
                        let res = await this.callApi(apiUrl, "GET");
                        return res.data;
                } catch (error) {
                        console.error("Error fetching server list:", error);
                        throw error;
                }
        }

        async getApiUrlList(serverName: string): Promise<ApiUrlList> {
                let apiUrl = CONFIGS.url.backendBase + CONFIGS.url.getApiUrlList;
                let res = await this.callApi(apiUrl, "GET", { "server_name": serverName });
                return res.data;
        }

        async getApiReqRes(serverName: string, apiUrl: string, method: string): Promise<ApiDetails> {
                let url = CONFIGS.url.backendBase + CONFIGS.url.getApiReqRes;
                let data = {
                        "server_name": serverName,
                        "api_url": apiUrl,
                        "method": method
                }
                let res = await this.callApi(url, "GET", data);
                return res.data;
        }

        async genApiTestCode(language: string, testTool: string, serverName: string, apiUrl: string, method: string, test_context: any): Promise<TestCode> {
                let url = CONFIGS.url.backendBase + CONFIGS.url.genApiTestCode;
                let reqBody = (await this.getApiReqRes(serverName, apiUrl, method)).apiReq
                let data = {
                        "language": language,
                        "test_tool": testTool,
                        "api_header": { "Content-Type": "application/json" },
                        "request": reqBody,
                        "test_context": test_context
                };
                let res = await this.callApi(url, "POST", data);
                return res.data;
        }
}
