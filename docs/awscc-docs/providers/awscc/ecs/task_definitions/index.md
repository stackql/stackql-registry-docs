---
title: task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions
  - ecs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task_definitions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecs.task_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>task_definition_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>task_definitions</code> resource, the following permissions are required:

### Create
```json
ecs:RegisterTaskDefinition,
ecs:DescribeTaskDefinition,
ecs:TagResource,
iam:GetRole,
iam:PassRole
```

### List
```json
ecs:ListTaskDefinitions,
ecs:DescribeTaskDefinition
```


## Example
```sql
SELECT
region,
task_definition_arn
FROM awscc.ecs.task_definitions
WHERE region = 'us-east-1'
```
