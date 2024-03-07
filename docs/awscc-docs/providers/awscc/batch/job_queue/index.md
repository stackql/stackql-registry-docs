---
title: job_queue
hide_title: false
hide_table_of_contents: false
keywords:
  - job_queue
  - batch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>job_queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>job_queue</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.batch.job_queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>job_queue_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>job_queue_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compute_environment_order</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scheduling_policy_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>job_queue</code> resource, the following permissions are required:

### Read
<pre>
Batch:DescribeJobQueues</pre>

### Update
<pre>
Batch:DescribeJobQueues,
Batch:UpdateJobQueue,
Batch:TagResource,
Batch:UnTagResource</pre>

### Delete
<pre>
Batch:UpdateJobQueue,
Batch:DescribeJobQueues,
Batch:DeleteJobQueue</pre>


## Example
```sql
SELECT
region,
job_queue_name,
job_queue_arn,
compute_environment_order,
priority,
state,
scheduling_policy_arn,
tags
FROM awscc.batch.job_queue
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;JobQueueArn&gt;'
```
