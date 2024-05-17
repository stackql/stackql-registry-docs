---
title: transit_gateway_prefix_list_references
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_prefix_list_references
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
<tr><td><b>Name</b></td><td><code>transit_gateway_prefix_list_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_prefix_list_references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blackhole" /> | `boolean` | Indicates whether traffic that matches this route is dropped. |
| <CopyableCode code="prefixListId" /> | `string` | The ID of the prefix list. |
| <CopyableCode code="prefixListOwnerId" /> | `string` | The ID of the prefix list owner. |
| <CopyableCode code="state" /> | `string` | The state of the prefix list reference. |
| <CopyableCode code="transitGatewayAttachment" /> | `object` | Describes a transit gateway prefix list attachment. |
| <CopyableCode code="transitGatewayRouteTableId" /> | `string` | The ID of the transit gateway route table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_prefix_list_references_Get" /> | `SELECT` | <CopyableCode code="TransitGatewayRouteTableId, region" /> | Gets information about the prefix list references in a specified transit gateway route table. |
| <CopyableCode code="transit_gateway_prefix_list_reference_Create" /> | `INSERT` | <CopyableCode code="PrefixListId, TransitGatewayRouteTableId, region" /> | Creates a reference (route) to a prefix list in a specified transit gateway route table. |
| <CopyableCode code="transit_gateway_prefix_list_reference_Delete" /> | `DELETE` | <CopyableCode code="PrefixListId, TransitGatewayRouteTableId, region" /> | Deletes a reference (route) to a prefix list in a specified transit gateway route table. |
| <CopyableCode code="transit_gateway_prefix_list_reference_Modify" /> | `EXEC` | <CopyableCode code="PrefixListId, TransitGatewayRouteTableId, region" /> | Modifies a reference (route) to a prefix list in a specified transit gateway route table. |
