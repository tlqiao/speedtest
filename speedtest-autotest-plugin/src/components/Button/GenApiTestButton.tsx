import React, { useState } from 'react';
import { ApiHelper } from '../../service/base';
import { CONFIGS } from '../../config/configs'
import { Button, Spin } from 'antd';
import { LoadingOutlined } from "@ant-design/icons";
import { MESSAGE } from "../../constants";
import '../../static/style.css';


interface GenAPITestButtonProps {
        language: string;
        testTool: string;
        serverName: string;
        apiUrl: string;
        method: string;
        testContext: any;
        onCodeGenerated: (code: string) => void;
}

const apiHelper = new ApiHelper();

export const GenAPITestButton: React.FC<GenAPITestButtonProps> = ({
        language,
        testTool,
        serverName,
        apiUrl,
        method,
        testContext,
        onCodeGenerated
}) => {
        const [loading, setLoading] = useState(false);
        const saveCode = async (code: string) => {
                vscode.postMessage({
                        command: MESSAGE.saveToFileMessage,
                        content: code
                })
        }
        const handleButtonClick = async () => {
                try {
                        setLoading(true);
                        const apiTestCodePromise = apiHelper.genApiTestCode(
                                language,
                                testTool,
                                serverName,
                                apiUrl,
                                method,
                                testContext
                        );
                        const timeoutPromise = new Promise<void>((resolve) => {
                                setTimeout(() => {
                                        resolve();
                                }, CONFIGS.timeout);
                        });
                        await Promise.race([apiTestCodePromise, timeoutPromise]);
                        const apiTestCode = await apiTestCodePromise;
                        onCodeGenerated(apiTestCode.code);
                        await saveCode(apiTestCode.code)
                } catch (error) {
                        console.error('Error generating API test code:', error);
                } finally {
                        setLoading(false);
                }
        };
        return (

                <Button className="custom-button"
                        icon={loading ? <Spin indicator={<LoadingOutlined spin />} /> : null}
                        disabled={loading}
                        onClick={handleButtonClick}>GenTest</Button>
        );
};
