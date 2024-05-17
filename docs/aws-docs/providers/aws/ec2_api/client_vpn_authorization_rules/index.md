---
title: client_vpn_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_authorization_rules
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
<tr><td><b>Name</b></td><td><code>client_vpn_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.client_vpn_authorization_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A brief description of the authorization rule. |
| <CopyableCode code="accessAll" /> | `boolean` | Indicates whether the authorization rule grants access to all clients. |
| <CopyableCode code="clientVpnEndpointId" /> | `string` | The ID of the Client VPN endpoint with which the authorization rule is associated. |
| <CopyableCode code="destinationCidr" /> | `string` | The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies. |
| <CopyableCode code="groupId" /> | `string` | The ID of the Active Directory group to which the authorization rule grants access. |
| <CopyableCode code="status" /> | `object` | Describes the state of an authorization rule. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="client_vpn_authorization_rules_Describe" /> | `SELECT` | <CopyableCode code="ClientVpnEndpointId, region" /> |
