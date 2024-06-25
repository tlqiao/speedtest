import '../../static/style.css'
import { MESSAGE } from '../../constants'
import { Button } from 'antd';
import React from 'react';
interface SaveButtonProps {
        textareaValue: string
}
export const SaveToFileButton: React.FC<SaveButtonProps> = ({ textareaValue }) => {
        const handleClick = () => {
                vscode.postMessage({
                        command: MESSAGE.saveToFileMessage,
                        content: textareaValue
                });
        };

        return (
                <Button className='custom-button' onClick={handleClick}>Save</Button>
        );
};
