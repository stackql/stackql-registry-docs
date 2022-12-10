---
title: transit_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_tables
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
<tr><td><b>Name</b></td><td><code>transit_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | The creation time. |
| `defaultAssociationRouteTable` | `boolean` | Indicates whether this is the default association route table for the transit gateway. |
| `defaultPropagationRouteTable` | `boolean` | Indicates whether this is the default propagation route table for the transit gateway. |
| `state` | `string` | The state of the transit gateway route table. |
| `tagSet` | `array` | Any tags assigned to the route table. |
| `transitGatewayId` | `string` | The ID of the transit gateway. |
| `transitGatewayRouteTableId` | `string` | The ID of the transit gateway route table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_route_tables_Describe` | `SELECT` |  | Describes one or more transit gateway route tables. By default, all transit gateway route tables are described. Alternatively, you can filter the results. |
| `transit_gateway_route_table_Create` | `INSERT` | `TransitGatewayId` | Creates a route table for the specified transit gateway. |
| `transit_gateway_route_table_Delete` | `DELETE` | `TransitGatewayRouteTableId` | Deletes the specified transit gateway route table. You must disassociate the route table from any transit gateway route tables before you can delete it. |
| `transit_gateway_route_table_Associate` | `EXEC` | `TransitGatewayAttachmentId, TransitGatewayRouteTableId` | Associates the specified attachment with the specified transit gateway route table. You can associate only one route table with an attachment. |
| `transit_gateway_route_table_Disassociate` | `EXEC` | `TransitGatewayAttachmentId, TransitGatewayRouteTableId` | Disassociates a resource attachment from a transit gateway route table. |
