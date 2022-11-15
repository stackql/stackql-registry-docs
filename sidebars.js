/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'stackql-provider-registry',
    {
      type: 'link',
      label: 'Product Home',
      href: '/home'
    },
    {
      type: 'link',
      label: 'Product Docs',
      href: '/docs'
    },    
    {
      type: 'category',
      label: 'Available Providers',
      collapsed: false,
      items: [{type: 'autogenerated', dirName: 'providers'}]
    },
    {
      type: 'link',
      label: 'Downloads',
      href: '/downloads'
    },
    {
      type: 'link',
      label: 'Blog',
      href: '/blog'
    },        
  ],
};

module.exports = sidebars;
