---
title: ipam_pool_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool_cidrs
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
<tr><td><b>Name</b></td><td><code>ipam_pool_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_pool_cidrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cidr` | `string` | The CIDR provisioned to the IPAM pool. A CIDR is a representation of an IP address and its associated network mask (or netmask) and refers to a range of IP addresses. An IPv4 CIDR example is &lt;code&gt;10.24.34.0/23&lt;/code&gt;. An IPv6 CIDR example is &lt;code&gt;2001:DB8::/32&lt;/code&gt;. |
| `failureReason` | `object` | Details related to why an IPAM pool CIDR failed to be provisioned. |
| `state` | `string` | The state of the CIDR. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_pool_cidrs_Get` | `SELECT` | `IpamPoolId` | Get the CIDRs provisioned to an IPAM pool. |
| `ipam_pool_cidr_Allocate` | `EXEC` | `IpamPoolId` | Allocate a CIDR from an IPAM pool. In IPAM, an allocation is a CIDR assignment from an IPAM pool to another resource or IPAM pool. For more information, see &lt;a href="/vpc/latest/ipam/allocate-cidrs-ipam.html"&gt;Allocate CIDRs&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
| `ipam_pool_cidr_Deprovision` | `EXEC` | `IpamPoolId` | Deprovision a CIDR provisioned from an IPAM pool. If you deprovision a CIDR from a pool that has a source pool, the CIDR is recycled back into the source pool. For more information, see &lt;a href="/vpc/latest/ipam/depro-pool-cidr-ipam.html"&gt;Deprovision pool CIDRs&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `ipam_pool_cidr_Provision` | `EXEC` | `IpamPoolId` | &lt;p&gt;Provision a CIDR to an IPAM pool. You can use this action to provision new CIDRs to a top-level pool or to transfer a CIDR from a top-level pool to a pool within it.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/prov-cidr-ipam.html"&gt;Provision CIDRs to pools&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
