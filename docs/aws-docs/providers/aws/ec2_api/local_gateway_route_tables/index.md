---
title: local_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tables
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
<tr><td><b>Name</b></td><td><code>local_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.local_gateway_route_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localGatewayId" /> | `string` | The ID of the local gateway. |
| <CopyableCode code="localGatewayRouteTableArn" /> | `string` | The Amazon Resource Name (ARN) of the local gateway route table. |
| <CopyableCode code="localGatewayRouteTableId" /> | `string` | The ID of the local gateway route table. |
| <CopyableCode code="outpostArn" /> | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the local gateway route table. |
| <CopyableCode code="state" /> | `string` | The state of the local gateway route table. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the local gateway route table. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="local_gateway_route_tables_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
