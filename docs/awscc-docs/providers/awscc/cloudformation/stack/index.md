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
Gets an individual <code>stack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stack</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capabilities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disable_rollback</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_termination_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>notification_ar_ns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>parent_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>root_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>change_set_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_policy_body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stack_policy_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_status_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>template_body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>timeout_in_minutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>last_update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
capabilities,
role_ar_n,
outputs,
description,
disable_rollback,
enable_termination_protection,
notification_ar_ns,
parameters,
parent_id,
root_id,
change_set_id,
stack_name,
stack_id,
stack_policy_body,
stack_policy_ur_l,
stack_status,
stack_status_reason,
tags,
template_body,
template_ur_l,
timeout_in_minutes,
last_update_time,
creation_time
FROM awscc.cloudformation.stack
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StackId&gt;'
```
