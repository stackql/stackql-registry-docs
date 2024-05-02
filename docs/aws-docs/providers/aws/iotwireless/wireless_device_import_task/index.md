---
title: wireless_device_import_task
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_device_import_task
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>wireless_device_import_task</code> resource, use <code>wireless_device_import_tasks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device_import_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Wireless Device Import Tasks</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.wireless_device_import_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id for Wireless Device Import Task, Returned upon successful start.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn for Wireless Device Import Task, Returned upon successful start.</td></tr>
<tr><td><code>destination_name</code></td><td><code>string</code></td><td>Destination Name for import task</td></tr>
<tr><td><code>creation_date</code></td><td><code>string</code></td><td>CreationDate for import task</td></tr>
<tr><td><code>sidewalk</code></td><td><code>object</code></td><td>sidewalk contain file for created device and role</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Status for import task</td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td>StatusReason for import task</td></tr>
<tr><td><code>initialized_imported_devices_count</code></td><td><code>integer</code></td><td>Initialized Imported Devices Count</td></tr>
<tr><td><code>pending_imported_devices_count</code></td><td><code>integer</code></td><td>Pending Imported Devices Count</td></tr>
<tr><td><code>onboarded_imported_devices_count</code></td><td><code>integer</code></td><td>Onboarded Imported Devices Count</td></tr>
<tr><td><code>failed_imported_devices_count</code></td><td><code>integer</code></td><td>Failed Imported Devices Count</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
id,
arn,
destination_name,
creation_date,
sidewalk,
status,
status_reason,
initialized_imported_devices_count,
pending_imported_devices_count,
onboarded_imported_devices_count,
failed_imported_devices_count,
tags
FROM aws.iotwireless.wireless_device_import_task
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>wireless_device_import_task</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetWirelessDeviceImportTask,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateWirelessDeviceImportTask,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iam:PassRole
```

### Delete
```json
iotwireless:DeleteWirelessDeviceImportTask
```

