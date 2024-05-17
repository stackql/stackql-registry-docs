---
title: transit_gateway_route_table_propagations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_propagations
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
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_propagations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_route_table_propagations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceId" /> | `string` | The ID of the resource. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource. Note that the &lt;code&gt;tgw-peering&lt;/code&gt; resource type has been deprecated. |
| <CopyableCode code="state" /> | `string` | The state of the resource. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_route_table_propagations_Get" /> | `SELECT` | <CopyableCode code="TransitGatewayRouteTableId, region" /> | Gets information about the route table propagations for the specified transit gateway route table. |
| <CopyableCode code="transit_gateway_route_table_propagation_Disable" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, TransitGatewayRouteTableId, region" /> | Disables the specified resource attachment from propagating routes to the specified propagation route table. |
| <CopyableCode code="transit_gateway_route_table_propagation_Enable" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, TransitGatewayRouteTableId, region" /> | Enables the specified attachment to propagate routes to the specified propagation route table. |
