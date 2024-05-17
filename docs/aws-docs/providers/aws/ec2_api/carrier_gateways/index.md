---
title: carrier_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateways
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
<tr><td><b>Name</b></td><td><code>carrier_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.carrier_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="carrierGatewayId" /> | `string` | The ID of the carrier gateway. |
| <CopyableCode code="ownerId" /> | `string` | The Amazon Web Services account ID of the owner of the carrier gateway. |
| <CopyableCode code="state" /> | `string` | The state of the carrier gateway. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the carrier gateway. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC associated with the carrier gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="carrier_gateways_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your carrier gateways. |
| <CopyableCode code="carrier_gateway_Create" /> | `INSERT` | <CopyableCode code="VpcId, region" /> | Creates a carrier gateway. For more information about carrier gateways, see &lt;a href="https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#wavelength-carrier-gateway"&gt;Carrier gateways&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Wavelength Developer Guide&lt;/i&gt;. |
| <CopyableCode code="carrier_gateway_Delete" /> | `DELETE` | <CopyableCode code="CarrierGatewayId, region" /> | &lt;p&gt;Deletes a carrier gateway.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you do not delete the route that contains the carrier gateway as the Target, the route is a blackhole route. For information about how to delete a route, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html"&gt;DeleteRoute&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; |
