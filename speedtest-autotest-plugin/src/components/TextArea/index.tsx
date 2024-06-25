import React, { useState, useEffect } from 'react';
import '../../static/style.css';

interface TextareaProps {
        value: string;
        onChange: (value: string) => void
}

export const Textarea: React.FC<TextareaProps> = ({ value, onChange }) => {
        const [textValue, setTextValue] = useState(value || '');
        useEffect(() => {
                setTextValue(value);
        }, [value]);

        const copyToClipboard = () => {
                navigator.clipboard.writeText(textValue);
        };

        const clearTextarea = () => {
                onChange('');
                setTextValue(' ');
        };

        const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
                const newValue = event.target.value;
                setTextValue(newValue);
                onChange(newValue);
        };


        return (
                <div style={{ position: 'relative' }}>
                        <textarea className='custom-textarea'
                                value={textValue}
                                onChange={handleChange}
                        />
                        <div className="textarea-buttons">
                                <button className="textarea-button"
                                        onClick={copyToClipboard}
                                >
                                        Copy
                                </button>
                                <button className="textarea-button"
                                        onClick={clearTextarea}
                                >
                                        Clear
                                </button>
                        </div>
                </div>
        );
};