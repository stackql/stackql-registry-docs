---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - data_factory
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | Azure data factory nested object which contains information about creating pipeline run |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Triggers_Get` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Gets a trigger. |
| `Triggers_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists triggers. |
| `Triggers_CreateOrUpdate` | `INSERT` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName, data__properties` | Creates or updates a trigger. |
| `Triggers_Delete` | `DELETE` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Deletes a trigger. |
| `Triggers_GetEventSubscriptionStatus` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Get a trigger's event subscription status. |
| `Triggers_QueryByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Query triggers. |
| `Triggers_Start` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Starts a trigger. |
| `Triggers_Stop` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Stops a trigger. |
| `Triggers_SubscribeToEvents` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Subscribe event trigger to events. |
| `Triggers_UnsubscribeFromEvents` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Unsubscribe event trigger from events. |
