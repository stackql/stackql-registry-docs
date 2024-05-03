---
title: multicast_group
hide_title: false
hide_table_of_contents: false
keywords:
  - multicast_group
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

Gets or operates on an individual <code>multicast_group</code> resource, use <code>multicast_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multicast_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage Multicast groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.multicast_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Multicast group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Multicast group description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>Multicast group LoRaWAN</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Multicast group arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Multicast group id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the Multicast group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Multicast group status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
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
name,
description,
lo_ra_wan,
arn,
id,
tags,
status,
associate_wireless_device,
disassociate_wireless_device
FROM aws.iotwireless.multicast_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>multicast_group</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetMulticastGroup,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateMulticastGroup,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iotwireless:AssociateWirelessDeviceWithMulticastGroup,
iotwireless:DisassociateWirelessDeviceFromMulticastGroup
```

### Delete
```json
iotwireless:DeleteMulticastGroup
```

