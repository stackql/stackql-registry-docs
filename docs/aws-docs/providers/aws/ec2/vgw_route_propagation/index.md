---
title: vgw_route_propagation
hide_title: false
hide_table_of_contents: false
keywords:
  - vgw_route_propagation
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
<tr><td><b>Name</b></td><td><code>vgw_route_propagation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vgw_route_propagation</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vgw_route_propagation_Disable` | `EXEC` | `GatewayId, RouteTableId` | Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC. |
| `vgw_route_propagation_Enable` | `EXEC` | `GatewayId, RouteTableId` | Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC. |
