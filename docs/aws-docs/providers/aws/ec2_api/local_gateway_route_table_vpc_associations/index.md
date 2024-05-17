---
title: local_gateway_route_table_vpc_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_table_vpc_associations
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
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_vpc_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.local_gateway_route_table_vpc_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localGatewayId" /> | `string` | The ID of the local gateway. |
| <CopyableCode code="localGatewayRouteTableArn" /> | `string` | The Amazon Resource Name (ARN) of the local gateway route table for the association. |
| <CopyableCode code="localGatewayRouteTableId" /> | `string` | The ID of the local gateway route table. |
| <CopyableCode code="localGatewayRouteTableVpcAssociationId" /> | `string` | The ID of the association. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the local gateway route table for the association. |
| <CopyableCode code="state" /> | `string` | The state of the association. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the association. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="local_gateway_route_table_vpc_associations_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the specified associations between VPCs and local gateway route tables. |
| <CopyableCode code="local_gateway_route_table_vpc_association_Create" /> | `INSERT` | <CopyableCode code="LocalGatewayRouteTableId, VpcId, region" /> | Associates the specified VPC with the specified local gateway route table. |
| <CopyableCode code="local_gateway_route_table_vpc_association_Delete" /> | `DELETE` | <CopyableCode code="LocalGatewayRouteTableVpcAssociationId, region" /> | Deletes the specified association between a VPC and local gateway route table. |
