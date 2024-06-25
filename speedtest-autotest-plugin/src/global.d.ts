interface Message {
        command: string;
        content: string;
        [key: string]: any;
}
type VSCode = {
        Uri: any;
        env: any;
        postMessage(message: Message): void;
        getState(): any;
        setState(state: any): void;
};

declare const vscode: VSCode;