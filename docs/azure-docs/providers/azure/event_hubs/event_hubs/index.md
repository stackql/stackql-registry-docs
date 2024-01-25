---
title: event_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_hubs
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>event_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hubs.event_hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `` | Properties supplied to the Create Or Update Event Hub operation. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `eventHubName, namespaceName, resourceGroupName, subscriptionId` | Gets an Event Hubs description for the specified Event Hub. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the Event Hubs in a Namespace. |
| `create_or_update` | `INSERT` | `eventHubName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates a new Event Hub as a nested resource within a Namespace. |
| `delete` | `DELETE` | `eventHubName, namespaceName, resourceGroupName, subscriptionId` | Deletes an Event Hub from the specified Namespace and resource group. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets all the Event Hubs in a Namespace. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the ACS and SAS connection strings for the Event Hub. |
