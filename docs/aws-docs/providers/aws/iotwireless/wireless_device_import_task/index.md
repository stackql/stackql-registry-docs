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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>wireless_device_import_task</code> resource, use <code>wireless_device_import_tasks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device_import_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Wireless Device Import Tasks</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_device_import_task" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for Wireless Device Import Task, Returned upon successful start.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn for Wireless Device Import Task, Returned upon successful start.</td></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>Destination Name for import task</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>CreationDate for import task</td></tr>
<tr><td><CopyableCode code="sidewalk" /></td><td><code>object</code></td><td>sidewalk contain file for created device and role</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status for import task</td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td>StatusReason for import task</td></tr>
<tr><td><CopyableCode code="initialized_imported_devices_count" /></td><td><code>integer</code></td><td>Initialized Imported Devices Count</td></tr>
<tr><td><CopyableCode code="pending_imported_devices_count" /></td><td><code>integer</code></td><td>Pending Imported Devices Count</td></tr>
<tr><td><CopyableCode code="onboarded_imported_devices_count" /></td><td><code>integer</code></td><td>Onboarded Imported Devices Count</td></tr>
<tr><td><CopyableCode code="failed_imported_devices_count" /></td><td><code>integer</code></td><td>Failed Imported Devices Count</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

