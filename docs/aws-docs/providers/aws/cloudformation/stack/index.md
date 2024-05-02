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
Gets or operates on an individual <code>stack</code> resource, use <code>stacks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capabilities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disable_rollback</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_termination_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>notification_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>parent_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>root_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>change_set_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_policy_body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stack_policy_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_status_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>template_body</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>template_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>timeout_in_minutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>last_update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

