export function parseCode(code: string): string {
        const regex = /^```javascript([\s\S]*)```$/;
        const match = regex.exec(code);

        if (match) {
                return match[1];
        } else {
                return code;
        }
}