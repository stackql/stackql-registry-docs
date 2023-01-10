---
title: session_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - session_hosts
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>session_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.desktop_virtualization.session_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Schema for SessionHost properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SessionHosts_Get` | `SELECT` | `hostPoolName, resourceGroupName, sessionHostName, subscriptionId` | Get a session host. |
| `SessionHosts_List` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` | List sessionHosts. |
| `SessionHosts_Delete` | `DELETE` | `hostPoolName, resourceGroupName, sessionHostName, subscriptionId` | Remove a SessionHost. |
| `SessionHosts_Update` | `EXEC` | `hostPoolName, resourceGroupName, sessionHostName, subscriptionId` | Update a session host. |
