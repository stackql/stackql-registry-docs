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


const providers = [{name: 'aws', localPort: 3001}]


const providerDocItems = providers.map(provider =>{
  const name = provider.name
  const itemBaseUrl = `https://stackql-${name}-docs.netlify.app/providers/${name}`
  if(registry === name){
    return  {
        type: 'category',
        label: `${name}`,
        link:{type: 'doc', id: `${name}-doc`},
        collapsed: true,
        items:[
          {
            type: 'autogenerated',
            dirName: `providers/aws`,
          },
        ]
      }
  }
  return {
    type: 'html', 
    value: `<a href="${itemBaseUrl}">${name}</a>`,
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
