---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>scheduled_action</code> resource or lists <code>scheduled_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_action_name" /></td><td><code>string</code></td><td>Auto-generated unique identifier</td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="recurrence" /></td><td><code>string</code></td><td>The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.</td></tr>
<tr><td><CopyableCode code="time_zone" /></td><td><code>string</code></td><td>The time zone for the cron expression.</td></tr>
<tr><td><CopyableCode code="end_time" /></td><td><code>string</code></td><td>The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="desired_capacity" /></td><td><code>integer</code></td><td>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.</td></tr>
<tr><td><CopyableCode code="max_size" /></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
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
    <td><CopyableCode code="AutoScalingGroupName, region" /></td>
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
Gets all <code>scheduled_actions</code> in a region.
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
FROM aws.autoscaling.scheduled_actions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scheduled_action</code>.
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
FROM aws.autoscaling.scheduled_actions
WHERE region = 'us-east-1' AND data__Identifier = '<ScheduledActionName>|<AutoScalingGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.autoscaling.scheduled_actions (
 AutoScalingGroupName,
 region
)
SELECT 
'{{ AutoScalingGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.autoscaling.scheduled_actions (
 MinSize,
 Recurrence,
 TimeZone,
 EndTime,
 AutoScalingGroupName,
 StartTime,
 DesiredCapacity,
 MaxSize,
 region
)
SELECT 
 '{{ MinSize }}',
 '{{ Recurrence }}',
 '{{ TimeZone }}',
 '{{ EndTime }}',
 '{{ AutoScalingGroupName }}',
 '{{ StartTime }}',
 '{{ DesiredCapacity }}',
 '{{ MaxSize }}',
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
  - name: scheduled_action
    props:
      - name: MinSize
        value: '{{ MinSize }}'
      - name: Recurrence
        value: '{{ Recurrence }}'
      - name: TimeZone
        value: '{{ TimeZone }}'
      - name: EndTime
        value: '{{ EndTime }}'
      - name: AutoScalingGroupName
        value: '{{ AutoScalingGroupName }}'
      - name: StartTime
        value: '{{ StartTime }}'
      - name: DesiredCapacity
        value: '{{ DesiredCapacity }}'
      - name: MaxSize
        value: '{{ MaxSize }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.scheduled_actions
WHERE data__Identifier = '<ScheduledActionName|AutoScalingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scheduled_actions</code> resource, the following permissions are required:

### Create
```json
autoscaling:PutScheduledUpdateGroupAction,
autoscaling:DescribeScheduledActions
```

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

### List
```json
autoscaling:DescribeScheduledActions
```

