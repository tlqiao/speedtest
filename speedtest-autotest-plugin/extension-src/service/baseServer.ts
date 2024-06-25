import axios from 'axios';
import { CONFIGS } from '../config/configs'

interface TestCode {
        code: string
};

interface ApiDetails {
        apiReq: {
                [key: string]: any;
        };
        apiRes: {
                [key: string]: any;
        };
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
        async genWebUITestCode(testTool: string, locators: string, scenarios: string): Promise<TestCode> {
                let url = CONFIGS.url.backendBase + CONFIGS.url.genWebUIStepFunctionCode;
                let reqBody = {
                        test_tool: testTool,
                        locators: locators,
                        scenarios: scenarios
                };
                let res = await this.callApi(url, "POST", reqBody);
                return res.data;
        }

        async genMobileUITestCode(testTool: string, locators: string, scenarios: string): Promise<TestCode> {
                let url = CONFIGS.url.backendBase + CONFIGS.url.genMobileStepFunctionCode;
                let reqBody = {
                        test_tool: testTool,
                        locators: locators,
                        scenarios: scenarios
                };
                let res = await this.callApi(url, "POST", reqBody);
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
