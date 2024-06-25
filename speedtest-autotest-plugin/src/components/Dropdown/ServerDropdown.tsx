import React, { useState, useEffect, ChangeEvent } from 'react';
import { ApiHelper } from '../../service/base';
import '../../static/style.css';

const apiHelper = new ApiHelper();

interface ServerDropdownProps {
  onSelectServer: (selectedServer: string) => void;
}

const ServerDropdown: React.FC<ServerDropdownProps> = ({ onSelectServer }) => {
  const [options, setOptions] = useState<string[]>([]);
  const [selectedValue, setSelectedValue] = useState<string>('');

  useEffect(() => {
    async function fetchServerList() {
      try {
        const serverList = (await apiHelper.getServerList()).server_List;
        const defaultSelectedValue = serverList.length > 0 ? serverList[0] : '';
        setOptions(serverList);
        setSelectedValue(defaultSelectedValue);
        onSelectServer(defaultSelectedValue);
      } catch (error) {
        console.error('Error fetching server list:', error);
      }
    }
    fetchServerList();
  }, []);

  const handleServerChange = (event: ChangeEvent<HTMLSelectElement>) => {
    setSelectedValue(event.target.value);
    onSelectServer(event.target.value);
  };

  return (
    <select
      value={selectedValue}
      onChange={handleServerChange}
      className="custom-select">
      {
        options.map((option, index) => (
          <option key={index} value={option} className='custom-option'>{option}</option>
        ))
      }
    </select >
  );
};

export default ServerDropdown;
