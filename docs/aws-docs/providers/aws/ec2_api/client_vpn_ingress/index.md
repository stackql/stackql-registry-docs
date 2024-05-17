---
title: client_vpn_ingress
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_ingress
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
<tr><td><b>Name</b></td><td><code>client_vpn_ingress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.client_vpn_ingress" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="client_vpn_ingress_Authorize" /> | `EXEC` | <CopyableCode code="ClientVpnEndpointId, TargetNetworkCidr, region" /> | Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in Amazon Web Services or on-premises networks. |
| <CopyableCode code="client_vpn_ingress_Revoke" /> | `EXEC` | <CopyableCode code="ClientVpnEndpointId, TargetNetworkCidr, region" /> | Removes an ingress authorization rule from a Client VPN endpoint.  |
