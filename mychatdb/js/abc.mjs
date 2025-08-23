import { GoogleGenerativeAI } from "https://cdn.jsdelivr.net/npm/@google/generative-ai/+esm";
const genAI = new GoogleGenerativeAI('AIzaSyCxyH23ynapHtEASHfD4IrPFJmWSNEjK_M');
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
async function sendPrompt(prompt, fn) {
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    if (typeof (fn) === 'function')
        fn(text);
    else
        console.log(text);
}
window.mychatdb.sendPrompt = sendPrompt;
