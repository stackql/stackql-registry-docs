---
title: wcf_relays
hide_title: false
hide_table_of_contents: false
keywords:
  - wcf_relays
  - relay
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>wcf_relays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.relay.wcf_relays</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties of the WCF relay. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WCFRelays_Get` | `SELECT` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Returns the description for the specified WCF relay. |
| `WCFRelays_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Lists the WCF relays within the namespace. |
| `WCFRelays_CreateOrUpdate` | `INSERT` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Creates or updates a WCF relay. This operation is idempotent. |
| `WCFRelays_Delete` | `DELETE` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Deletes a WCF relay. |
| `WCFRelays_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId` | Creates or updates an authorization rule for a WCF relay. |
| `WCFRelays_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId` | Deletes a WCF relay authorization rule. |
| `WCFRelays_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId` | Get authorizationRule for a WCF relay by name. |
| `WCFRelays_ListAuthorizationRules` | `EXEC` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Authorization rules for a WCF relay. |
| `WCFRelays_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId` | Primary and secondary connection strings to the WCF relay. |
| `WCFRelays_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the WCF relay. |
