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


Used to retrieve a list of <code>job_queues</code> in a region or to create or delete a <code>job_queues</code> resource, use <code>job_queue</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobQueue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_queue_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
job_queue_arn
FROM aws.batch.job_queues
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ComputeEnvironmentOrder": [
  {
   "ComputeEnvironment": "{{ ComputeEnvironment }}",
   "Order": "{{ Order }}"
  }
 ],
 "Priority": "{{ Priority }}"
}
>>>
--required properties only
INSERT INTO aws.batch.job_queues (
 ComputeEnvironmentOrder,
 Priority,
 region
)
SELECT 
{{ .ComputeEnvironmentOrder }},
 {{ .Priority }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "JobQueueName": "{{ JobQueueName }}",
 "ComputeEnvironmentOrder": [
  {
   "ComputeEnvironment": "{{ ComputeEnvironment }}",
   "Order": "{{ Order }}"
  }
 ],
 "JobStateTimeLimitActions": [
  {
   "Action": "{{ Action }}",
   "MaxTimeSeconds": "{{ MaxTimeSeconds }}",
   "Reason": "{{ Reason }}",
   "State": "{{ State }}"
  }
 ],
 "Priority": "{{ Priority }}",
 "State": "{{ State }}",
 "SchedulingPolicyArn": "{{ SchedulingPolicyArn }}",
 "Tags": {}
}
>>>
--all properties
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
 {{ .JobQueueName }},
 {{ .ComputeEnvironmentOrder }},
 {{ .JobStateTimeLimitActions }},
 {{ .Priority }},
 {{ .State }},
 {{ .SchedulingPolicyArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

