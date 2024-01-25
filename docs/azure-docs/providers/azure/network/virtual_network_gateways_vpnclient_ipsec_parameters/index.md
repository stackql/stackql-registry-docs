---
title: virtual_network_gateways_vpnclient_ipsec_parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_vpnclient_ipsec_parameters
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_gateways_vpnclient_ipsec_parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateways_vpnclient_ipsec_parameters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dhGroup` | `string` | The DH Groups used in IKE Phase 1 for initial SA. |
| `ikeEncryption` | `string` | The IKE encryption algorithm (IKE phase 2). |
| `ikeIntegrity` | `string` | The IKE integrity algorithm (IKE phase 2). |
| `ipsecEncryption` | `string` | The IPSec encryption algorithm (IKE phase 1). |
| `ipsecIntegrity` | `string` | The IPSec integrity algorithm (IKE phase 1). |
| `pfsGroup` | `string` | The Pfs Groups used in IKE Phase 2 for new child SA. |
| `saDataSizeKilobytes` | `integer` | The IPSec Security Association (also called Quick Mode or Phase 2 SA) payload size in KB for P2S client.. |
| `saLifeTimeSeconds` | `integer` | The IPSec Security Association (also called Quick Mode or Phase 2 SA) lifetime in seconds for P2S client. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` |
