---
title: local_gateway_route_table_virtual_interface_group_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_table_virtual_interface_group_associations
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_virtual_interface_group_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_route_table_virtual_interface_group_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | The tags assigned to the association. |
| `localGatewayId` | `string` | The ID of the local gateway. |
| `localGatewayRouteTableArn` | `string` | The Amazon Resource Name (ARN) of the local gateway route table for the virtual interface group. |
| `localGatewayRouteTableId` | `string` | The ID of the local gateway route table. |
| `localGatewayRouteTableVirtualInterfaceGroupAssociationId` | `string` | The ID of the association. |
| `localGatewayVirtualInterfaceGroupId` | `string` | The ID of the virtual interface group. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the local gateway virtual interface group association. |
| `state` | `string` | The state of the association. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `local_gateway_route_table_virtual_interface_group_associations_Describe` | `SELECT` |  |
