---
title: transit_gateway_route_table_propagations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_propagations
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
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_propagations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_route_table_propagations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceType` | `string` | The type of resource. Note that the &lt;code&gt;tgw-peering&lt;/code&gt; resource type has been deprecated. |
| `state` | `string` | The state of the resource. |
| `transitGatewayAttachmentId` | `string` | The ID of the attachment. |
| `resourceId` | `string` | The ID of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_route_table_propagations_Get` | `SELECT` | `TransitGatewayRouteTableId` | Gets information about the route table propagations for the specified transit gateway route table. |
| `transit_gateway_route_table_propagation_Disable` | `EXEC` | `TransitGatewayAttachmentId, TransitGatewayRouteTableId` | Disables the specified resource attachment from propagating routes to the specified propagation route table. |
| `transit_gateway_route_table_propagation_Enable` | `EXEC` | `TransitGatewayAttachmentId, TransitGatewayRouteTableId` | Enables the specified attachment to propagate routes to the specified propagation route table. |
