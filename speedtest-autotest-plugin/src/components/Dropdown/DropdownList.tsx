import React, { ChangeEvent, useState } from 'react';
import '../../static/style.css';


interface ModelDropdownProps {
        onSelectedModel: (model: string) => void;
}

const ModelDropdown: React.FC<ModelDropdownProps> = ({ onSelectedModel }) => {
        const [model, setModel] = useState('gpt-3.5-turbo');
        const handleModelChange = (event: ChangeEvent<HTMLSelectElement>) => {
                setModel(event.target.value);
                onSelectedModel(event.target.value);
        };

        return (
                <select
                        value={model}
                        onChange={handleModelChange}
                        className="custom-select">
                        <option value="gpt-3.5-turbo" className='custom-option'>gpt-3.5-turbo</option>
                        <option value="gpt-4-turbo" className='custom-option'>gpt-4-turbo</option>
                </select >

        );
};

interface TestToolDropdownProps {
        onSelectTestTool: (testTool: string) => void;
}

const TestToolDropdown: React.FC<TestToolDropdownProps> = ({ onSelectTestTool }) => {
        const [tool, setTool] = useState<string>('');
        const handleTestToolChange = (event: ChangeEvent<HTMLSelectElement>) => {
                setTool(event.target.value);
                onSelectTestTool(event.target.value);
        };

        return (
                <select
                        value={tool}
                        onChange={handleTestToolChange}
                        className="custom-select">
                        <option value="Jest" className='custom-option'>Jest</option>
                        <option value="Pyteset" className='custom-option'>Pytest</option>
                </select >
        )
};

interface LanguageDropdownProps {
        onSelectLanguage: (language: string) => void;
}

const LanguageDropdown: React.FC<LanguageDropdownProps> = ({ onSelectLanguage }) => {
        const [language, setLanguage] = useState('Javascript');

        const handleLanguageChange = (event: ChangeEvent<HTMLSelectElement>) => {
                setLanguage(event.target.value);
                onSelectLanguage(event.target.value);
        };

        return (
                <select
                        value={language}
                        onChange={handleLanguageChange}
                        className="custom-select">
                        <option value="Javascript" className='custom-option'>Javascript</option>
                        <option value="Typescript" className='custom-option'>Typescript</option>
                        <option value="Python" className='custom-option'>Python</option>
                </select >
        );
};

interface MethodDropdownProps {
        onSelectMethod: (method: string) => void;
}


const MethodDropdown: React.FC<MethodDropdownProps> = ({ onSelectMethod }) => {
        const [method, setMethod] = useState('GET');
        const handleMethodChange = (event: ChangeEvent<HTMLSelectElement>) => {
                setMethod(event.target.value)
                onSelectMethod(event.target.value);
        };

        return (
                <select
                        value={method}
                        onChange={handleMethodChange}
                        className="custom-select">
                        <option value="GET" className='custom-option'>GET</option>
                        <option value="POST" className='custom-option'>POST</option>
                        <option value="DELETE" className='custom-option'>DELETE</option>
                        <option value="PUT" className='custom-option'>PUT</option>
                </select >

        );
};

export { LanguageDropdown, TestToolDropdown, MethodDropdown, ModelDropdown }
