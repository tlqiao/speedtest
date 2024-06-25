// get selected window does not work
let currentSelection = 'init';
document.addEventListener('mouseup', function () { setTimeout(handleSelection, 100); });
document.addEventListener('touchend', function () { setTimeout(handleSelection, 100); });
function handleSelection() {
        const selectedText = window.getSelection().toString();
        if (selectedText.length > 0) {
                currentSelection = selectedText;
        } else { currentSelection = "No content selected" }
}

chrome.runtime.onMessage.addListener(
        async function (message, sender, sendResponse) {
                console.log(sender.tab ?
                        "from a content script:" + sender.tab.url :
                        "from the extension,message action: " + message.action);
                if (message.action === "getWholeHTML") { await chrome.runtime.sendMessage({ type: "getWholeHTML", pageHTML: document.body.outerHTML }) }
                else if (message.action === "getSelectedHTML") { await chrome.runtime.sendMessage({ type: "getSelectedHTML", pageHTML: currentSelection }) }
        }
);