---
title: scheduled_action
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_action
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>scheduled_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduled_action</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.scheduled_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_action_name</code></td><td><code>string</code></td><td>Auto-generated unique identifier</td></tr>
<tr><td><code>min_size</code></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
<tr><td><code>recurrence</code></td><td><code>string</code></td><td>The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.</td></tr>
<tr><td><code>time_zone</code></td><td><code>string</code></td><td>The time zone for the cron expression.</td></tr>
<tr><td><code>end_time</code></td><td><code>string</code></td><td>The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><code>start_time</code></td><td><code>string</code></td><td>The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><code>desired_capacity</code></td><td><code>integer</code></td><td>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.</td></tr>
<tr><td><code>max_size</code></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
scheduled_action_name,
min_size,
recurrence,
time_zone,
end_time,
auto_scaling_group_name,
start_time,
desired_capacity,
max_size
FROM awscc.autoscaling.scheduled_action
WHERE region = 'us-east-1'
AND data__Identifier = '{ScheduledActionName}';
AND data__Identifier = '{AutoScalingGroupName}';
```

## Permissions

To operate on the <code>scheduled_action</code> resource, the following permissions are required:

### Read
```json
autoscaling:DescribeScheduledActions
```

### Update
```json
autoscaling:PutScheduledUpdateGroupAction
```

### Delete
```json
autoscaling:DeleteScheduledAction,
autoscaling:DescribeScheduledActions
```

