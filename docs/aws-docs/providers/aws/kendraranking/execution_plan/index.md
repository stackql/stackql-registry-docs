---
title: execution_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - execution_plan
  - kendraranking
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>execution_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>execution_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A KendraRanking Rescore execution plan</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kendraranking.execution_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the execution plan</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for labeling the execution plan</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity_units</code></td><td><code>object</code></td><td>Capacity units</td></tr>
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
id,
arn,
description,
tags,
name,
capacity_units
FROM aws.kendraranking.execution_plan
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>execution_plan</code> resource, the following permissions are required:

### Read
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:ListTagsForResource
```

### Update
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:UpdateRescoreExecutionPlan,
kendra-ranking:ListTagsForResource,
kendra-ranking:TagResource,
kendra-ranking:UntagResource
```

### Delete
```json
kendra-ranking:DescribeRescoreExecutionPlan,
kendra-ranking:DeleteRescoreExecutionPlan
```

