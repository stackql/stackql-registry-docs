---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
  - greengrassv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>deployment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.greengrassv2.deployment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parent_target_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>components</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>iot_job_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>deployment_policies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>deployment</code> resource, the following permissions are required:

### Read
```json
greengrass:GetDeployment,
iot:DescribeJob,
iot:DescribeThing,
iot:DescribeThingGroup,
iot:GetThingShadow
```

### Update
```json
greengrass:GetDeployment,
greengrass:TagResource,
greengrass:UntagResource,
iot:DescribeJob
```

### Delete
```json
greengrass:DeleteDeployment,
greengrass:CancelDeployment,
iot:CancelJob,
iot:DeleteJob,
iot:DescribeJob
```


## Example
```sql
SELECT
region,
target_arn,
parent_target_arn,
deployment_id,
deployment_name,
components,
iot_job_configuration,
deployment_policies,
tags
FROM awscc.greengrassv2.deployment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DeploymentId&gt;'
```
