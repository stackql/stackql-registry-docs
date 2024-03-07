---
title: primary_task_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - primary_task_sets
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
Retrieves a list of <code>primary_task_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>primary_task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>primary_task_sets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecs.primary_task_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><code>service</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>primary_task_sets</code> resource, the following permissions are required:

### Create
<pre>
ecs:DescribeTaskSets,
ecs:UpdateServicePrimaryTaskSet</pre>


## Example
```sql
SELECT
region,
cluster,
service
FROM awscc.ecs.primary_task_sets
WHERE region = 'us-east-1'
```
