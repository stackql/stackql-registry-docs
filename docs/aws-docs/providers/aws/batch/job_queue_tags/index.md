---
title: job_queue_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - job_queue_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>job_queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queue_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobQueue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_queue_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_queue_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_queue_arn" /></td><td><code>string</code></td><td>ARN of the Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="compute_environment_order" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="job_state_time_limit_actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduling_policy_arn" /></td><td><code>string</code></td><td>ARN of the Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>job_queues</code> in a region.
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
tag_key,
tag_value
FROM aws.batch.job_queue_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>job_queue_tags</code> resource, see <a href="/providers/aws/batch/job_queues/#permissions"><code>job_queues</code></a>

