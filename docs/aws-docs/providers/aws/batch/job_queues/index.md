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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>job_queue</code> resource or lists <code>job_queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobQueue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_queue_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_queue_arn" /></td><td><code>string</code></td><td>ARN of the Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="compute_environment_order" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="job_state_time_limit_actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduling_policy_arn" /></td><td><code>string</code></td><td>ARN of the Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html"><code>AWS::Batch::JobQueue</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ComputeEnvironmentOrder, Priority, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>job_queues</code> in a region.
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
FROM aws.batch.job_queues
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>job_queue</code>.
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
FROM aws.batch.job_queues
WHERE region = 'us-east-1' AND data__Identifier = '<JobQueueArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_queue</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.batch.job_queues (
 ComputeEnvironmentOrder,
 Priority,
 region
)
SELECT 
'{{ ComputeEnvironmentOrder }}',
 '{{ Priority }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.batch.job_queues (
 JobQueueName,
 ComputeEnvironmentOrder,
 JobStateTimeLimitActions,
 Priority,
 State,
 SchedulingPolicyArn,
 Tags,
 region
)
SELECT 
 '{{ JobQueueName }}',
 '{{ ComputeEnvironmentOrder }}',
 '{{ JobStateTimeLimitActions }}',
 '{{ Priority }}',
 '{{ State }}',
 '{{ SchedulingPolicyArn }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: job_queue
    props:
      - name: JobQueueName
        value: '{{ JobQueueName }}'
      - name: ComputeEnvironmentOrder
        value:
          - ComputeEnvironment: '{{ ComputeEnvironment }}'
            Order: '{{ Order }}'
      - name: JobStateTimeLimitActions
        value:
          - Action: '{{ Action }}'
            MaxTimeSeconds: '{{ MaxTimeSeconds }}'
            Reason: '{{ Reason }}'
            State: '{{ State }}'
      - name: Priority
        value: '{{ Priority }}'
      - name: State
        value: '{{ State }}'
      - name: SchedulingPolicyArn
        value: '{{ SchedulingPolicyArn }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.batch.job_queues
WHERE data__Identifier = '<JobQueueArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>job_queues</code> resource, the following permissions are required:

### Create
```json
Batch:CreateJobQueue,
Batch:TagResource,
Batch:DescribeJobQueues
```

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

### List
```json
Batch:DescribeJobQueues
```
