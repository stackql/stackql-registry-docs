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
Retrieves a list of <code>deployment_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeDeploy::DeploymentConfig</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codedeploy.deployment_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>deployment_config_name</code></td><td><code>string</code></td><td>A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
deployment_config_name
FROM aws.codedeploy.deployment_configs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>deployment_configs</code> resource, the following permissions are required:

### Create
```json
codedeploy:CreateDeploymentConfig
```

### List
```json
codedeploy:ListDeploymentConfigs
```

