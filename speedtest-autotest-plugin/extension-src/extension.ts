import * as vscode from 'vscode';
import { genUITest, writeUITestCode } from './commands/uiTest';
import { genApiTest, writeApiTestCode } from './commands/apiTest';
import { COMMAND } from './constant'
import { SpeedTestSidebarProvider } from './providers/speedTestProvider';
import { apiInfo } from './providers/apiInfo';



declare const __non_webpack_require__: any
export function activate(context: vscode.ExtensionContext) {
    context.subscriptions.push(
        vscode.window.registerWebviewViewProvider('speedTestSidebar', new SpeedTestSidebarProvider(context, context?.extensionUri, {}))
    );

    context.subscriptions.push(
        vscode.commands.registerCommand(COMMAND.uitest, async () => {
            const editor = vscode.window.activeTextEditor;
            if (editor) {
                const result = await genUITest(editor);
                await writeUITestCode(result, editor);
            }
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand(COMMAND.apitest, async () => {
            const editor = vscode.window.activeTextEditor;
            if (editor) {
                const result = await genApiTest(editor, apiInfo.language, apiInfo.testTool, apiInfo.serverName, apiInfo.apiUrl, apiInfo.method);
                await writeApiTestCode(result, editor);
            }
        })
    );
}

export function deactivate() { }
