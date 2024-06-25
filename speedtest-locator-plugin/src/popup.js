document.addEventListener("DOMContentLoaded", async function () {
        document.getElementById("generate").addEventListener("click", async () => {
                const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
                let range = document.getElementById("range");
                if (range.value === "selectedPage") {
                        const response = await chrome.tabs.sendMessage(tab.id, { action: "getSelectedHTML" });
                }
                else { const response = await chrome.tabs.sendMessage(tab.id, { action: "getWholeHTML" }) };
        });

        document.getElementById("clear").addEventListener("click", function () {
                document.getElementById("result").value = ""
        })
        document.getElementById("copy").addEventListener("click", function () {
                let copiedText = document.getElementById("result");
                copiedText.select();
                copiedText.setSelectionRange(0, 99999); //For mobile devices
                navigator.clipboard.writeText(copiedText.value);
        })
});

function handleMobileContent(xmlString, numberOfNodes) {
        // Initialize DOMParser and XMLSerializer
        const parser = new DOMParser();
        const serializer = new XMLSerializer();

        // Parse the XML string
        const xmlDoc = parser.parseFromString(xmlString, "application/xml");

        // Get all elements
        const allNodes = Array.from(xmlDoc.querySelectorAll("*"));

        // Calculate the middle starting point
        const totalNodes = allNodes.length;
        if (totalNodes < numberOfNodes) {
                return "Not enough nodes to extract the requested number of middle nodes.";
        }

        const startIndex = Math.floor((totalNodes - numberOfNodes) / 2);
        const endIndex = startIndex + numberOfNodes;

        // Collect the XML strings of the middle nodes
        const middleNodeXmlStrings = [];
        for (let i = startIndex; i < endIndex; i++) {
                middleNodeXmlStrings.push(serializer.serializeToString(allNodes[i]));
        }

        return middleNodeXmlStrings;
}

function handleWebContent(bodyContent, numRows) {
        const lines = bodyContent.split('\n');
        if (lines.length > numRows) {
                const startIndex = Math.floor((lines.length - numRows) / 2);
                const endIndex = startIndex + numRows;
                const middleRows = lines.slice(startIndex, endIndex);
                return middleRows.join('\n');
        } else {
                return bodyContent
        }
}

function generateLocator(testTool, platform, pageContent) {
        const baseUrl = "http://127.0.0.1:9099";
        let spinner = document.getElementById("spinner");
        let generate = document.getElementById("generate");
        spinner.hidden = false;
        generate.disabled = true;
        if (testTool.startsWith('WebdriverIO')) {
                fetch(`${baseUrl}/mobiletest/genMobileLocator`, {
                        method: 'POST',
                        headers: {
                                'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                                client_tool: testTool,
                                platform: platform,
                                layout: pageContent
                        })
                })
                        .then(response => response.json())
                        .then(data => {
                                document.getElementById('result').value = data.locators;
                        })
                        .catch(error => {
                                console.error('Error:', error);
                                document.getElementById('result').value = 'Failed to fetch data';
                        }).finally(() => {
                                spinner.hidden = true;
                                generate.disabled = false;
                        });
        }
        else {
                fetch(`${baseUrl}/uitest/genWebLocator`, {
                        method: 'POST',
                        headers: {
                                'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                                testTool: testTool,
                                webPage: pageContent
                        })
                })
                        .then(response => response.json())
                        .then(data => {
                                document.getElementById('result').value = data.locators;
                        })
                        .catch(error => {
                                console.error('Error:', error);
                                document.getElementById('result').value = 'Failed to fetch data';
                        }).finally(() => {
                                spinner.hidden = true;
                                generate.disabled = false;
                        });
        }
}

chrome.runtime.onMessage.addListener(
        function (request, sender, sendResponse) {
                console.log(sender.tab ?
                        "from a content script:" + sender.tab.url :
                        "from the extension");
                const testTool = document.getElementById('tool').value;
                const number = document.getElementById('number').value;
                const platform = document.getElementById('platform').value;
                if (request.type === "getWholeHTML") {
                        let pageContent = handleWebContent(request.pageHTML, number);
                        generateLocator(testTool, platform, pageContent)
                }
                else if (request.type === "getSelectedHTML") {
                        let pageContent = document.getElementById('result');
                        if (testTool.startsWith('WebdriverIO')) {
                                let newPageContent = handleMobileContent(pageContent, number)
                                generateLocator(testTool, platform, newPageContent)
                        } else {
                                generateLocator(testTool, platform, pageContent)
                        }
                }
        }
);