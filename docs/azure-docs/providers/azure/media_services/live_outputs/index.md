---
title: live_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_outputs
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
<tr><td><b>Name</b></td><td><code>live_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.live_outputs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The JSON object that contains the properties required to create a live output. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Gets a live output. |
| `list` | `SELECT` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Lists the live outputs of a live event. |
| `create` | `INSERT` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Creates a new live output. |
| `delete` | `DELETE` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Deletes a live output. Deleting a live output does not delete the asset the live output is writing to. |
| `_list` | `EXEC` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Lists the live outputs of a live event. |
| `async_operation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, subscriptionId` | Get a Live Output operation status. |
| `operation_location` | `EXEC` | `accountName, api-version, liveEventName, liveOutputName, operationId, resourceGroupName, subscriptionId` | Get a Live Output operation status. |
