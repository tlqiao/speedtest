import React, { useState, useEffect } from 'react';
import { Textarea } from '../components/TextArea';
import { TestToolDropdown, MethodDropdown, ModelDropdown, LanguageDropdown } from '../components/Dropdown/DropdownList';
import ApiUrlDropdown from '../components/Dropdown/ApiUrlDropdown';
import ServerDropdown from '../components/Dropdown/ServerDropdown';
import { GetDetailsButton } from '../components/Button/GetDetailsButton';
import '../static/style.css'
import { GenAPITestButton } from '../components/Button/GenApiTestButton';
import { SaveToFileButton } from '../components/Button/SaveToFileButton'

const Layout = () => {
        const [language, setLanguage] = useState('');
        const [serverName, setServerName] = useState('');
        const [apiUrl, setApiUrl] = useState('');
        const [testTool, setTestTool] = useState('Jest');
        const [method, setMethod] = useState("GET");
        const [model, setModel] = useState("gpt-3.5-turbo");
        const [textareaValue, setTextareaValue] = useState('');
        const handleTextareaChange = (value: string) => {
                setTextareaValue(value);
        };
        const handleGetApiDetailsButtonClick = async (apiDetails: any) => {
                let value = apiDetails ? JSON.stringify(apiDetails, null, 2) : ''
                setTextareaValue(value);
        };

        const handleGenApiTestButtonClick = async (code: string) => {
                setTextareaValue(code);
        };

        const sendDropdownValues = () => {
                const apiInfos = {
                        model,
                        language,
                        testTool,
                        serverName,
                        apiUrl,
                        method,
                };
                vscode.postMessage({
                        command: 'apiInfoChange',
                        content: JSON.stringify(apiInfos)
                });
        };

        useEffect(() => {
                sendDropdownValues();
        }, [model, language, testTool, serverName, apiUrl, method]);

        return (
                <div className="container">
                        <div className="dropdown-container">
                                <div className="dropdown-item">
                                        <label className='custom-label'>Model:</label>
                                        <ModelDropdown onSelectedModel={setModel} />
                                </div>
                                <div className="dropdown-item">
                                        <label className='custom-label'>Language:</label>
                                        <LanguageDropdown onSelectLanguage={setLanguage} />
                                </div>
                                <div className="dropdown-item">
                                        <label className='custom-label'>Tool:</label>
                                        <TestToolDropdown onSelectTestTool={setTestTool} />
                                </div>
                                <div className="dropdown-item">
                                        <label className='custom-label'>Server:</label>
                                        <ServerDropdown onSelectServer={setServerName} />
                                </div>
                                <div className="dropdown-item">
                                        <label className='custom-label'>Url:</label>
                                        <ApiUrlDropdown serverName={serverName} onSelectApiUrl={setApiUrl} />
                                </div>
                                <div className="dropdown-item">
                                        <label className='custom-label'>Method:</label>
                                        <MethodDropdown onSelectMethod={setMethod} />
                                </div>
                        </div>
                        <div>
                                <div className='textarea-container'>
                                        <Textarea value={textareaValue} onChange={handleTextareaChange} />
                                </div>
                        </div>
                        <div className="action-container">
                                <GetDetailsButton serverName={serverName} method={method} apiUrl={apiUrl} onClick={handleGetApiDetailsButtonClick}></GetDetailsButton>
                                <GenAPITestButton language={language} testTool={testTool} serverName={serverName} method={method} apiUrl={apiUrl} testContext={textareaValue} onCodeGenerated={handleGenApiTestButtonClick}></GenAPITestButton>
                                <SaveToFileButton textareaValue={textareaValue} />
                        </div>
                </div >
        )
};
export default Layout;
