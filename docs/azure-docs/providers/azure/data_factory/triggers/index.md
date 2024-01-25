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
| `get` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Gets a trigger. |
| `list_by_factory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists triggers. |
| `create_or_update` | `INSERT` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName, data__properties` | Creates or updates a trigger. |
| `delete` | `DELETE` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Deletes a trigger. |
| `_list_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists triggers. |
| `query_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Query triggers. |
| `start` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Starts a trigger. |
| `stop` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Stops a trigger. |
| `subscribe_to_events` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Subscribe event trigger to events. |
| `unsubscribe_from_events` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, triggerName` | Unsubscribe event trigger from events. |
