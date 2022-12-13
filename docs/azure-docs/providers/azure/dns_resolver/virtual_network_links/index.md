---
title: virtual_network_links
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_links
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>virtual_network_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.virtual_network_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the virtual network link. |
| `properties` | `object` | Represents the properties of a virtual network link. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkLinks_Get` | `SELECT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Gets properties of a virtual network link to a DNS forwarding ruleset. |
| `VirtualNetworkLinks_List` | `SELECT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Lists virtual network links to a DNS forwarding ruleset. |
| `VirtualNetworkLinks_CreateOrUpdate` | `INSERT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName, data__properties` | Creates or updates a virtual network link to a DNS forwarding ruleset. |
| `VirtualNetworkLinks_Delete` | `DELETE` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Deletes a virtual network link to a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| `VirtualNetworkLinks_Update` | `EXEC` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName` | Updates a virtual network link to a DNS forwarding ruleset. |
