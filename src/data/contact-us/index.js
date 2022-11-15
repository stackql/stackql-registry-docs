import React from 'react';

export const contactusPageData = {
    title: 'Contact Us',
    description: 'StackQL is an open-source infrastructure-as-code tool that enables you to deploy, configure, query and operate cloud and SaaS services using SQL.',
    image: '/img/stackql-cover.png',
    keywords: [
      'stackql',
      'stack',
      'cloud query',
      'infrastructure query',
      'infrastructre-as-code',
      'iac',
      'configuration-as-data',
      'infraql',
      'cspm',
      'query google cloud resources',
      'okta deployment',
    ],    
    header: {
        title: `<span>Get <span style="color:#00af91">in Touch</span></span>`,
        subtitle: "A new approach to querying and provisioning cloud services.",
    },
    body: {
        form: {
            heading: "Send us a message",
            hubspot: {
                region: 'na1',
                portalId: '21220110',
                formId: '85a06e5f-d7aa-46ec-9953-b26ff962eedb',
            },
        },    
        address: {
            heading: 'Address',
            line1: 'Level 24, 570 Bourke Street',
            line2: 'Melbourne, Victoria 3000, Australia',
            phone: '+61 (0)3 8658 5880',
            phoneLink: 'tel:+61 (0)3 8658 5880',
            email: 'info@stackql.io',
            emailLink: 'mailto:info@stackql.io',
            twitter: '@stackql',
            twitterLink: 'https://twitter.com/stackql',
            map: {
                mapsApiKey: 'AIzaSyD1DhS73DM65hHWcZTqqrerWbqICO9MuDA', 
                lat: 37.8153, 
                long: 144.9565, 
                defaultZoom: 11, 
                markerTitle: 'StackQL Studios',
            },
        },    
    },     
};    