---
title: stack
hide_title: false
hide_table_of_contents: false
keywords:
  - stack
  - cloudformation
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

Gets or operates on an individual <code>stack</code> resource, use <code>stacks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.stack" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_rollback" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_termination_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="root_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="change_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_policy_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stack_status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="template_body" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_in_minutes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="last_update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
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
capabilities,
role_arn,
outputs,
description,
disable_rollback,
enable_termination_protection,
notification_arns,
parameters,
parent_id,
root_id,
change_set_id,
stack_name,
stack_id,
stack_policy_body,
stack_policy_url,
stack_status,
stack_status_reason,
tags,
template_body,
template_url,
timeout_in_minutes,
last_update_time,
creation_time
FROM aws.cloudformation.stack
WHERE data__Identifier = '<StackId>';
```

## Permissions

To operate on the <code>stack</code> resource, the following permissions are required:

### Update
```json
cloudformation:DescribeStacks,
cloudformation:UpdateStack,
cloudformation:UpdateTerminationProtection,
cloudformation:SetStackPolicy,
iam:PassRole
```

### Delete
```json
cloudformation:DescribeStacks,
cloudformation:DeleteStack
```

### Read
```json
cloudformation:DescribeStacks,
cloudformation:GetStackPolicy,
cloudformation:GetTemplate
```

