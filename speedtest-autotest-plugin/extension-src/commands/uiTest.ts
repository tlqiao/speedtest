import * as vscode from 'vscode';
import { ApiHelper } from '../service/baseServer'
import { parseCode } from './utils'

let apiHelper = new ApiHelper();
async function readFileContent(activeEditor: vscode.TextEditor | undefined): Promise<string | undefined> {
        if (activeEditor) {
                const document = activeEditor.document;
                return document.getText();
        }
        return undefined;
}

async function extractLocatorCode(fileContent: string): Promise<string> {
        const locatorsRegex = /locators\s*=\s*{[^{}]*}/;
        const match = locatorsRegex.exec(fileContent);
        return match ? match[0] : '';
}

async function highlightLayoutCode(layoutCode: string, activeEditor: vscode.TextEditor | undefined) {
        if (activeEditor) {
                const startPos = activeEditor.document.positionAt(activeEditor.document.getText().indexOf(layoutCode));
                const endPos = activeEditor.document.positionAt(activeEditor.document.getText().indexOf(layoutCode) + layoutCode.length);
                const selection = new vscode.Selection(startPos, endPos);
                activeEditor.selection = selection;
                activeEditor.revealRange(selection);
                return { startPos, endPos }
        }
        return {}
}
async function processFileContentAndHighlight(activeEditor: vscode.TextEditor | undefined) {
        const fileContent = await readFileContent(activeEditor);
        if (fileContent) {
                const layoutCode = await extractLocatorCode(fileContent);
                if (layoutCode) {
                        await highlightLayoutCode(layoutCode, activeEditor);
                        return layoutCode;
                } else {
                        vscode.window.showErrorMessage('Layout code not found in the currently opened file.');
                }
        } else {
                vscode.window.showErrorMessage('No file is currently opened.');
        }
        return "no locators found"
}

export async function genUITest(activeEditor: vscode.TextEditor | undefined): Promise<string> {
        if (!activeEditor) {
                return "no active editor found";
        }
        let locators = await processFileContentAndHighlight(activeEditor);
        let testTool: string;
        if (locators.includes('cy.get')) {
                testTool = 'cypress';
        } else if (locators.includes('page.getBy')) {
                testTool = 'playwright';
        } else if (locators.includes('Android') || locators.includes('IOS')) {
                testTool = 'webdriverio';
        } else {
                testTool = 'selenium';
        }
        const selection = activeEditor.selection;
        const selectedText = activeEditor.document.getText(selection);
        interface UiStepCode {
                code: string;
        }
        let uiStepCode: UiStepCode;
        if (selectedText) {
                if (testTool == 'webdriverio') {
                        uiStepCode = await apiHelper.genMobileUITestCode(testTool, locators, selectedText);
                } else {
                        uiStepCode = await apiHelper.genWebUITestCode(testTool, locators, selectedText);
                }
                let code = uiStepCode ? parseCode(uiStepCode.code) : "no code generated";
                return code
        } else {
                return "no ui test case selected";
        }
}
export async function writeUITestCode(code: string, activeEditor: vscode.TextEditor | undefined) {
        if (activeEditor) {
                const document = activeEditor.document;
                const oldContent = document.getText();
                const locators = await extractLocatorCode(oldContent);

                if (locators) {
                        const locatorsEndPos = document.positionAt(oldContent.indexOf(locators) + locators.length);
                        const newPosition = new vscode.Position(locatorsEndPos.line + 1, 0); // Insert after the locators declaration
                        const insertIndex = document.offsetAt(newPosition);

                        const newContent = oldContent.slice(0, insertIndex) + '\n' + code + '\n' + oldContent.slice(insertIndex);

                        activeEditor.edit(editBuilder => {
                                const fullRange = new vscode.Range(
                                        document.positionAt(0),
                                        document.positionAt(oldContent.length)
                                );
                                editBuilder.replace(fullRange, newContent);
                        });
                } else {
                        vscode.window.showErrorMessage('Locators not found in the file.');
                }
        }
}