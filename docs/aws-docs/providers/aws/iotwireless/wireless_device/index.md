---
title: wireless_device
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_device
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


Gets or updates an individual <code>wireless_device</code> resource, use <code>wireless_devices</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_device" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Wireless device type, currently only Sidewalk and LoRa</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Wireless device name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Wireless device description</td></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>Wireless device destination name</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Wireless device arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="thing_arn" /></td><td><code>string</code></td><td>Thing arn. Passed into update to associate Thing with Wireless device.</td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td>Thing Arn. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><CopyableCode code="last_uplink_received_at" /></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><CopyableCode code="positioning" /></td><td><code>string</code></td><td>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</td></tr>
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
type,
name,
description,
destination_name,
lo_ra_wan,
tags,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at,
positioning
FROM aws.iotwireless.wireless_device
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>wireless_device</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetWirelessDevice,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateWirelessDevice,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iotwireless:AssociateWirelessDeviceWithThing
```

