import siteConfig from '@generated/docusaurus.config';


export const providers = [
    {name: 'aws', description: 'Cloud computing by Amazon Web Services.'}]

export const getProviderSiteUrl = (name: string) =>{
    const registry = siteConfig.customFields?.registry
    return registry === name? `/providers/${name}`: `https://stackql-${name}-docs.netlify.app/providers/${name}`
}
