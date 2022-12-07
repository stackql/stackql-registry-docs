---
title: coip_pool_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - coip_pool_usage
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
<tr><td><b>Name</b></td><td><code>coip_pool_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.coip_pool_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `awsService` | `string` | The Amazon Web Services service. |
| `coIp` | `string` | The customer-owned IP address. |
| `allocationId` | `string` | The allocation ID of the address. |
| `awsAccountId` | `string` | The Amazon Web Services account ID. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `coip_pool_usage_Get` | `SELECT` | `PoolId` |
