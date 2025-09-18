import siteConfig from '@generated/docusaurus.config';

export const providers = [
    {name: 'aws', description: 'Cloud computing services by AWS.', title: 'AWS'},
    {name: 'azure', description: 'Cloud computing services offered by Microsoft.', title: 'Microsoft Azure'},
    {name: 'google', description: 'Cloud computing services offered by Google.', title: 'Google'},
    {name: 'github', description: 'Web-based version-control and collaboration.', title: 'GitHub'},
    {name: 'snowflake', description: 'Cloud data platform for data warehousing and analytics.', title: 'Snowflake'},
    {name: 'databricks_workspace', description: 'Workspace resources and ML operations for Databricks.', title: 'Databricks Workspace'},
    {name: 'databricks_account', description: 'Account management and provisioning for Databricks.', title: 'Databricks Account'},
    {name: 'openai', description: 'AI models and services by OpenAI.', title: 'OpenAI'},
    {name: 'anthropic', description: 'AI language models and services powered by Claude.', title: 'Anthropic'},
    {name: 'k8s', description: 'Open source container management platform.', title: 'Kubernetes'},
    {name: 'googleadmin', description: 'Google Workspace identity services.', title: 'Google Admin'},
    {name: 'okta', description: 'Authentication and authorization services.', title: 'Okta'},
    {name: 'datadog', description: 'Monitoring, alerting and reporting platform.', title: 'Datadog'},
    {name: 'confluent', description: 'Managed Kafka clusters and streaming services.', title: 'Confluent Cloud'},
    {name: 'firebase', description: 'Mobile and web application development platform.', title: 'Firebase'},
    {name: 'netlify', description: 'Web development and content distribution platform.', title: 'Netlify'},
    {name: 'vercel', description: 'Cloud platform for serverless web application deployment.', title: 'Vercel'},
    {name: 'digitalocean', description: 'Cloud computing services and Infrastructure as a Service.', title: 'Digital Ocean'},
    {name: 'pagerduty', description: 'Incident management platform for real-time operations.', title: 'PagerDuty'},
    {name: 'sumologic', description: 'Unified logs and metrics analytics platform.', title: 'Sumologic'},
    {name: 'linode', description: 'Cloud computing services by Akamai.', title: 'Linode'},
    {name: 'azure_extras', description: 'Additional Azure cloud computing services by Microsoft.', title: 'Azure Extras'},
    {name: 'azure_isv', description: 'Independent Software Vendor Services on Azure.', title: 'Azure Native ISV'},
    {name: 'azure_stack', description: 'Azure Hybrid Apps Across Datacenters, Edge Locations.', title: 'Azure Stack'},
    {name: 'godaddy', description: 'Domain name registrations and hosting services.', title: 'Godaddy'},
    {name: 'homebrew', description: 'Open-source package manager for macOS and Linux.', title: 'Homebrew'},
]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    if(registry === name){
        return `/providers/${name}`
    } else if (
        [
        'okta',
        'snowflake',
        'google',
        'googleadmin',
        'googleworkspace',
        'firebase',
        'databricks_workspace',
        'databricks_account',
        'digitalocean',
        'linode',
        'datadog',
        'godaddy',
        'netlify',
        'pagerduty',
        'azure',
        'azure_extras',
        'azure_isv',
        'azure_stack',
        'aws',     
        'sumologic',
        'vercel',
        'k8s',
        'homebrew',   
    ].includes(name)) {
        return `https://${name.replace('_', '-')}-provider.stackql.io/`
    } else {
        return `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
    }
    // return registry === name ? `/providers/${name}`: `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
}