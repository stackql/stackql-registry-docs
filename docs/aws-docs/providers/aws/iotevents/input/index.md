---
title: input
hide_title: false
hide_table_of_contents: false
keywords:
  - input
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
Gets or operates on an individual <code>input</code> resource, use <code>inputs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see &#91;How to Use AWS IoT Events&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iotevents&#x2F;latest&#x2F;developerguide&#x2F;how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotevents.input</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>input_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>input_description</code></td><td><code>string</code></td><td>A brief description of the input.</td></tr>
<tr><td><code>input_name</code></td><td><code>string</code></td><td>The name of the input.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
input_definition,
input_description,
input_name,
tags
FROM aws.iotevents.input
WHERE data__Identifier = '<InputName>';
```

## Permissions

To operate on the <code>input</code> resource, the following permissions are required:

### Read
```json
iotevents:DescribeInput,
iotevents:ListTagsForResource
```

### Update
```json
iotevents:UpdateInput,
iotevents:DescribeInput,
iotevents:ListTagsForResource,
iotevents:UntagResource,
iotevents:TagResource
```

### Delete
```json
iotevents:DeleteInput,
iotevents:DescribeInput
```

