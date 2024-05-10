---
title: deployment_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_configs
  - codedeploy
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>deployment_configs</code> in a region or to create or delete a <code>deployment_configs</code> resource, use <code>deployment_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeDeploy::DeploymentConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codedeploy.deployment_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="deployment_config_name" /></td><td><code>string</code></td><td>A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
deployment_config_name
FROM aws.codedeploy.deployment_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>deployment_config</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- deployment_config.iql (required properties only)
INSERT INTO aws.codedeploy.deployment_configs (
 ComputePlatform,
 DeploymentConfigName,
 MinimumHealthyHosts,
 ZonalConfig,
 TrafficRoutingConfig,
 region
)
SELECT 
'{{ ComputePlatform }}',
 '{{ DeploymentConfigName }}',
 '{{ MinimumHealthyHosts }}',
 '{{ ZonalConfig }}',
 '{{ TrafficRoutingConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- deployment_config.iql (all properties)
INSERT INTO aws.codedeploy.deployment_configs (
 ComputePlatform,
 DeploymentConfigName,
 MinimumHealthyHosts,
 ZonalConfig,
 TrafficRoutingConfig,
 region
)
SELECT 
 '{{ ComputePlatform }}',
 '{{ DeploymentConfigName }}',
 '{{ MinimumHealthyHosts }}',
 '{{ ZonalConfig }}',
 '{{ TrafficRoutingConfig }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: deployment_config
    props:
      - name: ComputePlatform
        value: '{{ ComputePlatform }}'
      - name: DeploymentConfigName
        value: '{{ DeploymentConfigName }}'
      - name: MinimumHealthyHosts
        value:
          Value: '{{ Value }}'
          Type: '{{ Type }}'
      - name: ZonalConfig
        value:
          FirstZoneMonitorDurationInSeconds: '{{ FirstZoneMonitorDurationInSeconds }}'
          MonitorDurationInSeconds: '{{ MonitorDurationInSeconds }}'
          MinimumHealthyHostsPerZone:
            Value: '{{ Value }}'
            Type: '{{ Type }}'
      - name: TrafficRoutingConfig
        value:
          Type: '{{ Type }}'
          TimeBasedLinear:
            LinearInterval: '{{ LinearInterval }}'
            LinearPercentage: '{{ LinearPercentage }}'
          TimeBasedCanary:
            CanaryPercentage: '{{ CanaryPercentage }}'
            CanaryInterval: '{{ CanaryInterval }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codedeploy.deployment_configs
WHERE data__Identifier = '<DeploymentConfigName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployment_configs</code> resource, the following permissions are required:

### Create
```json
codedeploy:CreateDeploymentConfig
```

### Delete
```json
codedeploy:GetDeploymentConfig,
codedeploy:DeleteDeploymentConfig
```

### List
```json
codedeploy:ListDeploymentConfigs
```

