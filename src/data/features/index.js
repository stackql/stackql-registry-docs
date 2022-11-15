import React from 'react';

export const featuresPageData = {
    title: 'Features',
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
      title: `<span>Configuration<br /><span style="color:#00af91">as Data</span></span>`,
      subtitle: "A new approach to querying and provisioning cloud services.",
      label: "FAMILIAR, FUNCTIONAL, FLEXIBLE",
      cards: [
        {
          icon: 'fas fa-layer-group',
          title: 'Provision',
          text: `
          Configuration-as-Data approach to deploy and configure cloud and SaaS resources.      
          `,
          link: '#provision',
        },
        {
          icon: 'fas fa-map',
          title: 'Navigate',
          text: `
          Simplified API discovery for available service and resources in cloud and SaaS providers.      
          `,
          link: '#navigate',
        },
        {
          icon: 'fas fa-search',
          title: 'Query',
          text: `
          Perform live and interactive queries for inventory, compliance, cost optimization and more.      
          `,
          link: '#query',
        },
        {
          icon: 'fas fa-power-off',
          title: 'Operate',
          text: `
          Manage complete life cycle of cloud and SaaS resources from deployment to termination.      
          `,
          link: '#operate',
        },                        
      ],
    },
    content: { 
      title: `<span><span style="color:#00af91">One Solution</span> for everything</span>`,
      subtitle: 'What do you need to do?',
      features: [
        {
          id: 'provision',
          title: 'Cloud Provisioning Simplified.',
          code: `-- Deploy new cloud resources
INSERT INTO google.compute.instances (
  name,
  zone,
  machineType,
  project)
SELECT
  'worker-1',
  'australia-southeast1-a',
  'f1-micro',
  'infraql-demo';
          `,
          checks: [
            'No state file to maintain',
            'Use other tools interchangeably',
            'Create, query and interact with cloud resources',
            'Works seamlessly with existing stacks',
          ],
        },
        {
          id: 'navigate',
          title: 'Easily Navigate Cloud APIs.',
          code: `-- Discover available services and resources
SHOW SERVICES IN google LIKE '%compute%';
SHOW RESOURCES IN google.compute LIKE '%instances%';
-- Show attributes of a resource
DESCRIBE google.compute.instances;
DESCRIBE EXTENDED google.compute.instances;
-- Show available methods for a resource
SHOW METHODS IN google.compute.instances;
-- Create a provisioning template
SHOW INSERT INTO google.compute.instances;
        `,
          checks: [
            'Discover available services and resources',
            'Show attributes of a resource',
            'Show available methods for a resource',
            'Create provisioning templates',
          ],
        },    
        {
          id: 'query',
          title: 'Query Cloud and SaaS Assets.',
          code: `-- Query cloud resources
SELECT machineType, COUNT(*)
 FROM google.compute.instances
 GROUP BY machineType
 WHERE zone = 'us-east1-a';
/*
    +------------------------+
    |  MACHINETYPE   | COUNT |
    +------------------------+
    | n1-standard-1  |   3   |
    | n1-megamem-96  |   8   |
    | c2-standard-60 |   4   |
    +------------------------+      
*/
          `,
          checks: [
            'Perform live queries against cloud resources',
            'Query for security misconfigurations',
            'Inventory cloud assets for cost optimization',
            'Perform compliance and configuration drift checks'
          ],
        },
        {
          id: 'operate',
          title: 'Cloud Operations Made Easy.',
          code: `-- Perform operations on cloud resources
USE google;
EXEC compute.instances.start
  @instance = 'demo-instance-1',
  @project = 'infraql-demo',
  @zone = 'australia-southeast1-a';
✔ Instance started successfully      
          `,
          checks: [
            'Perform operations on cloud resources',
            'Interact with cloud services',
            'Make configuration changes',
            'Manage cloud infrastructure',
          ],
        },        
      ],    
    },    
};