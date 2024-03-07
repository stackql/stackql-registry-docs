---
title: continuous_deployment_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_deployment_policy
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>continuous_deployment_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>continuous_deployment_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>continuous_deployment_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.continuous_deployment_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>continuous_deployment_policy_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>continuous_deployment_policy</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteContinuousDeploymentPolicy,
cloudfront:GetContinuousDeploymentPolicy
```

### Read
```json
cloudfront:GetContinuousDeploymentPolicy
```

### Update
```json
cloudfront:UpdateContinuousDeploymentPolicy,
cloudfront:GetContinuousDeploymentPolicy
```


## Example
```sql
SELECT
region,
continuous_deployment_policy_config,
id,
last_modified_time
FROM awscc.cloudfront.continuous_deployment_policy
WHERE data__Identifier = '&lt;Id&gt;'
```
