---
title: local_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateways
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
<tr><td><b>Name</b></td><td><code>local_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.local_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localGatewayId" /> | `string` | The ID of the local gateway. |
| <CopyableCode code="outpostArn" /> | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the local gateway. |
| <CopyableCode code="state" /> | `string` | The state of the local gateway. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the local gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="local_gateways_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
