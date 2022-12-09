---
title: transit_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateways
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
<tr><td><b>Name</b></td><td><code>transit_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the transit gateway. |
| `options` | `object` | Describes the options for a transit gateway. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the transit gateway. |
| `state` | `string` | The state of the transit gateway. |
| `tagSet` | `array` | The tags for the transit gateway. |
| `transitGatewayArn` | `string` | The Amazon Resource Name (ARN) of the transit gateway. |
| `transitGatewayId` | `string` | The ID of the transit gateway. |
| `creationTime` | `string` | The creation time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateways_Describe` | `SELECT` |  | Describes one or more transit gateways. By default, all transit gateways are described. Alternatively, you can filter the results. |
| `transit_gateway_Create` | `INSERT` |  | &lt;p&gt;Creates a transit gateway.&lt;/p&gt; &lt;p&gt;You can use a transit gateway to interconnect your virtual private clouds (VPC) and on-premises networks. After the transit gateway enters the &lt;code&gt;available&lt;/code&gt; state, you can attach your VPCs and VPN connections to the transit gateway.&lt;/p&gt; &lt;p&gt;To attach your VPCs, use &lt;a&gt;CreateTransitGatewayVpcAttachment&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To attach a VPN connection, use &lt;a&gt;CreateCustomerGateway&lt;/a&gt; to create a customer gateway and specify the ID of the customer gateway and the ID of the transit gateway in a call to &lt;a&gt;CreateVpnConnection&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When you create a transit gateway, we create a default transit gateway route table and use it as the default association route table and the default propagation route table. You can use &lt;a&gt;CreateTransitGatewayRouteTable&lt;/a&gt; to create additional transit gateway route tables. If you disable automatic route propagation, we do not create a default transit gateway route table. You can use &lt;a&gt;EnableTransitGatewayRouteTablePropagation&lt;/a&gt; to propagate routes from a resource attachment to a transit gateway route table. If you disable automatic associations, you can use &lt;a&gt;AssociateTransitGatewayRouteTable&lt;/a&gt; to associate a resource attachment with a transit gateway route table.&lt;/p&gt; |
| `transit_gateway_Delete` | `DELETE` | `TransitGatewayId` | Deletes the specified transit gateway. |
| `transit_gateway_Modify` | `EXEC` | `TransitGatewayId` | Modifies the specified transit gateway. When you modify a transit gateway, the modified options are applied to new transit gateway attachments only. Your existing transit gateway attachments are not modified. |
