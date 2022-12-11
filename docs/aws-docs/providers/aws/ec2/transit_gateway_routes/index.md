---
title: transit_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_routes
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
<tr><td><b>Name</b></td><td><code>transit_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_routes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_route_Create` | `INSERT` | `DestinationCidrBlock, TransitGatewayRouteTableId` | Creates a static route for the specified transit gateway route table. |
| `transit_gateway_route_Delete` | `DELETE` | `DestinationCidrBlock, TransitGatewayRouteTableId` | Deletes the specified route from the specified transit gateway route table. |
| `transit_gateway_route_Replace` | `EXEC` | `DestinationCidrBlock, TransitGatewayRouteTableId` | Replaces the specified route in the specified transit gateway route table. |
| `transit_gateway_routes_Export` | `EXEC` | `S3Bucket, TransitGatewayRouteTableId` | &lt;p&gt;Exports routes from the specified transit gateway route table to the specified S3 bucket. By default, all routes are exported. Alternatively, you can filter by CIDR range.&lt;/p&gt; &lt;p&gt;The routes are saved to the specified bucket in a JSON file. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#tgw-export-route-tables"&gt;Export Route Tables to Amazon S3&lt;/a&gt; in &lt;i&gt;Transit Gateways&lt;/i&gt;.&lt;/p&gt; |
| `transit_gateway_routes_Search` | `EXEC` | `Filter, TransitGatewayRouteTableId` | Searches for routes in the specified transit gateway route table. |
