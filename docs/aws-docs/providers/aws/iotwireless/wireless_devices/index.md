---
title: wireless_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_devices
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
Retrieves a list of <code>wireless_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wireless_devices</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.wireless_devices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>Wireless device type, currently only Sidewalk and LoRa</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Wireless device name</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Wireless device description</td></tr>
<tr><td><code>DestinationName</code></td><td><code>string</code></td><td>Wireless device destination name</td></tr>
<tr><td><code>LoRaWAN</code></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Wireless device arn. Returned after successful create.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><code>ThingArn</code></td><td><code>string</code></td><td>Thing arn. Passed into update to associate Thing with Wireless device.</td></tr>
<tr><td><code>ThingName</code></td><td><code>string</code></td><td>Thing Arn. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><code>LastUplinkReceivedAt</code></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iotwireless.wireless_devices<br/>WHERE region = 'us-east-1'
</pre>
