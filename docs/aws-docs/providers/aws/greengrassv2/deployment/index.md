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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>deployment</code> resource, use <code>deployments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass V2 deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.deployment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="iot_job_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
target_arn,
parent_target_arn,
deployment_id,
deployment_name,
components,
iot_job_configuration,
deployment_policies,
tags
FROM aws.greengrassv2.deployment
WHERE data__Identifier = '<DeploymentId>';
```

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

