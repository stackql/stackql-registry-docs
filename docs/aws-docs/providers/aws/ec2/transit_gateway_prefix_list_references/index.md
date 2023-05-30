---
title: transit_gateway_prefix_list_references
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_prefix_list_references
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
<tr><td><b>Name</b></td><td><code>transit_gateway_prefix_list_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_prefix_list_references</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transitGatewayAttachment` | `object` | Describes a transit gateway prefix list attachment. |
| `transitGatewayRouteTableId` | `string` | The ID of the transit gateway route table. |
| `blackhole` | `boolean` | Indicates whether traffic that matches this route is dropped. |
| `prefixListId` | `string` | The ID of the prefix list. |
| `prefixListOwnerId` | `string` | The ID of the prefix list owner. |
| `state` | `string` | The state of the prefix list reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_prefix_list_references_Get` | `SELECT` | `TransitGatewayRouteTableId, region` | Gets information about the prefix list references in a specified transit gateway route table. |
| `transit_gateway_prefix_list_reference_Create` | `INSERT` | `PrefixListId, TransitGatewayRouteTableId, region` | Creates a reference (route) to a prefix list in a specified transit gateway route table. |
| `transit_gateway_prefix_list_reference_Delete` | `DELETE` | `PrefixListId, TransitGatewayRouteTableId, region` | Deletes a reference (route) to a prefix list in a specified transit gateway route table. |
| `transit_gateway_prefix_list_reference_Modify` | `EXEC` | `PrefixListId, TransitGatewayRouteTableId, region` | Modifies a reference (route) to a prefix list in a specified transit gateway route table. |
