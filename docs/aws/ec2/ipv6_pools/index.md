---
title: ipv6_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ipv6_pools
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
<tr><td><b>Name</b></td><td><code>ipv6_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipv6_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description for the address pool. |
| `poolCidrBlockSet` | `array` | The CIDR blocks for the address pool. |
| `poolId` | `string` | The ID of the address pool. |
| `tagSet` | `array` | Any tags for the address pool. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ipv6_pools_Describe` | `SELECT` |  |
