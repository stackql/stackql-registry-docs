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

const itemBaseUrl = isLocal? `http://localhost:3001/${registry}` : `https://stackql-aws-docs.netlify.app/providers`

//If is root, the items should all be link
//If is provider, the doc of the provider should be:
// {
//   type: 'category',
//   label: `AWS`,
//   link:{type: 'doc', id: 'aws/aws-doc'},
//   items:[
//     {
//       type: 'autogenerated',
//       dirName: 'aws/provider-resources',
//     },
//   ]
// }

const providerDocItems = providers.map(provider =>{
  const name = provider.name
  const itemBaseUrl = isLocal? `http://localhost:${provider.localPort}` : `https://stackql-${name}-docs.netlify.app/`
  if(registry === name){
    return  {
        type: 'category',
        label: `${name}`,
        link:{type: 'doc', id: `${name}/${name}-doc`},
        items:[
          {
            type: 'autogenerated',
            dirName: `${name}/provider-resources`,
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
