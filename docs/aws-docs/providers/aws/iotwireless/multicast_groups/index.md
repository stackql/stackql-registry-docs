---
title: multicast_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - multicast_groups
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
Retrieves a list of <code>multicast_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multicast_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multicast_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.multicast_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of Multicast group</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Multicast group description</td></tr>
<tr><td><code>LoRaWAN</code></td><td><code>undefined</code></td><td>Multicast group LoRaWAN</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Multicast group arn. Returned after successful create.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Multicast group id. Returned after successful create.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the Multicast group.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>Multicast group status. Returned after successful read.</td></tr>
<tr><td><code>AssociateWirelessDevice</code></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><code>DisassociateWirelessDevice</code></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotwireless.multicast_groups
WHERE region = 'us-east-1'
</pre>
