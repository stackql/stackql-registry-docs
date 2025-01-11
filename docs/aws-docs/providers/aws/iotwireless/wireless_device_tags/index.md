---
title: wireless_device_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_device_tags
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

Expands all tag keys and values for <code>wireless_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_device_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Wireless device type, currently only Sidewalk and LoRa</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Wireless device name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Wireless device description</td></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>Wireless device destination name</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Wireless device arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="thing_arn" /></td><td><code>string</code></td><td>Thing arn. Passed into update to associate Thing with Wireless device.</td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td>Thing Arn. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><CopyableCode code="last_uplink_received_at" /></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><CopyableCode code="positioning" /></td><td><code>string</code></td><td>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>wireless_devices</code> in a region.
```sql
SELECT
region,
type,
name,
description,
destination_name,
lo_ra_wan,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at,
positioning,
tag_key,
tag_value
FROM aws.iotwireless.wireless_device_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>wireless_device_tags</code> resource, see <a href="/providers/aws/iotwireless/wireless_devices/#permissions"><code>wireless_devices</code></a>

