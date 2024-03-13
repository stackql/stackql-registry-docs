---
title: fuota_task
hide_title: false
hide_table_of_contents: false
keywords:
  - fuota_task
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
Gets an individual <code>fuota_task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fuota_task</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.fuota_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of FUOTA task</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>FUOTA task description</td></tr>
<tr><td><code>lo_ra_wan</code></td><td><code>object</code></td><td>FUOTA task LoRaWAN</td></tr>
<tr><td><code>firmware_update_image</code></td><td><code>string</code></td><td>FUOTA task firmware update image binary S3 link</td></tr>
<tr><td><code>firmware_update_role</code></td><td><code>string</code></td><td>FUOTA task firmware IAM role for reading S3</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>FUOTA task arn. Returned after successful create.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the FUOTA task.</td></tr>
<tr><td><code>fuota_task_status</code></td><td><code>string</code></td><td>FUOTA task status. Returned after successful read.</td></tr>
<tr><td><code>associate_wireless_device</code></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><code>disassociate_wireless_device</code></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
<tr><td><code>associate_multicast_group</code></td><td><code>string</code></td><td>Multicast group to associate. Only for update request.</td></tr>
<tr><td><code>disassociate_multicast_group</code></td><td><code>string</code></td><td>Multicast group to disassociate. Only for update request.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
lo_ra_wan,
firmware_update_image,
firmware_update_role,
arn,
id,
tags,
fuota_task_status,
associate_wireless_device,
disassociate_wireless_device,
associate_multicast_group,
disassociate_multicast_group
FROM awscc.iotwireless.fuota_task
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>fuota_task</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetFuotaTask,
iotwireless:ListTagsForResource
```

### Update
```json
iam:PassRole,
iotwireless:UpdateFuotaTask,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iotwireless:AssociateMulticastGroupWithFuotaTask,
iotwireless:DisassociateMulticastGroupFromFuotaTask,
iotwireless:AssociateWirelessDeviceWithFuotaTask,
iotwireless:DisassociateWirelessDeviceFromFuotaTask
```

### Delete
```json
iotwireless:DeleteFuotaTask
```

