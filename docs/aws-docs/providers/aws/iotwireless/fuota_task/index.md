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
Gets an individual <code>fuota_task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.fuota_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of FUOTA task</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>FUOTA task description</td></tr><tr><td><code>LoRaWAN</code></td><td><code>undefined</code></td><td>FUOTA task LoRaWAN</td></tr><tr><td><code>FirmwareUpdateImage</code></td><td><code>string</code></td><td>FUOTA task firmware update image binary S3 link</td></tr><tr><td><code>FirmwareUpdateRole</code></td><td><code>string</code></td><td>FUOTA task firmware IAM role for reading S3</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>FUOTA task arn. Returned after successful create.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the FUOTA task.</td></tr><tr><td><code>FuotaTaskStatus</code></td><td><code>string</code></td><td>FUOTA task status. Returned after successful read.</td></tr><tr><td><code>AssociateWirelessDevice</code></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr><tr><td><code>DisassociateWirelessDevice</code></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr><tr><td><code>AssociateMulticastGroup</code></td><td><code>string</code></td><td>Multicast group to associate. Only for update request.</td></tr><tr><td><code>DisassociateMulticastGroup</code></td><td><code>string</code></td><td>Multicast group to disassociate. Only for update request.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.iotwireless.fuota_task
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
