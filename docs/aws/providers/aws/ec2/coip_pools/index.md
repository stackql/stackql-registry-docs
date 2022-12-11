---
title: coip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - coip_pools
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
<tr><td><b>Name</b></td><td><code>coip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.coip_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | The tags. |
| `localGatewayRouteTableId` | `string` | The ID of the local gateway route table. |
| `poolArn` | `string` | The ARN of the address pool. |
| `poolCidrSet` | `array` | The address ranges of the address pool. |
| `poolId` | `string` | The ID of the address pool. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `coip_pools_Describe` | `SELECT` |  |
