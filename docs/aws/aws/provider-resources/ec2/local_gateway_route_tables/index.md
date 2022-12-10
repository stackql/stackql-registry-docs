---
title: local_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tables
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
<tr><td><b>Name</b></td><td><code>local_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `localGatewayRouteTableArn` | `string` | The Amazon Resource Name (ARN) of the local gateway route table. |
| `localGatewayRouteTableId` | `string` | The ID of the local gateway route table. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the local gateway route table. |
| `state` | `string` | The state of the local gateway route table. |
| `tagSet` | `array` | The tags assigned to the local gateway route table. |
| `localGatewayId` | `string` | The ID of the local gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `local_gateway_route_tables_Describe` | `SELECT` |  |
