---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
Retrieves a list of <code>devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.networkmanager.devices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DeviceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the device.</td></tr>
<tr><td><code>DeviceId</code></td><td><code>string</code></td><td>The ID of the device.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the device.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags for the device.</td></tr>
<tr><td><code>GlobalNetworkId</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>Location</code></td><td><code>undefined</code></td><td>The site location.</td></tr>
<tr><td><code>Model</code></td><td><code>string</code></td><td>The device model</td></tr>
<tr><td><code>SerialNumber</code></td><td><code>string</code></td><td>The device serial number.</td></tr>
<tr><td><code>SiteId</code></td><td><code>string</code></td><td>The site ID.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The device type.</td></tr>
<tr><td><code>Vendor</code></td><td><code>string</code></td><td>The device vendor.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.networkmanager.devices
WHERE region = 'us-east-1'
</pre>
