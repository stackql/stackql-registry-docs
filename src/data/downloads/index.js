import React from 'react';

export const downloadsPageData = {
    title: 'Downloads',
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
        title: `<span><span style="color:#00af91">Download</span> StackQL</span>`,
        subtitle: "A new approach to querying and provisioning cloud services.",
        label: "FAMILIAR, FUNCTIONAL, FLEXIBLE",
    },
    downloadCards: [
        {
          platform: 'windows',
          icon: 'fab fa-windows',
          title: 'Microsoft Windows',
          description: 'x86 and x64',
          buttons: [
            {
              url:  'https://releases.stackql.io/stackql/latest/stackql_windows_amd64.msi',
              text: 'Download MSI',
              icon: 'fas fa-download',
            },
            {
              url:  'https://releases.stackql.io/stackql/latest/stackql_windows_amd64.zip',
              text: 'Download ZIP',
              icon: 'fas fa-download',
            },    
          ],
        },
        {
          platform: 'macos',  
          icon: 'fab fa-apple',
          title: 'MacOS',
          description: '64-bit AMD and ARM',
          buttons: [
            {
              url:  'https://storage.googleapis.com/stackql-public-releases/latest/stackql_darwin_multiarch.pkg',
              text: 'Download PKG',
              icon: 'fas fa-download',
            },
          ],
        },
        {
          platform: 'linux',  
          icon: 'fab fa-linux',
          title: 'Linux',
          description: 'x86 and x64',
          buttons: [
            {
              url:  'https://releases.stackql.io/stackql/latest/stackql_linux_amd64.zip',
              text: 'Download ZIP',
              icon: 'fas fa-download',
            },
          ]
        }
      ]
};