---
title: ipam_resource_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_cidrs
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.ipam_resource_cidrs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="complianceStatus" /> | `string` | The compliance status of the IPAM resource. For more information on compliance statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| <CopyableCode code="ipUsage" /> | `number` | The IP address space in the IPAM pool that is allocated to this resource. To convert the decimal to a percentage, multiply the decimal by 100. |
| <CopyableCode code="ipamId" /> | `string` | The IPAM ID for an IPAM resource. |
| <CopyableCode code="ipamPoolId" /> | `string` | The pool ID for an IPAM resource. |
| <CopyableCode code="ipamScopeId" /> | `string` | The scope ID for an IPAM resource. |
| <CopyableCode code="managementState" /> | `string` | The management state of the resource. For more information about management states, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| <CopyableCode code="overlapStatus" /> | `string` | The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| <CopyableCode code="resourceCidr" /> | `string` | The CIDR for an IPAM resource. |
| <CopyableCode code="resourceId" /> | `string` | The ID of an IPAM resource. |
| <CopyableCode code="resourceName" /> | `string` | The name of an IPAM resource. |
| <CopyableCode code="resourceOwnerId" /> | `string` | The Amazon Web Services account number of the owner of an IPAM resource. |
| <CopyableCode code="resourceRegion" /> | `string` | The Amazon Web Services Region for an IPAM resource. |
| <CopyableCode code="resourceTagSet" /> | `array` | The tags for an IPAM resource. |
| <CopyableCode code="resourceType" /> | `string` | The type of IPAM resource. |
| <CopyableCode code="vpcId" /> | `string` | The ID of a VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="ipam_resource_cidrs_Get" /> | `SELECT` | <CopyableCode code="IpamScopeId, region" /> | Get information about the resources in a scope. |
| <CopyableCode code="ipam_resource_cidr_Modify" /> | `EXEC` | <CopyableCode code="CurrentIpamScopeId, Monitored, ResourceCidr, ResourceId, ResourceRegion, region" /> | &lt;p&gt;Modify a resource CIDR. You can use this action to transfer resource CIDRs between scopes and ignore resource CIDRs that you do not want to manage. If set to false, the resource will not be tracked for overlap, it cannot be auto-imported into a pool, and it will be removed from any pool it has an allocation in.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/move-resource-ipam.html"&gt;Move resource CIDRs between scopes&lt;/a&gt; and &lt;a href="/vpc/latest/ipam/change-monitoring-state-ipam.html"&gt;Change the monitoring state of resource CIDRs&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
