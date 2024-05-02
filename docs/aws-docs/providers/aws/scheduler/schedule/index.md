---
title: schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule
  - scheduler
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>schedule</code> resource, use <code>schedules</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::Schedule Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.scheduler.schedule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the schedule.</td></tr>
<tr><td><code>end_date</code></td><td><code>string</code></td><td>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.</td></tr>
<tr><td><code>flexible_time_window</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>The ARN for a KMS Key that will be used to encrypt customer data.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule_expression</code></td><td><code>string</code></td><td>The scheduling expression.</td></tr>
<tr><td><code>schedule_expression_timezone</code></td><td><code>string</code></td><td>The timezone in which the scheduling expression is evaluated.</td></tr>
<tr><td><code>start_date</code></td><td><code>string</code></td><td>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target</code></td><td><code>object</code></td><td></td></tr>
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
arn,
description,
end_date,
flexible_time_window,
group_name,
kms_key_arn,
name,
schedule_expression,
schedule_expression_timezone,
start_date,
state,
target
FROM aws.scheduler.schedule
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>schedule</code> resource, the following permissions are required:

### Read
```json
scheduler:GetSchedule
```

### Update
```json
scheduler:UpdateSchedule,
scheduler:GetSchedule,
iam:PassRole
```

### Delete
```json
scheduler:DeleteSchedule,
scheduler:GetSchedule
```

