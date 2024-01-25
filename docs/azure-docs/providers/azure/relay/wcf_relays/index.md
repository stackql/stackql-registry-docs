---
title: wcf_relays
hide_title: false
hide_table_of_contents: false
keywords:
  - wcf_relays
  - relay
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
<tr><td><b>Name</b></td><td><code>wcf_relays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.relay.wcf_relays</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties of the WCF relay. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Returns the description for the specified WCF relay. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Lists the WCF relays within the namespace. |
| `create_or_update` | `INSERT` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Creates or updates a WCF relay. This operation is idempotent. |
| `delete` | `DELETE` | `namespaceName, relayName, resourceGroupName, subscriptionId` | Deletes a WCF relay. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Lists the WCF relays within the namespace. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the WCF relay. |
