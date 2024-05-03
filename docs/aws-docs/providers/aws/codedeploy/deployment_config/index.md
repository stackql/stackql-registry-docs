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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>deployment_config</code> resource, use <code>deployment_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeDeploy::DeploymentConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codedeploy.deployment_config" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The destination platform type for the deployment (Lambda, Server, or ECS).</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
compute_platform,
deployment_config_name,
minimum_healthy_hosts,
zonal_config,
traffic_routing_config
FROM aws.codedeploy.deployment_config
WHERE data__Identifier = '<DeploymentConfigName>';
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

