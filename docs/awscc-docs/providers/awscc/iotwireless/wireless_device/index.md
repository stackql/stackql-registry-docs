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
Gets an individual <code>wireless_device</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wireless_device</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.wireless_device</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Wireless device type, currently only Sidewalk and LoRa</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Wireless device name</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Wireless device description</td></tr>
<tr><td><code>destination_name</code></td><td><code>string</code></td><td>Wireless device destination name</td></tr>
<tr><td><code>lo_ra_wa_n</code></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Wireless device arn. Returned after successful create.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><code>thing_arn</code></td><td><code>string</code></td><td>Thing arn. Passed into update to associate Thing with Wireless device.</td></tr>
<tr><td><code>thing_name</code></td><td><code>string</code></td><td>Thing Arn. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><code>last_uplink_received_at</code></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><code>positioning</code></td><td><code>string</code></td><td>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
name,
description,
destination_name,
lo_ra_wa_n,
tags,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at,
positioning
FROM awscc.iotwireless.wireless_device
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
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

### Delete
```json
iotwireless:DeleteWirelessDevice,
iotwireless:DisassociateWirelessDeviceFromThing
```

