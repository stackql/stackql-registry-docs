import siteConfig from '@generated/docusaurus.config';


export const providers = [
    {name: 'aws', description: 'Cloud computing by Amazon Web Services.', title: 'AWS'},
    {name: 'azure', description: 'Cloud computing services offered by Microsoft.', title: 'Microsoft Azure'},
    {name: 'firebase', description: 'Mobile and web application development platform.', title: 'Firebase'},
    {name: 'github', description: 'Web-based version-control and collaboration.', title: 'GitHub'},
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
    {name: 'k8s', description: 'Open source container management platform.', title: 'Kubernetes'},
    {name: 'netlify', description: 'Web development and content distribution platform.', title: 'Netlify'},
    {name: 'okta', description: 'Authentication and authorization services.', title: 'Okta'},
    {name: 'sumologic', description: 'Unified logs and metrics analytics platform.', title: 'Sumologic'},
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    // return registry === name? `/providers/${name}`: `https://stackql-${name}-docs.netlify.app/providers/${name}`
    return registry === name? `/providers/${name}`: `https://${name}.stackql.io/providers/${name}`
}