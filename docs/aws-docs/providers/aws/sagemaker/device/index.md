---
title: device
hide_title: false
hide_table_of_contents: false
keywords:
  - device
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>device</code> resource, use <code>devices</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::Device</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.device</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>device_fleet_name</code></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><code>device</code></td><td><code>object</code></td><td>The Edge Device you want to register against a device fleet</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Associate tags with the resource</td></tr>
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
device_fleet_name,
device,
tags
FROM aws.sagemaker.device
WHERE data__Identifier = '<Device/DeviceName>';
```

## Permissions

To operate on the <code>device</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeDevice
```

### Update
```json
sagemaker:UpdateDevices
```

### Delete
```json
sagemaker:DeregisterDevices
```

