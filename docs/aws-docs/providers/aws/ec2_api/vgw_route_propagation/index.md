---
title: vgw_route_propagation
hide_title: false
hide_table_of_contents: false
keywords:
  - vgw_route_propagation
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
<tr><td><b>Name</b></td><td><code>vgw_route_propagation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vgw_route_propagation" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vgw_route_propagation_Disable" /> | `EXEC` | <CopyableCode code="GatewayId, RouteTableId, region" /> | Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC. |
| <CopyableCode code="vgw_route_propagation_Enable" /> | `EXEC` | <CopyableCode code="GatewayId, RouteTableId, region" /> | Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC. |
