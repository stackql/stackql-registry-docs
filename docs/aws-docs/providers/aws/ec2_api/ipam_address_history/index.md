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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_address_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.ipam_address_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceCidr" /> | `string` | The CIDR of the resource. |
| <CopyableCode code="resourceComplianceStatus" /> | `string` | The compliance status of a resource. For more information on compliance statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| <CopyableCode code="resourceId" /> | `string` | The ID of the resource. |
| <CopyableCode code="resourceName" /> | `string` | The name of the resource. |
| <CopyableCode code="resourceOverlapStatus" /> | `string` | The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see &lt;a href="/vpc/latest/ipam/monitor-cidr-compliance-ipam.html"&gt;Monitor CIDR usage by resource&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. |
| <CopyableCode code="resourceOwnerId" /> | `string` | The ID of the resource owner. |
| <CopyableCode code="resourceRegion" /> | `string` | The Amazon Web Services Region of the resource. |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource. |
| <CopyableCode code="sampledEndTime" /> | `string` | Sampled end time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the end time may have occurred before this specific time. |
| <CopyableCode code="sampledStartTime" /> | `string` | Sampled start time of the resource-to-CIDR association within the IPAM scope. Changes are picked up in periodic snapshots, so the start time may have occurred before this specific time. |
| <CopyableCode code="vpcId" /> | `string` | The VPC ID of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="ipam_address_history_Get" /> | `SELECT` | <CopyableCode code="Cidr, IpamScopeId, region" /> |
