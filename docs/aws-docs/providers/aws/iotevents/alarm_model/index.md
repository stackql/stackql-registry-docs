---
title: alarm_model
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_model
  - iotevents
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


Gets or updates an individual <code>alarm_model</code> resource, use <code>alarm_models</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_model" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><CopyableCode code="alarm_model_description" /></td><td><code>string</code></td><td>A brief description of the alarm model.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="alarm_event_actions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="alarm_capabilities" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
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
alarm_model_name,
alarm_model_description,
role_arn,
key,
severity,
alarm_rule,
alarm_event_actions,
alarm_capabilities,
tags
FROM aws.iotevents.alarm_model
WHERE region = 'us-east-1' AND data__Identifier = '<AlarmModelName>';
```


## Permissions

To operate on the <code>alarm_model</code> resource, the following permissions are required:

### Read
```json
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource
```

### Update
```json
iotevents:UpdateAlarmModel,
iotevents:UpdateInputRouting,
iotevents:DescribeAlarmModel,
iotevents:ListTagsForResource,
iotevents:UntagResource,
iotevents:TagResource,
iam:PassRole
```

