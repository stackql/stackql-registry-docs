---
title: wireless_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_gateways
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
Retrieves a list of <code>wireless_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wireless_gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.wireless_gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>wireless_gateways</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessGateway,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### List
```json
iotwireless:ListWirelessGateways,
iotwireless:ListTagsForResource
```


## Example
```sql
SELECT
region,
id
FROM awscc.iotwireless.wireless_gateways
WHERE region = 'us-east-1'
```
