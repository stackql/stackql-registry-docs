---
title: detector_model
hide_title: false
hide_table_of_contents: false
keywords:
  - detector_model
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
Gets an individual <code>detector_model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector_model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>detector_model</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotevents.detector_model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>detector_model_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>detector_model_description</code></td><td><code>string</code></td><td>A brief description of the detector model.</td></tr>
<tr><td><code>detector_model_name</code></td><td><code>string</code></td><td>The name of the detector model.</td></tr>
<tr><td><code>evaluation_method</code></td><td><code>string</code></td><td>Information about the order in which events are evaluated and how actions are executed.</td></tr>
<tr><td><code>key</code></td><td><code>string</code></td><td>The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
detector_model_definition,
detector_model_description,
detector_model_name,
evaluation_method,
key,
role_arn,
tags
FROM aws.iotevents.detector_model
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DetectorModelName&gt;'
```
