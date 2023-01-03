import siteConfig from '@generated/docusaurus.config';


export const providers = [
    {name: 'aws', description: 'Cloud computing by Amazon Web Services.', title: 'AWS'},
    {name: 'azure', description: 'Cloud computing services offered by Microsoft.', title: 'Microsoft Azure'},
    {name: 'firebase', description: 'Mobile and web application development platform.', title: 'Firebase'},
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    // return registry === name? `/providers/${name}`: `https://stackql-${name}-docs.netlify.app/providers/${name}`
    return registry === name? `/providers/${name}`: `https://${name}-docs.stackql.io/providers/${name}`
}