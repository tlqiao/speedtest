export interface ApiInfo {
        language: string;
        testTool: string;
        serverName: string;
        apiUrl: string;
        method: string;
}

export let apiInfo: ApiInfo = {
        language: '',
        testTool: '',
        serverName: '',
        apiUrl: '',
        method: ''
};

export function updateApiInfo(newApiInfo: ApiInfo) {
        apiInfo = newApiInfo;
}
