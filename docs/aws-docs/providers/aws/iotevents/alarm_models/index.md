---
title: alarm_models
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_models
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
Retrieves a list of <code>alarm_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>alarm_models</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotevents.alarm_models</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AlarmModelName</code></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><code>AlarmModelDescription</code></td><td><code>string</code></td><td>A brief description of the alarm model.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><code>Key</code></td><td><code>string</code></td><td>The value used to identify a alarm instance. When a device or system sends input, a new alarm instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding alarm instance based on this identifying information.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct alarm instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><code>Severity</code></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>AlarmRule</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AlarmEventActions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AlarmCapabilities</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iotevents.alarm_models<br/>WHERE region = 'us-east-1'
</pre>
