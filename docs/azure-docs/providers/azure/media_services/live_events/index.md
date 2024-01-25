---
title: live_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events
  - media_services
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
<tr><td><b>Name</b></td><td><code>live_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.live_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The live event properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Gets properties of a live event. |
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists all the live events in the account. |
| `create` | `INSERT` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Creates a new live event. |
| `delete` | `DELETE` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Deletes a live event. |
| `_list` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists all the live events in the account. |
| `allocate` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | A live event is in StandBy state after allocation completes, and is ready to start. |
| `async_operation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, subscriptionId` | Get a live event operation status. |
| `operation_location` | `EXEC` | `accountName, api-version, liveEventName, operationId, resourceGroupName, subscriptionId` | Get a live event operation status. |
| `reset` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Resets an existing live event. All live outputs for the live event are deleted and the live event is stopped and will be started again. All assets used by the live outputs and streaming locators created on these assets are unaffected.  |
| `start` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | A live event in Stopped or StandBy state will be in Running state after the start operation completes. |
| `stop` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Stops a running live event. |
| `update` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Updates settings on an existing live event. |
