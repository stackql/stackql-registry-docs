import siteConfig from '@generated/docusaurus.config';


export const providers = [
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
    {name: 'googleadmin', description: 'Google Workspace identity services.', title: 'Google Admin'},
    {name: 'azure', description: 'Cloud computing services offered by Microsoft.', title: 'Microsoft Azure'},
    {name: 'aws', description: 'Cloud computing by Amazon Web Services.', title: 'AWS'},
    {name: 'digitalocean', description: 'Cloud computing services and Infrastructure as a Service (IaaS).', title: 'Digital Ocean'},
    {name: 'github', description: 'Web-based version-control and collaboration.', title: 'GitHub'},
    {name: 'linode', description: 'Cloud computing services by Akamai.', title: 'Linode'},
    {name: 'netlify', description: 'Web development and content distribution platform.', title: 'Netlify'},
    {name: 'okta', description: 'Authentication and authorization services.', title: 'Okta'},
    {name: 'sumologic', description: 'Unified logs and metrics analytics platform.', title: 'Sumologic'},
    {name: 'azure_extras', description: 'Additional Azure cloud computing services by Microsoft.', title: 'Azure Extras'},
    {name: 'firebase', description: 'Mobile and web application development platform.', title: 'Firebase'},
    {name: 'k8s', description: 'Open source container management platform.', title: 'Kubernetes'},
    {name: 'vercel', description: 'Cloud platform for serverless deployment and hosting of web applications.', title: 'Vercel'},
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    return registry === name? `/providers/${name}`: `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
}