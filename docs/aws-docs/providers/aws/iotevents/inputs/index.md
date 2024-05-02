---
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
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
Retrieves a list of <code>inputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see &#91;How to Use AWS IoT Events&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;iotevents&#x2F;latest&#x2F;developerguide&#x2F;how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotevents.inputs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>input_name</code></td><td><code>string</code></td><td>The name of the input.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
input_name
FROM aws.iotevents.inputs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>inputs</code> resource, the following permissions are required:

### Create
```json
iotevents:CreateInput,
iotevents:TagResource,
iotevents:DescribeInput,
iotevents:ListTagsForResource
```

### List
```json
iotevents:ListInputs
```

