---
title: coip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - coip_pools
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
<tr><td><b>Name</b></td><td><code>coip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.coip_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localGatewayRouteTableId" /> | `string` | The ID of the local gateway route table. |
| <CopyableCode code="poolArn" /> | `string` | The ARN of the address pool. |
| <CopyableCode code="poolCidrSet" /> | `array` | The address ranges of the address pool. |
| <CopyableCode code="poolId" /> | `string` | The ID of the address pool. |
| <CopyableCode code="tagSet" /> | `array` | The tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="coip_pools_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
