---
title: ipam_resource_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_cidrs
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
<tr><td><b>Name</b></td><td><code>ipam_resource_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_resource_cidrs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `overlapStatus` | `string` | The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `ipamScopeId` | `string` | The scope ID for an IPAM resource. |
| `resourceTagSet` | `array` | The tags for an IPAM resource. |
| `resourceId` | `string` | The ID of an IPAM resource. |
| `complianceStatus` | `string` | The compliance status of the IPAM resource. For more information on compliance statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `ipamId` | `string` | The IPAM ID for an IPAM resource. |
| `resourceName` | `string` | The name of an IPAM resource. |
| `vpcId` | `string` | The ID of a VPC. |
| `resourceOwnerId` | `string` | The Amazon Web Services account number of the owner of an IPAM resource. |
| `resourceType` | `string` | The type of IPAM resource. |
| `resourceCidr` | `string` | The CIDR for an IPAM resource. |
| `ipamPoolId` | `string` | The pool ID for an IPAM resource. |
| `resourceRegion` | `string` | The Amazon Web Services Region for an IPAM resource. |
| `managementState` | `string` | The management state of the resource. For more information about management states, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `ipUsage` | `number` | The IP address space in the IPAM pool that is allocated to this resource. To convert the decimal to a percentage, multiply the decimal by 100. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_resource_cidrs_Get` | `SELECT` | `IpamScopeId` | Get information about the resources in a scope. |
| `ipam_resource_cidr_Modify` | `EXEC` | `CurrentIpamScopeId, Monitored, ResourceCidr, ResourceId, ResourceRegion` | &lt;p&gt;Modify a resource CIDR. You can use this action to transfer resource CIDRs between scopes and ignore resource CIDRs that you do not want to manage. If set to false, the resource will not be tracked for overlap, it cannot be auto-imported into a pool, and it will be removed from any pool it has an allocation in.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/move-resource-ipam.html"&gt;Move resource CIDRs between scopes&lt;/a&gt; and &lt;a href="/vpc/latest/ipam/change-monitoring-state-ipam.html"&gt;Change the monitoring state of resource CIDRs&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
