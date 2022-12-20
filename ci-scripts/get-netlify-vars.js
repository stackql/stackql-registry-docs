const fs = require('fs');



const regex = /^docs\/[a-zA-Z0-9_-]+-docs\/*/;;

const isMatchRegex = (path) => regex.test(path);

const allProviders = ['aws', 'azure']   

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

    process.env.GITHUB_OUTPUT=process.env.GITHUB_OUTPUT + `provider_to_deploy=${providersToDeploy.join(',')}`


}