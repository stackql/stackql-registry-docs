import siteConfig from '@generated/docusaurus.config';


export const providers = [
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
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
    // {name: 'googleworkspace', description: 'Productivity and collaboration tools for businesses.', title: 'Google Workspace'},
    // {name: 'googlemybusiness', description: 'Tools for businesses to manage their online presence.', title: 'Google My Business'},
    // {name: 'googledevelopers', description: 'Developer APIs by Google.', title: 'Google Developer APIs'},
    // {name: 'googleanalytics', description: 'Web tracking and analytics service.', title: 'Google Analytics'},
    // {name: 'googleads', description: 'Online advertising platform by Google.', title: 'Google Ads'},
    // {name: 'youtube', description: 'Online video sharing and social media platform.', title: 'Youtube'},
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    return registry === name? `/providers/${name}`: `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
}