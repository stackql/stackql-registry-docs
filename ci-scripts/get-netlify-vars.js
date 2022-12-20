const fs = require('fs');



const regex = /^docs\/[a-zA-Z0-9_-]+-docs\/providers\/[a-zA-Z0-9_-]+$/;



const isMatchRegex = (path) => regex.test(path);

module.exports = async ({ github, context, core, pathOutput }) => {
//1. set different config to each site as github action env vars
//2. use provider to set out, so next step will use those Netlify configs
//3. If it multiple, or updating root, output multiple configs, and loop as matrix in next step
    const changedFiles = process.env.CHANGED_FILES
    console.log('changedFiles', changedFiles)
    const diffs = fs.readFileSync('diff.txt', 'utf-8').split('\n').filter(Boolean)
    console.log(diffs)
    const providers = diffs.map(diff => {
        if(isMatchRegex(diff)){
            return diff.split('/')[2].split('-docs')[0]
        }}).filter(Boolean)
    console.log(providers)

}