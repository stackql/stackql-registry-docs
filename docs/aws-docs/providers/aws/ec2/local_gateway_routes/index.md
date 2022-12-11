---
title: local_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_routes
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
<tr><td><b>Name</b></td><td><code>local_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_routes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `local_gateway_route_Create` | `INSERT` | `DestinationCidrBlock, LocalGatewayRouteTableId, LocalGatewayVirtualInterfaceGroupId` | Creates a static route for the specified local gateway route table. |
| `local_gateway_route_Delete` | `DELETE` | `DestinationCidrBlock, LocalGatewayRouteTableId` | Deletes the specified route from the specified local gateway route table. |
| `local_gateway_routes_Search` | `EXEC` | `LocalGatewayRouteTableId` | Searches for routes in the specified local gateway route table. |
