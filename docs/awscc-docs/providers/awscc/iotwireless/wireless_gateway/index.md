---
title: wireless_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_gateway
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
Gets an individual <code>wireless_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wireless_gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.wireless_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of Wireless Gateway.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of Wireless Gateway.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><code>lo_ra_wa_n</code></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><code>thing_arn</code></td><td><code>string</code></td><td>Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.</td></tr>
<tr><td><code>thing_name</code></td><td><code>string</code></td><td>Thing Name. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><code>last_uplink_received_at</code></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>wireless_gateway</code> resource, the following permissions are required:

### Read
<pre>
iotwireless:GetWirelessGateway,
iotwireless:ListTagsForResource</pre>

### Update
<pre>
iotwireless:UpdateWirelessGateway,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iotwireless:AssociateWirelessGatewayWithThing</pre>

### Delete
<pre>
iotwireless:DeleteWirelessGateway,
iotwireless:DisassociateWirelessGatewayFromThing</pre>


## Example
```sql
SELECT
region,
name,
description,
tags,
lo_ra_wa_n,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at
FROM awscc.iotwireless.wireless_gateway
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
