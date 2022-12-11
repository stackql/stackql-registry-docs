---
title: ipam_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pools
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
<tr><td><b>Name</b></td><td><code>ipam_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the IPAM pool. |
| `allocationMinNetmaskLength` | `integer` | The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128. |
| `ipamRegion` | `string` | The Amazon Web Services Region of the IPAM pool. |
| `ipamScopeType` | `string` | In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict. |
| `locale` | `string` | The locale of the IPAM pool. In IPAM, the locale is the Amazon Web Services Region where you want to make an IPAM pool available for allocations. Only resources in the same Region as the locale of the pool can get IP address allocations from the pool. You can only allocate a CIDR for a VPC, for example, from an IPAM pool that shares a locale with the VPC’s Region. Note that once you choose a Locale for a pool, you cannot modify it. If you choose an Amazon Web Services Region for locale that has not been configured as an operating Region for the IPAM, you'll get an error. |
| `tagSet` | `array` | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key &lt;code&gt;Owner&lt;/code&gt; and the value &lt;code&gt;TeamA&lt;/code&gt;, specify &lt;code&gt;tag:Owner&lt;/code&gt; for the filter name and &lt;code&gt;TeamA&lt;/code&gt; for the filter value. |
| `allocationResourceTagSet` | `array` | Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant. |
| `awsService` | `string` | Limits which service in Amazon Web Services that the pool can be used in. "ec2", for example, allows users to use space for Elastic IP addresses and VPCs. |
| `autoImport` | `boolean` | &lt;p&gt;If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. &lt;/p&gt; &lt;p&gt;A locale must be set on the pool for this feature to work.&lt;/p&gt; |
| `sourceIpamPoolId` | `string` | The ID of the source IPAM pool. You can use this option to create an IPAM pool within an existing source pool. |
| `addressFamily` | `string` | The address family of the pool. |
| `allocationDefaultNetmaskLength` | `integer` | The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16. |
| `ipamPoolArn` | `string` | The ARN of the IPAM pool. |
| `ipamScopeArn` | `string` | The ARN of the scope of the IPAM pool. |
| `poolDepth` | `integer` | The depth of pools in your IPAM pool. The pool depth quota is 10. For more information, see &lt;a href="/vpc/latest/ipam/quotas-ipam.html"&gt;Quotas in IPAM&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
| `allocationMaxNetmaskLength` | `integer` | The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the IPAM pool. |
| `publiclyAdvertisable` | `boolean` | Determines if a pool is publicly advertisable. This option is not available for pools with AddressFamily set to &lt;code&gt;ipv4&lt;/code&gt;. |
| `ipamArn` | `string` | The ARN of the IPAM. |
| `ipamPoolId` | `string` | The ID of the IPAM pool. |
| `stateMessage` | `string` | A message related to the failed creation of an IPAM pool. |
| `state` | `string` | The state of the IPAM pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_pools_Describe` | `SELECT` |  | Get information about your IPAM pools. |
| `ipam_pool_Create` | `INSERT` | `AddressFamily, IpamScopeId` | &lt;p&gt;Create an IP address pool for Amazon VPC IP Address Manager (IPAM). In IPAM, a pool is a collection of contiguous IP addresses CIDRs. Pools enable you to organize your IP addresses according to your routing and security needs. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/create-top-ipam.html"&gt;Create a top-level pool&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_pool_Delete` | `DELETE` | `IpamPoolId` | &lt;p&gt;Delete an IPAM pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot delete an IPAM pool if there are allocations in it or CIDRs provisioned to it. To release allocations, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReleaseIpamPoolAllocation.html"&gt;ReleaseIpamPoolAllocation&lt;/a&gt;. To deprovision pool CIDRs, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeprovisionIpamPoolCidr.html"&gt;DeprovisionIpamPoolCidr&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/delete-pool-ipam.html"&gt;Delete a pool&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_pool_Modify` | `EXEC` | `IpamPoolId` | &lt;p&gt;Modify the configurations of an IPAM pool.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/mod-pool-ipam.html"&gt;Modify a pool&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
