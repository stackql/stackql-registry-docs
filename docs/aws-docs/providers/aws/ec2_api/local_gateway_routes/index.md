---
title: local_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_routes
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
<tr><td><b>Name</b></td><td><code>local_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.local_gateway_routes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="local_gateway_route_Create" /> | `INSERT` | <CopyableCode code="DestinationCidrBlock, LocalGatewayRouteTableId, LocalGatewayVirtualInterfaceGroupId, region" /> | Creates a static route for the specified local gateway route table. |
| <CopyableCode code="local_gateway_route_Delete" /> | `DELETE` | <CopyableCode code="DestinationCidrBlock, LocalGatewayRouteTableId, region" /> | Deletes the specified route from the specified local gateway route table. |
| <CopyableCode code="local_gateway_routes_Search" /> | `EXEC` | <CopyableCode code="LocalGatewayRouteTableId, region" /> | Searches for routes in the specified local gateway route table. |
