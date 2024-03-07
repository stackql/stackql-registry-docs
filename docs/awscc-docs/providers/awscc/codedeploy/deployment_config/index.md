---
title: deployment_config
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_config
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
Gets an individual <code>deployment_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codedeploy.deployment_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>compute_platform</code></td><td><code>string</code></td><td>The destination platform type for the deployment (Lambda, Server, or ECS).</td></tr>
<tr><td><code>deployment_config_name</code></td><td><code>string</code></td><td>A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.</td></tr>
<tr><td><code>minimum_healthy_hosts</code></td><td><code>object</code></td><td>The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.</td></tr>
<tr><td><code>zonal_config</code></td><td><code>object</code></td><td>The zonal deployment config that specifies how the zonal deployment behaves</td></tr>
<tr><td><code>traffic_routing_config</code></td><td><code>object</code></td><td>The configuration that specifies how the deployment traffic is routed.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
compute_platform,
deployment_config_name,
minimum_healthy_hosts,
zonal_config,
traffic_routing_config
FROM awscc.codedeploy.deployment_config
WHERE region = 'us-east-1'
AND data__Identifier = '{DeploymentConfigName}';
```

## Permissions

To operate on the <code>deployment_config</code> resource, the following permissions are required:

### Read
```json
codedeploy:GetDeploymentConfig
```

### Delete
```json
codedeploy:GetDeploymentConfig,
codedeploy:DeleteDeploymentConfig
```

