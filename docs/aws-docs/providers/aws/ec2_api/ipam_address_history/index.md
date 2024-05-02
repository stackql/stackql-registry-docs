---
title: ipam_address_history
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_address_history
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
<tr><td><b>Name</b></td><td><code>ipam_address_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.ipam_address_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceCidr` | `string` | The CIDR of the resource. |
| `resourceComplianceStatus` | `string` | The compliance status of a resource. For more information on compliance statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `resourceId` | `string` | The ID of the resource. |
| `resourceName` | `string` | The name of the resource. |
| `resourceOverlapStatus` | `string` | The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| `resourceOwnerId` | `string` | The ID of the resource owner. |
| `resourceRegion` | `string` | The Amazon Web Services Region of the resource. |
| `resourceType` | `string` | The type of the resource. |
| `sampledEndTime` | `string` | Sampled end time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the end time may have occurred before this specific time. |
| `sampledStartTime` | `string` | Sampled start time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the start time may have occurred before this specific time. |
| `vpcId` | `string` | The VPC ID of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ipam_address_history_Get` | `SELECT` | `Cidr, IpamScopeId, region` |
