---
title: associated_ipv6_pool_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - associated_ipv6_pool_cidrs
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
<tr><td><b>Name</b></td><td><code>associated_ipv6_pool_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.associated_ipv6_pool_cidrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `associatedResource` | `string` | The resource that's associated with the IPv6 CIDR block. |
| `ipv6Cidr` | `string` | The IPv6 CIDR block. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `associated_ipv6_pool_cidrs_Get` | `SELECT` | `PoolId` |
