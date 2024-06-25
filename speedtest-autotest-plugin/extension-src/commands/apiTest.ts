import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { ApiHelper } from '../service/baseServer'
import { parseCode } from './utils'

let apiHelper = new ApiHelper();
export async function saveContentToFile(content: string) {
        const folderPath = vscode.workspace.workspaceFolders![0].uri.fsPath;
        const baseFileName = 'apiTest';
        let fileName = baseFileName + '.js';
        let filePath = path.join(folderPath, fileName);
        let counter = 1;
        while (fs.existsSync(filePath)) {
                fileName = `${baseFileName}${counter.toString().padStart(3, '0')}.js`;
                filePath = path.join(folderPath, fileName);
                counter++;
        }
        fs.writeFile(filePath, content, (err) => {
                if (err) {
                        vscode.window.showErrorMessage(`Error writing to file: ${err.message}`);
                } else {
                        vscode.window.showInformationMessage(`File created: ${filePath}`);
                }
        });
}

export async function genApiTest(activeEditor: vscode.TextEditor | undefined, language: string, testTool: string, serverName: string, apiUrl: string, method: string): Promise<string> {
        if (!activeEditor) {
                return "no active editor found";
        }
        const selection = activeEditor.selection;
        const selectedText = activeEditor.document.getText(selection);
        let res = await apiHelper.genApiTestCode(language, testTool, serverName, apiUrl, method, selectedText);
        let code = res ? parseCode(res.code) : "no code generated";
        return code;
}

export async function writeApiTestCode(code: string, activeEditor: vscode.TextEditor | undefined) {
        if (activeEditor) {
                const document = activeEditor.document;
                const edit = new vscode.WorkspaceEdit();
                const lastLine = document.lineAt(document.lineCount - 1);
                const end = new vscode.Position(document.lineCount - 1, lastLine.text.length);
                edit.insert(document.uri, end, code);

                await vscode.workspace.applyEdit(edit);
        } else {
                vscode.window.showErrorMessage('No active text editor found.');
        }
}
