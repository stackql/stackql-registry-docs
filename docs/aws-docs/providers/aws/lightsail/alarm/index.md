---
title: alarm
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm
  - lightsail
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

Gets or operates on an individual <code>alarm</code> resource, use <code>alarms</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Alarm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.alarm" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_name" /></td><td><code>string</code></td><td>The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.</td></tr>
<tr><td><CopyableCode code="monitored_resource_name" /></td><td><code>string</code></td><td>The validation status of the SSL&#x2F;TLS certificate.</td></tr>
<tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the metric to associate with the alarm.</td></tr>
<tr><td><CopyableCode code="comparison_operator" /></td><td><code>string</code></td><td>The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.</td></tr>
<tr><td><CopyableCode code="contact_protocols" /></td><td><code>array</code></td><td>The contact protocols to use for the alarm, such as Email, SMS (text messaging), or both.</td></tr>
<tr><td><CopyableCode code="alarm_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datapoints_to_alarm" /></td><td><code>integer</code></td><td>The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (datapointsToAlarm) is the M.</td></tr>
<tr><td><CopyableCode code="evaluation_periods" /></td><td><code>integer</code></td><td>The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (evaluationPeriods) is the N.</td></tr>
<tr><td><CopyableCode code="notification_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the alarm is enabled. Notifications are enabled by default if you don't specify this parameter.</td></tr>
<tr><td><CopyableCode code="notification_triggers" /></td><td><code>array</code></td><td>The alarm states that trigger a notification.</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The value against which the specified statistic is compared.</td></tr>
<tr><td><CopyableCode code="treat_missing_data" /></td><td><code>string</code></td><td>Sets how this alarm will handle missing data points.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the alarm.</td></tr>
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
alarm_name,
monitored_resource_name,
metric_name,
comparison_operator,
contact_protocols,
alarm_arn,
datapoints_to_alarm,
evaluation_periods,
notification_enabled,
notification_triggers,
threshold,
treat_missing_data,
state
FROM aws.lightsail.alarm
WHERE data__Identifier = '<AlarmName>';
```

## Permissions

To operate on the <code>alarm</code> resource, the following permissions are required:

### Read
```json
lightsail:GetAlarms
```

### Update
```json
lightsail:PutAlarm,
lightsail:GetAlarms
```

### Delete
```json
lightsail:DeleteAlarm,
lightsail:GetAlarms
```

