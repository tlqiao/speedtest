import React, { useState, useEffect, ChangeEvent } from 'react';
import { ApiHelper } from '../../service/base';
import '../../static/style.css';

const apiHelper = new ApiHelper();
interface ApiUrlDropdownProps {
        serverName: string;
        onSelectApiUrl: (apiUrl: string) => void;
}

const ApiUrlDropdown: React.FC<ApiUrlDropdownProps> = ({ serverName, onSelectApiUrl }) => {
        const [apiUrlList, setApiUrlList] = useState<string[]>([]);
        const [selectedValue, setSelectedValue] = useState<string>('');

        useEffect(() => {
                async function fetchApiUrlList() {
                        if (!serverName) return;
                        try {
                                const apiUrlList = (await apiHelper.getApiUrlList(serverName)).apiUrlList;
                                const defaultSelectedValue = apiUrlList.length > 0 ? apiUrlList[0] : '';
                                setApiUrlList(apiUrlList);
                                setSelectedValue(defaultSelectedValue);
                                onSelectApiUrl(defaultSelectedValue);
                        } catch (error) {
                                console.error('Error fetching API URL list:', error);
                        }
                }
                fetchApiUrlList();
        }, [serverName, onSelectApiUrl]);

        const handleDropdownChange = (event: ChangeEvent<HTMLSelectElement>) => {
                setSelectedValue(event.target.value);
                onSelectApiUrl(event.target.value);
        };
        const truncate = (str: string, maxLength: number) => {
                return str.length > maxLength ? str.substring(0, maxLength) + '...' : str;
        };

        return (
                <select
                        value={selectedValue}
                        onChange={handleDropdownChange}
                        className="custom-select"
                >
                        {
                                apiUrlList.map((option, index) => (
                                        <option key={index} value={option} className='custom-option'>{truncate(option, 40)}</option>
                                ))
                        }
                </select >
        );
};

export default ApiUrlDropdown;
