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


Used to retrieve a list of <code>scheduled_actions</code> in a region or to create or delete a <code>scheduled_actions</code> resource, use <code>scheduled_action</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="scheduled_action_name" /></td><td><code>string</code></td><td>Auto-generated unique identifier</td></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
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
scheduled_action_name,
auto_scaling_group_name
FROM aws.autoscaling.scheduled_actions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>scheduled_action</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- scheduled_action.iql (required properties only)
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
-- scheduled_action.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
autoscaling:DeleteScheduledAction,
autoscaling:DescribeScheduledActions
```

### List
```json
autoscaling:DescribeScheduledActions
```

