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
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.wireless_devices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>wireless_devices</code> resource, the following permissions are required:

### Create
<pre>
iotwireless:CreateWirelessDevice,
iotwireless:TagResource,
iotwireless:ListTagsForResource</pre>

### List
<pre>
iotwireless:ListWirelessDevices,
iotwireless:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.iotwireless.wireless_devices
WHERE region = 'us-east-1'
```
