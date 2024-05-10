---
title: composite_alarm
hide_title: false
hide_table_of_contents: false
keywords:
  - composite_alarm
  - cloudwatch
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


Gets or updates an individual <code>composite_alarm</code> resource, use <code>composite_alarms</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>composite_alarm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.composite_alarm" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the alarm</td></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the Composite Alarm</td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>string</code></td><td>Expression which aggregates the state of other Alarms (Metric or Composite Alarms)</td></tr>
<tr><td><CopyableCode code="alarm_description" /></td><td><code>string</code></td><td>The description of the alarm</td></tr>
<tr><td><CopyableCode code="actions_enabled" /></td><td><code>boolean</code></td><td>Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.</td></tr>
<tr><td><CopyableCode code="ok_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="alarm_actions" /></td><td><code>array</code></td><td>The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="insufficient_data_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="actions_suppressor" /></td><td><code>string</code></td><td>Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. </td></tr>
<tr><td><CopyableCode code="actions_suppressor_wait_period" /></td><td><code>integer</code></td><td>Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr>
<tr><td><CopyableCode code="actions_suppressor_extension_period" /></td><td><code>integer</code></td><td>Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs to associate with the composite alarm. You can associate as many as 50 tags with an alarm.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
alarm_name,
alarm_rule,
alarm_description,
actions_enabled,
ok_actions,
alarm_actions,
insufficient_data_actions,
actions_suppressor,
actions_suppressor_wait_period,
actions_suppressor_extension_period,
tags
FROM aws.cloudwatch.composite_alarm
WHERE region = 'us-east-1' AND data__Identifier = '<AlarmName>';
```


## Permissions

To operate on the <code>composite_alarm</code> resource, the following permissions are required:

### Read
```json
cloudwatch:DescribeAlarms,
cloudwatch:ListTagsForResource
```

### Update
```json
cloudwatch:DescribeAlarms,
cloudwatch:PutCompositeAlarm,
cloudwatch:TagResource,
cloudwatch:UntagResource
```

