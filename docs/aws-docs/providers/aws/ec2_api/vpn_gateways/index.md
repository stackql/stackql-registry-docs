---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpn_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="amazonSideAsn" /> | `integer` | The private Autonomous System Number (ASN) for the Amazon side of a BGP session. |
| <CopyableCode code="attachments" /> | `array` | Any VPCs attached to the virtual private gateway. |
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned. |
| <CopyableCode code="state" /> | `string` | The current state of the virtual private gateway. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the virtual private gateway. |
| <CopyableCode code="type" /> | `string` | The type of VPN connection the virtual private gateway supports. |
| <CopyableCode code="vpnGatewayId" /> | `string` | The ID of the virtual private gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpn_gateways_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes one or more of your virtual private gateways.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="vpn_gateway_Create" /> | `INSERT` | <CopyableCode code="Type, region" /> | &lt;p&gt;Creates a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="vpn_gateway_Delete" /> | `DELETE` | <CopyableCode code="VpnGatewayId, region" /> | Deletes the specified virtual private gateway. You must first detach the virtual private gateway from the VPC. Note that you don't need to delete the virtual private gateway if you plan to delete and recreate the VPN connection between your VPC and your network. |
| <CopyableCode code="vpn_gateway_Attach" /> | `EXEC` | <CopyableCode code="VpcId, VpnGatewayId, region" /> | &lt;p&gt;Attaches a virtual private gateway to a VPC. You can attach one virtual private gateway to one VPC at a time.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="vpn_gateway_Detach" /> | `EXEC` | <CopyableCode code="VpcId, VpnGatewayId, region" /> | &lt;p&gt;Detaches a virtual private gateway from a VPC. You do this if you're planning to turn off the VPC and not use it anymore. You can confirm a virtual private gateway has been completely detached from a VPC by describing the virtual private gateway (any attachments to the virtual private gateway are also described).&lt;/p&gt; &lt;p&gt;You must wait for the attachment's state to switch to &lt;code&gt;detached&lt;/code&gt; before you can delete the VPC or attach a different VPC to the virtual private gateway.&lt;/p&gt; |
