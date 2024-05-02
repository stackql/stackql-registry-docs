---
title: coip_pool_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - coip_pool_usage
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>coip_pool_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.coip_pool_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `allocationId` | `string` | The allocation ID of the address. |
| `awsAccountId` | `string` | The Amazon Web Services account ID. |
| `awsService` | `string` | The Amazon Web Services service. |
| `coIp` | `string` | The customer-owned IP address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `coip_pool_usage_Get` | `SELECT` | `PoolId, region` |
