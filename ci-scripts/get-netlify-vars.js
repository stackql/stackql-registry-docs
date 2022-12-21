const fs = require('fs');
const os = require('os');


const regex = /^docs\/[a-zA-Z0-9_-]+-docs\/*/;;

const isMatchRegex = (path) => regex.test(path);
const rootName = 'registry'
const allProviders = ['aws', 'azure', rootName]   

const appendToOutput = (providers) => {
    const output = process.env['GITHUB_OUTPUT']
    const providerStr = providers.join(',')
    fs.appendFileSync(output, `provider_to_deploy=${JSON.stringify(providerStr)}${os.EOL}`)

}

module.exports = async ({ github, context, core, pathOutput }) => {
//1. set different config to each site as github action env vars
//2. use provider to set out, so next step will use those Netlify configs
//3. If it multiple, or updating root, output multiple configs, and loop as matrix in next step
    const changedFiles = process.env.CHANGED_FILES ? process.env.CHANGED_FILES.split(' ').filter(Boolean) : undefined
    let globalChange = false;

    if(!changedFiles){
        throw Error('No changed files found')
    }

    console.log('changedFiles', changedFiles)
   
    const providers = changedFiles.map(diff => {
        if(isMatchRegex(diff)){
            return diff.split('/')[1].split('-docs')[0]
        }
        
        globalChange = true;

    }).filter(Boolean)

    const uniqueProviders = [...new Set(providers)]

    console.log('uniqueProviders', uniqueProviders)
    console.log('globalChange', globalChange)

    const providersToDeploy = globalChange ? allProviders : uniqueProviders
    appendToOutput(providersToDeploy)

}