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

Creates, updates, deletes or gets a <code>deployment_config</code> resource or lists <code>deployment_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeDeploy::DeploymentConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codedeploy.deployment_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The destination platform type for the deployment (Lambda, Server, or ECS).</td></tr>
<tr><td><CopyableCode code="deployment_config_name" /></td><td><code>string</code></td><td>A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.</td></tr>
<tr><td><CopyableCode code="minimum_healthy_hosts" /></td><td><code>object</code></td><td>The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.</td></tr>
<tr><td><CopyableCode code="zonal_config" /></td><td><code>object</code></td><td>The zonal deployment config that specifies how the zonal deployment behaves</td></tr>
<tr><td><CopyableCode code="traffic_routing_config" /></td><td><code>object</code></td><td>The configuration that specifies how the deployment traffic is routed.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>deployment_configs</code> in a region.
```sql
SELECT
region,
deployment_config_name
FROM aws.codedeploy.deployment_configs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>deployment_config</code>.
```sql
SELECT
region,
compute_platform,
deployment_config_name,
minimum_healthy_hosts,
zonal_config,
traffic_routing_config
FROM aws.codedeploy.deployment_configs
WHERE region = 'us-east-1' AND data__Identifier = '<DeploymentConfigName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
codedeploy:GetDeploymentConfig
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

