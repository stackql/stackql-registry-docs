---
title: stack_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_sets
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
Retrieves a list of <code>stack_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>StackSet as a resource provides one-click experience for provisioning a StackSet and StackInstances</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.stack_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>stack_set_id</code></td><td><code>string</code></td><td>The ID of the stack set that you're creating.</td></tr>
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
stack_set_id
FROM aws.cloudformation.stack_sets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>stack_sets</code> resource, the following permissions are required:

### Create
```json
cloudformation:GetTemplateSummary,
cloudformation:CreateStackSet,
cloudformation:CreateStackInstances,
cloudformation:DescribeStackSetOperation,
cloudformation:ListStackSetOperationResults,
cloudformation:TagResource,
iam:PassRole
```

### List
```json
cloudformation:ListStackSets,
cloudformation:DescribeStackSet,
cloudformation:ListStackInstances,
cloudformation:DescribeStackInstance
```

