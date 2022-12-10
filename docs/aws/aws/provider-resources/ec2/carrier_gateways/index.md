---
title: carrier_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateways
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>carrier_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.carrier_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | The tags assigned to the carrier gateway. |
| `vpcId` | `string` | The ID of the VPC associated with the carrier gateway. |
| `carrierGatewayId` | `string` | The ID of the carrier gateway. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the carrier gateway. |
| `state` | `string` | The state of the carrier gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `carrier_gateways_Describe` | `SELECT` |  | Describes one or more of your carrier gateways. |
| `carrier_gateway_Create` | `INSERT` | `VpcId` | Creates a carrier gateway. For more information about carrier gateways, see &lt;a href="https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html#wavelength-carrier-gateway"&gt;Carrier gateways&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Wavelength Developer Guide&lt;/i&gt;. |
| `carrier_gateway_Delete` | `DELETE` | `CarrierGatewayId` | &lt;p&gt;Deletes a carrier gateway.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you do not delete the route that contains the carrier gateway as the Target, the route is a blackhole route. For information about how to delete a route, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html"&gt;DeleteRoute&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; |
