---
title: public_ipv4_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ipv4_pools
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
<tr><td><b>Name</b></td><td><code>public_ipv4_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.public_ipv4_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the address pool. |
| `networkBorderGroup` | `string` | The name of the location from which the address pool is advertised. A network border group is a unique set of Availability Zones or Local Zones from where Amazon Web Services advertises public IP addresses. |
| `poolAddressRangeSet` | `array` | The address ranges. |
| `poolId` | `string` | The ID of the address pool. |
| `tagSet` | `array` | Any tags for the address pool. |
| `totalAddressCount` | `integer` | The total number of addresses. |
| `totalAvailableAddressCount` | `integer` | The total number of available addresses. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `public_ipv4_pools_Describe` | `SELECT` | `region` | Describes the specified IPv4 address pools. |
| `public_ipv4_pool_Create` | `INSERT` | `region` | Creates a public IPv4 address pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses you bring to Amazon Web Services, however, use IPAM pools only. To monitor the status of pool creation, use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribePublicIpv4Pools.html"&gt;DescribePublicIpv4Pools&lt;/a&gt;. |
| `public_ipv4_pool_Delete` | `DELETE` | `PoolId, region` | Delete a public IPv4 pool. A public IPv4 pool is an EC2 IP address pool required for the public IPv4 CIDRs that you own and bring to Amazon Web Services to manage with IPAM. IPv6 addresses you bring to Amazon Web Services, however, use IPAM pools only. |
