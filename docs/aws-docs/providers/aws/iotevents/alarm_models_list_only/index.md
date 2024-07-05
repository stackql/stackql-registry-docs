---
title: alarm_models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_models_list_only
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

Lists <code>alarm_models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/alarm_models/"><code>alarm_models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::AlarmModel resource creates a alarm model. AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you measure for your equipment and processes. You can create alarms that send notifications when a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize performance of your equipment and processes.<br />Alarms are instances of alarm models. The alarm model specifies what to detect, when to send notifications, who gets notified, and more. You can also specify one or more supported actions that occur when the alarm state changes. AWS IoT Events routes input attributes derived from your data to the appropriate alarms. If the data that you're monitoring is outside the specified range, the alarm is invoked. You can also acknowledge the alarms or set them to the snooze mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><CopyableCode code="alarm_model_description" /></td><td><code>string</code></td><td>A brief description of the alarm model.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.<br />This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.<br /></td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>object</code></td><td>Defines when your alarm is invoked.</td></tr>
<tr><td><CopyableCode code="alarm_event_actions" /></td><td><code>object</code></td><td>Contains information about one or more alarm actions.</td></tr>
<tr><td><CopyableCode code="alarm_capabilities" /></td><td><code>object</code></td><td>Contains the configuration information of alarm state changes</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.<br />For more information, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
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
Lists all <code>alarm_models</code> in a region.
```sql
SELECT
region,
alarm_model_name
FROM aws.iotevents.alarm_models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>alarm_models_list_only</code> resource, see <a href="/providers/aws/iotevents/alarm_models/#permissions"><code>alarm_models</code></a>


