import React from 'react';

const spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
const termLines = [
    {
        text: 'SELECT machineType, COUNT(*)',
        cmd: true,
        delay: 80,
    },
    {
        text: 'FROM google.compute.instances',
        cmd: true,
        delay: 80,
    },
    {
        text: 'GROUP BY machineType',
        cmd: true,
        delay: 80,
    },
    {
        text: "WHERE zone = 'us-east1-a'",
        cmd: true,
        delay: 80,
    },
    {
        text: ' ',
        cmd: false,
        repeat: true,
        repeatCount: 3,
        frames: spinner.map(function (spinner) {
        return {
            text: spinner + ' Running query',
            delay: 10
        }
    })
    },
    {
        text: 
`+------------------------+
|  MACHINETYPE   | COUNT |
+------------------------+
| n1-standard-1  |   3   |
| n1-megamem-96  |   8   |
| c2-standard-60 |   4   |
+------------------------+`,
        cmd: false,
    }
]

export const homePageData = {
  title: 'Home',
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
  hero: {
    title: [
      'Every Cloud.',
      'Every Operation.',
      'One Language.',
    ],
    subtitle: 'Provision. Query. Secure.',
    animatedTerm: {
      termLines: termLines,
    },
  },
  features: [
    {
      title: 'Query Multiple Clouds',
      icon: 'fas fa-angle-double-right',
      link: '/features',
      description: (
        <>
          Use a familiar SQL language to perform interactive queries against cloud providers for inventory, security posture management, compliance, cost optimisation and more
        </>
      ),
    },
    {
      title: 'Deploy Cloud Resources',
      icon: 'fas fa-code',
      link: '/features',
      description: (
        <>
          Infrastructure-as-Code to deploy and configure cloud infrastructure and applications using a familiar language ... SQL.  Extensible to all cloud and SaaS providers.
        </>
      ),
    },
    {
      title: 'Manage Cloud Resources',
      icon: 'fas fa-layer-group',
      link: '/features',
      description: (
        <>
          Manage complete life cycle of cloud and SaaS assets from deployment to termination, including seamlessly handling existing cloud stacks and SaaS applications.
        </>
      ),
    },
  ],
};