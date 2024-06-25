import { WebviewViewProvider, WebviewView, Webview, Uri } from "vscode";
import * as vscode from 'vscode';
import { MESSAGE } from '../constant'
import * as path from 'path';
import { saveContentToFile } from '../commands/apiTest';
import { ApiInfo, updateApiInfo } from './apiInfo';


declare const __non_webpack_require__: any;


export class SpeedTestSidebarProvider implements WebviewViewProvider {
        constructor(
                private readonly context: vscode.ExtensionContext,
                private readonly extensionPath: Uri,
                private _view: any = null
        ) { }
        resolveWebviewView(webviewView: WebviewView) {
                webviewView.webview.options = {
                        enableScripts: true,
                        localResourceRoots: [this.extensionPath],
                };
                webviewView.webview.html = this.getHtmlForWebview(webviewView.webview);
                this._view = webviewView;
                this.activateMessageListener();
        }

        private activateMessageListener() {
                this._view.webview.onDidReceiveMessage(async (message: any) => {
                        if (message.command === MESSAGE.saveToFile) {
                                await saveContentToFile(message.content);
                        }
                        if (message.command === MESSAGE.apiInfoChange) {
                                const newApiInfo: ApiInfo = JSON.parse(message.content);
                                updateApiInfo(newApiInfo)
                        }
                });
        }

        private getHtmlForWebview(webview: Webview): string {
                const manifest = __non_webpack_require__(
                        path.join(this.context.extensionPath, 'build', 'asset-manifest.json')
                );
                const mainScript = manifest['files']['main.js'];
                const mainStyle = manifest['files']['main.css'];
                const scriptUri = webview.asWebviewUri(Uri.joinPath(this.extensionPath, 'build', mainScript));
                const styleUri = webview.asWebviewUri(Uri.joinPath(this.extensionPath, 'build', mainStyle));

                return `<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="initial-scale=1, width=device-width" />
                <meta name="theme-color" content="#000000">
                <link rel="stylesheet" type="text/css" href="${styleUri}">
                <base href="${Uri.joinPath(this.extensionPath, 'build').with({ scheme: 'vscode-resource' })}/">
            </head>
            <body>
                <noscript>You need to enable JavaScript to run this app.</noscript>
                <div id="root"></div>
                <script>
                    const vscode = acquireVsCodeApi();
                </script>
                <script src="${scriptUri}"></script>
            </body>
            </html>`;
        }
}