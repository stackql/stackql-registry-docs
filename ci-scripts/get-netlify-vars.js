const fs = require('fs');

    
const readTxtToArr = (path) => { 
    const data = fs.readFileSync(path, 'utf8');
    return data.split('\n');
}
module.exports = async ({ github, context, core, pathOutput }) => {
//1. set different config to each site as github action env vars
//2. use provider to set out, so next step will use those Netlify configs
//3. If it multiple, or updating root, output multiple configs, and loop as matrix in next step
const data = fs.readFileSync('diff.txt', 'utf8');
console.log(data);
}