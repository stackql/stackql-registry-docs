---
title: wireless_device_import_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_device_import_tasks
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
Retrieves a list of <code>wireless_device_import_tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device_import_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wireless_device_import_tasks</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.wireless_device_import_tasks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id for Wireless Device Import Task, Returned upon successful start.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.iotwireless.wireless_device_import_tasks
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>wireless_device_import_tasks</code> resource, the following permissions are required:

### Create
```json
iotwireless:StartWirelessDeviceImportTask,
iotwireless:StartSingleWirelessDeviceImportTask,
iotwireless:TagResource,
iotwireless:ListTagsForResource,
iam:PassRole
```

### List
```json
iotwireless:ListWirelessDeviceImportTasks,
iotwireless:ListTagsForResource
```

