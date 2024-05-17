---
title: transit_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_tables
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
<tr><td><b>Name</b></td><td><code>transit_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_route_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | The creation time. |
| <CopyableCode code="defaultAssociationRouteTable" /> | `boolean` | Indicates whether this is the default association route table for the transit gateway. |
| <CopyableCode code="defaultPropagationRouteTable" /> | `boolean` | Indicates whether this is the default propagation route table for the transit gateway. |
| <CopyableCode code="state" /> | `string` | The state of the transit gateway route table. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the route table. |
| <CopyableCode code="transitGatewayId" /> | `string` | The ID of the transit gateway. |
| <CopyableCode code="transitGatewayRouteTableId" /> | `string` | The ID of the transit gateway route table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_route_tables_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more transit gateway route tables. By default, all transit gateway route tables are described. Alternatively, you can filter the results. |
| <CopyableCode code="transit_gateway_route_table_Create" /> | `INSERT` | <CopyableCode code="TransitGatewayId, region" /> | Creates a route table for the specified transit gateway. |
| <CopyableCode code="transit_gateway_route_table_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayRouteTableId, region" /> | Deletes the specified transit gateway route table. You must disassociate the route table from any transit gateway route tables before you can delete it. |
| <CopyableCode code="transit_gateway_route_table_Associate" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, TransitGatewayRouteTableId, region" /> | Associates the specified attachment with the specified transit gateway route table. You can associate only one route table with an attachment. |
| <CopyableCode code="transit_gateway_route_table_Disassociate" /> | `EXEC` | <CopyableCode code="TransitGatewayAttachmentId, TransitGatewayRouteTableId, region" /> | Disassociates a resource attachment from a transit gateway route table. |
