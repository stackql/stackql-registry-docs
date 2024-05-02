---
title: vpn_connection_device_types
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_device_types
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection_device_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.vpn_connection_device_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `platform` | `string` | Customer gateway device platform. |
| `software` | `string` | Customer gateway device software version. |
| `vendor` | `string` | Customer gateway device vendor. |
| `vpnConnectionDeviceTypeId` | `string` | Customer gateway device identifier. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `vpn_connection_device_types_Get` | `SELECT` | `region` |
