import siteConfig from '@generated/docusaurus.config';

export const providers = [
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
    {name: 'googleadmin', description: 'Google Workspace identity services.', title: 'Google Admin'},
    {name: 'azure', description: 'Cloud computing services offered by Microsoft.', title: 'Microsoft Azure'},
    {name: 'aws', description: 'Cloud computing by Amazon Web Services.', title: 'AWS'},
    {name: 'awscc', description: 'Cloud computing by Amazon Web Services.', title: 'AWS Cloud Control'},
    {name: 'digitalocean', description: 'Cloud computing services and Infrastructure as a Service (IaaS).', title: 'Digital Ocean'},
    {name: 'github', description: 'Web-based version-control and collaboration.', title: 'GitHub'},
    {name: 'linode', description: 'Cloud computing services by Akamai.', title: 'Linode'},
    {name: 'netlify', description: 'Web development and content distribution platform.', title: 'Netlify'},
    {name: 'okta', description: 'Authentication and authorization services.', title: 'Okta'},
    {name: 'azure_extras', description: 'Additional Azure cloud computing services by Microsoft.', title: 'Azure Extras'},
    {name: 'azure_isv', description: 'Independent Software Vendor Services on Azure.', title: 'Azure Native ISV'},
    {name: 'azure_stack', description: 'Azure Hybrid Apps Across Datacenters, Edge Locations, etc', title: 'Azure Stack'},
    {name: 'sumologic', description: 'Unified logs and metrics analytics platform.', title: 'Sumologic'},
    {name: 'firebase', description: 'Mobile and web application development platform.', title: 'Firebase'},
    {name: 'k8s', description: 'Open source container management platform.', title: 'Kubernetes'},
    {name: 'vercel', description: 'Cloud platform for serverless deployment and hosting of web applications.', title: 'Vercel'},
    {name: 'pagerduty', description: 'Incident management platform for real-time operations and response workflows.', title: 'PagerDuty'},  
    {name: 'datadog', description: 'Monitoring, alerting and reporting platform for cloud platforms and applications.', title: 'Datadog'},  
    {name: 'godaddy', description: 'Domain name registrations and hosting services.', title: 'Godaddy'},
    {name: 'homebrew', description: 'Open-source package manager for macOS and Linux.', title: 'Homebrew'},    
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    return registry === name? `/providers/${name}`: `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
}