---
title: task_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - task_sets
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
Retrieves a list of <code>task_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task_sets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecs.task_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><code>service</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the task set.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cluster,
service,
id
FROM awscc.ecs.task_sets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>task_sets</code> resource, the following permissions are required:

### Create
```json
ecs:CreateTaskSet,
ecs:DescribeTaskSets,
ecs:TagResource
```

