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

const itemBaseUrl = isLocal? `http://localhost:3001/${registry}` : 'https://stackql-registry-docs.netlify.app/providers'
/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'stackql-provider-registry',
    {
      type: 'category',
      label: `Available Providers`,
      collapsible: true,
      collapsed: registry !== 'root',
      items: [
        {
          type: 'html', 
          value: `<a href="${itemBaseUrl}">aws</a>`,
        },
      ]
    }
  ],
};

module.exports = sidebars;
