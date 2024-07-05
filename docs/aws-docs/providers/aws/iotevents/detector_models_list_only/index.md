---
title: detector_models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - detector_models_list_only
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

Lists <code>detector_models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/detector_models/"><code>detector_models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector_models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see &#91;How to Use AWS IoT Events&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.detector_models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="detector_model_definition" /></td><td><code>object</code></td><td>Information that defines how a detector operates.</td></tr>
<tr><td><CopyableCode code="detector_model_description" /></td><td><code>string</code></td><td>A brief description of the detector model.</td></tr>
<tr><td><CopyableCode code="detector_model_name" /></td><td><code>string</code></td><td>The name of the detector model.</td></tr>
<tr><td><CopyableCode code="evaluation_method" /></td><td><code>string</code></td><td>Information about the order in which events are evaluated and how actions are executed.</td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.<br />This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
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
Lists all <code>detector_models</code> in a region.
```sql
SELECT
region,
detector_model_name
FROM aws.iotevents.detector_models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>detector_models_list_only</code> resource, see <a href="/providers/aws/iotevents/detector_models/#permissions"><code>detector_models</code></a>


