---
title: local_gateway_virtual_interface_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_virtual_interface_groups
  - ec2
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
<tr><td><b>Name</b></td><td><code>local_gateway_virtual_interface_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_virtual_interface_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `localGatewayId` | `string` | The ID of the local gateway. |
| `localGatewayVirtualInterfaceGroupId` | `string` | The ID of the virtual interface group. |
| `localGatewayVirtualInterfaceIdSet` | `array` | The IDs of the virtual interfaces. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the local gateway virtual interface group. |
| `tagSet` | `array` | The tags assigned to the virtual interface group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `local_gateway_virtual_interface_groups_Describe` | `SELECT` | `region` |
