const fs = require('fs');

    
module.exports = async ({ github, context, core, pathOutput }) => {
//1. set different config to each site as github action env vars
//2. use provider to set out, so next step will use those Netlify configs
//3. If it multiple, or updating root, output multiple configs, and loop as matrix in next step
    const diffs = fs.readFileSync('diff.txt', 'utf-8').split('\n').filter(Boolean)
    console.log(diffs)

}