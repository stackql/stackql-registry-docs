---
title: alarm_model_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - alarm_model_tags
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

Expands all tag keys and values for <code>alarm_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alarm_model_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an alarm model to monitor an ITE input attribute. You can use the alarm to get notified when the value is outside a specified range. For more information, see &#91;Create an alarm model&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.alarm_model_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alarm_model_name" /></td><td><code>string</code></td><td>The name of the alarm model.</td></tr>
<tr><td><CopyableCode code="alarm_model_description" /></td><td><code>string</code></td><td>The description of the alarm model.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see &#91;Amazon Resource Names (ARNs)&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>An input attribute used as a key to create an alarm. ITE routes &#91;inputs&#93;(https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html) associated with this key to the alarm.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>integer</code></td><td>A non-negative integer that reflects the severity level of the alarm.</td></tr>
<tr><td><CopyableCode code="alarm_rule" /></td><td><code>object</code></td><td>Defines when your alarm is invoked.</td></tr>
<tr><td><CopyableCode code="alarm_event_actions" /></td><td><code>object</code></td><td>Contains information about one or more alarm actions.</td></tr>
<tr><td><CopyableCode code="alarm_capabilities" /></td><td><code>object</code></td><td>Contains the configuration information of alarm state changes.</td></tr>
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
Expands tags for all <code>alarm_models</code> in a region.
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
tag_key,
tag_value
FROM aws.iotevents.alarm_model_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>alarm_model_tags</code> resource, see <a href="/providers/aws/iotevents/alarm_models/#permissions"><code>alarm_models</code></a>

