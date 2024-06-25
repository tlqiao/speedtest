import React from 'react';
import '../../static/style.css';
import { ApiHelper } from '../../service/base';
import { Button, message } from 'antd';


interface ApiDetails {
        apiReq: {
                [key: string]: any;
        };
        apiRes: {
                [key: string]: any;
        };
}

interface GetDetailsButtonProps {
        serverName: string;
        method: string;
        apiUrl: string;
        onClick: (apiDetails: ApiDetails) => void;
}

const apiHelper = new ApiHelper();

export const GetDetailsButton: React.FC<GetDetailsButtonProps> = ({ serverName, method, apiUrl, onClick }) => {
        const handleButtonClick = async () => {
                try {
                        const apiDetails = await apiHelper.getApiReqRes(serverName, apiUrl, method);
                        onClick(apiDetails);
                } catch (error) {
                        message.error('Error fetching API details');
                }
        };
        return (
                <Button className="custom-button" onClick={handleButtonClick}>
                        Get
                </Button>
        );
};
