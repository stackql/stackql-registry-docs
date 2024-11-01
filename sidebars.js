/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check
const isLocal = process.env.NODE_ENV=== 'development'
const registry = process.env.REGISTRY || 'root'

const providers = [
  {name: 'aws'},
  {name: 'azure'}, 
  {name: 'google'},
  {name: 'googleadmin'},
  {name: 'digitalocean'},   
  {name: 'github'},
  {name: 'confluent'},
  {name: 'openai'},
  {name: 'anthropic'},
  {name: 'linode'},
  {name: 'netlify'},
  {name: 'okta'},
  {name: 'sumologic'},
  {name: 'firebase'}, 
  {name: 'k8s'},
  {name: 'vercel'}, 
  {name: 'pagerduty'},
  {name: 'datadog'},
  {name: 'godaddy'},
  {name: 'homebrew'},     
  {name: 'azure_extras'},
  {name: 'azure_isv'},
  {name: 'azure_stack'},  
]

const getProviderSiteUrl = (name) =>{
    return `https://${name.replace('_', '-')}.stackql.io/providers/${name}`
}

const providerDocItems = providers.map(provider =>{
  const name = provider.name
  //TODO: move item url into providers file, create getUrl as function
  if(registry === name){
    return  {
        type: 'category',
        label: `${name}`,
        link:{type: 'doc', id: `${name}-doc`},
        collapsed: true,
        items:[
          {
            type: 'autogenerated',
            dirName: `providers/${registry}`,
          },
        ]
      }
  }
  return {
    type: 'html', 
    value: `<a href="${getProviderSiteUrl(name)}">${name}</a>`,
  }
})


/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'stackql-provider-registry',
    {
      type: 'category',
      label: `Available Providers`,
      collapsible: true,
      collapsed: false,
      // @ts-ignore
      items: providerDocItems
    },
  
  ],
};

module.exports = sidebars;
