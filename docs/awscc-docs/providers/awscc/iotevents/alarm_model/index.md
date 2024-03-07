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
Gets an individual <code>alarm_model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alarm_model</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotevents.alarm_model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alarm_model_name</code></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><code>alarm_model_description</code></td><td><code>string</code></td><td>A brief description of the alarm model.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><code>key</code></td><td><code>string</code></td><td>The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><code>severity</code></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>alarm_rule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>alarm_event_actions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>alarm_capabilities</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### Delete
```json
iotevents:DeleteAlarmModel,
iotevents:DescribeAlarmModel
```


## Example
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
FROM awscc.iotevents.alarm_model
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AlarmModelName&gt;'
```
