---
title: application_group
hide_title: false
hide_table_of_contents: false
keywords:
  - application_group
  - event_hub
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
<tr><td><b>Name</b></td><td><code>application_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.application_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationGroup_Get` | `SELECT` | `applicationGroupName, namespaceName, resourceGroupName, subscriptionId` | Gets an ApplicationGroup for a Namespace. |
| `ApplicationGroup_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets a list of application groups for a Namespace. |
| `ApplicationGroup_Delete` | `DELETE` | `applicationGroupName, namespaceName, resourceGroupName, subscriptionId` | Deletes an ApplicationGroup for a Namespace. |
| `ApplicationGroup_CreateOrUpdateApplicationGroup` | `EXEC` | `applicationGroupName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an ApplicationGroup for a Namespace. |
