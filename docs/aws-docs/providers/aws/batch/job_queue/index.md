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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>job_queue</code> resource, use <code>job_queues</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobQueue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_queue" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_queue_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_queue_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_environment_order" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="job_state_time_limit_actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduling_policy_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
job_queue_name,
job_queue_arn,
compute_environment_order,
job_state_time_limit_actions,
priority,
state,
scheduling_policy_arn,
tags
FROM aws.batch.job_queue
WHERE data__Identifier = '<JobQueueArn>';
```

## Permissions

To operate on the <code>job_queue</code> resource, the following permissions are required:

### Read
```json
Batch:DescribeJobQueues
```

### Update
```json
Batch:DescribeJobQueues,
Batch:UpdateJobQueue,
Batch:TagResource,
Batch:UnTagResource
```

### Delete
```json
Batch:UpdateJobQueue,
Batch:DescribeJobQueues,
Batch:DeleteJobQueue
```

