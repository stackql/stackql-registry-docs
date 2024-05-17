---
title: local_gateway_virtual_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_virtual_interfaces
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
<tr><td><b>Name</b></td><td><code>local_gateway_virtual_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.local_gateway_virtual_interfaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="localAddress" /> | `string` | The local address. |
| <CopyableCode code="localBgpAsn" /> | `integer` | The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway. |
| <CopyableCode code="localGatewayId" /> | `string` | The ID of the local gateway. |
| <CopyableCode code="localGatewayVirtualInterfaceId" /> | `string` | The ID of the virtual interface. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the local gateway virtual interface. |
| <CopyableCode code="peerAddress" /> | `string` | The peer address. |
| <CopyableCode code="peerBgpAsn" /> | `integer` | The peer BGP ASN. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the virtual interface. |
| <CopyableCode code="vlan" /> | `integer` | The ID of the VLAN. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="local_gateway_virtual_interfaces_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
