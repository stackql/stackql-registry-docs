---
title: device
hide_title: false
hide_table_of_contents: false
keywords:
  - device
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>device</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>device</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.device</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>device_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the device.</td></tr>
<tr><td><code>device_id</code></td><td><code>string</code></td><td>The ID of the device.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the device.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the device.</td></tr>
<tr><td><code>global_network_id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>location</code></td><td><code>object</code></td><td>The site location.</td></tr>
<tr><td><code>model</code></td><td><code>string</code></td><td>The device model</td></tr>
<tr><td><code>serial_number</code></td><td><code>string</code></td><td>The device serial number.</td></tr>
<tr><td><code>site_id</code></td><td><code>string</code></td><td>The site ID.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The device type.</td></tr>
<tr><td><code>vendor</code></td><td><code>string</code></td><td>The device vendor.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
device_arn,
device_id,
description,
tags,
global_network_id,
location,
model,
serial_number,
site_id,
type,
vendor
FROM aws.networkmanager.device
WHERE region = 'us-east-1'
AND data__Identifier = '<GlobalNetworkId>'
AND data__Identifier = '<DeviceId>'
```
