---
title: composite_alarm_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - composite_alarm_tags
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

Expands all tag keys and values for <code>composite_alarms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>composite_alarm_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudwatch.composite_alarm_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the alarm</td></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name of the Composite Alarm</td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>string</code></td><td>Expression which aggregates the state of other Alarms (Metric or Composite Alarms)</td></tr>
<tr><td><CopyableCode code="alarm_description" /></td><td><code>string</code></td><td>The description of the alarm</td></tr>
<tr><td><CopyableCode code="actions_enabled" /></td><td><code>boolean</code></td><td>Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.</td></tr>
<tr><td><CopyableCode code="ok_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="alarm_actions" /></td><td><code>array</code></td><td>The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="insufficient_data_actions" /></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="actions_suppressor" /></td><td><code>string</code></td><td>Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.</td></tr>
<tr><td><CopyableCode code="actions_suppressor_wait_period" /></td><td><code>integer</code></td><td>Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr>
<tr><td><CopyableCode code="actions_suppressor_extension_period" /></td><td><code>integer</code></td><td>Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr>
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
Expands tags for all <code>composite_alarms</code> in a region.
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
tag_key,
tag_value
FROM aws.cloudwatch.composite_alarm_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>composite_alarm_tags</code> resource, see <a href="/providers/aws/cloudwatch/composite_alarms/#permissions"><code>composite_alarms</code></a>


