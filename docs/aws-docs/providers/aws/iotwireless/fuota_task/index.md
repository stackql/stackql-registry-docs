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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>fuota_task</code> resource, use <code>fuota_tasks</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage FUOTA tasks.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.fuota_task" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of FUOTA task</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>FUOTA task description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>FUOTA task LoRaWAN</td></tr>
<tr><td><CopyableCode code="firmware_update_image" /></td><td><code>string</code></td><td>FUOTA task firmware update image binary S3 link</td></tr>
<tr><td><CopyableCode code="firmware_update_role" /></td><td><code>string</code></td><td>FUOTA task firmware IAM role for reading S3</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>FUOTA task arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the FUOTA task.</td></tr>
<tr><td><CopyableCode code="fuota_task_status" /></td><td><code>string</code></td><td>FUOTA task status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
<tr><td><CopyableCode code="associate_multicast_group" /></td><td><code>string</code></td><td>Multicast group to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_multicast_group" /></td><td><code>string</code></td><td>Multicast group to disassociate. Only for update request.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.iotwireless.fuota_task
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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

