---
title: ipam_pool_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool_allocations
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
<tr><td><b>Name</b></td><td><code>ipam_pool_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_pool_allocations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the pool allocation. |
| `cidr` | `string` | The CIDR for the allocation. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is &lt;code&gt;10.24.34.0/23&lt;/code&gt;. An IPv6 CIDR example is &lt;code&gt;2001:DB8::/32&lt;/code&gt;. |
| `ipamPoolAllocationId` | `string` | The ID of an allocation. |
| `resourceId` | `string` | The ID of the resource. |
| `resourceOwner` | `string` | The owner of the resource. |
| `resourceRegion` | `string` | The Amazon Web Services Region of the resource. |
| `resourceType` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_pool_allocations_Get` | `SELECT` | `IpamPoolId` | Get a list of all the CIDR allocations in an IPAM pool. |
| `ipam_pool_allocation_Release` | `EXEC` | `Cidr, IpamPoolAllocationId, IpamPoolId` | Release an allocation within an IPAM pool. You can only use this action to release manual allocations. To remove an allocation for a resource without deleting the resource, set its monitored state to false using &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamResourceCidr.html"&gt;ModifyIpamResourceCidr&lt;/a&gt;. For more information, see &lt;a href="/vpc/latest/ipam/release-pool-alloc-ipam.html"&gt;Release an allocation&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
