---
title: event_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - event_sources
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>event_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.time_series_insights.event_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of the event source. |
| `location` | `string` | Resource location |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EventSources_Get` | `SELECT` | `environmentName, eventSourceName, resourceGroupName, subscriptionId` | Gets the event source with the specified name in the specified environment. |
| `EventSources_ListByEnvironment` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Lists all the available event sources associated with the subscription and within the specified resource group and environment. |
| `EventSources_CreateOrUpdate` | `INSERT` | `environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind` | Create or update an event source under the specified environment. |
| `EventSources_Delete` | `DELETE` | `environmentName, eventSourceName, resourceGroupName, subscriptionId` | Deletes the event source with the specified name in the specified subscription, resource group, and environment |
| `EventSources_Update` | `EXEC` | `environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind` | Updates the event source with the specified name in the specified subscription, resource group, and environment. |
