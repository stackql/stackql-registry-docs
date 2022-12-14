---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| `origin` | `string` | Origin of the operation. |
| `properties` | `object` | Description of operation properties format. |
| `display` | `` | Display metadata associated with the operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Operations_List` | `SELECT` |  | Lists all of the available Network Rest API operations. |
| `CheckDnsNameAvailability` | `EXEC` | `domainNameLabel, location, subscriptionId` | Checks whether a domain name in the cloudapp.azure.com zone is available for use. |
| `SupportedSecurityProviders` | `EXEC` | `resourceGroupName, subscriptionId, virtualWANName` | Gives the supported security providers for the virtual wan. |
| `generatevirtualwanvpnserverconfigurationvpnprofile` | `EXEC` | `resourceGroupName, subscriptionId, virtualWANName` | Generates a unique VPN profile for P2S clients for VirtualWan and associated VpnServerConfiguration combination in the specified resource group. |
