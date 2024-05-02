---
title: job_queues
hide_title: false
hide_table_of_contents: false
keywords:
  - job_queues
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
Retrieves a list of <code>job_queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobQueue</td></tr>
<tr><td><b>Id</b></td><td><code>aws.batch.job_queues</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>job_queue_arn</code></td><td><code>undefined</code></td><td></td></tr>
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
job_queue_arn
FROM aws.batch.job_queues
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>job_queues</code> resource, the following permissions are required:

### Create
```json
Batch:CreateJobQueue,
Batch:TagResource,
Batch:DescribeJobQueues
```

### List
```json
Batch:DescribeJobQueues
```

