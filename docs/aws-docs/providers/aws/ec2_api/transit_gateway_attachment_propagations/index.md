---
title: transit_gateway_attachment_propagations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_attachment_propagations
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
<tr><td><b>Name</b></td><td><code>transit_gateway_attachment_propagations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_attachment_propagations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="state" /> | `string` | The state of the propagation route table. |
| <CopyableCode code="transitGatewayRouteTableId" /> | `string` | The ID of the propagation route table. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="transit_gateway_attachment_propagations_Get" /> | `SELECT` | <CopyableCode code="TransitGatewayAttachmentId, region" /> |
