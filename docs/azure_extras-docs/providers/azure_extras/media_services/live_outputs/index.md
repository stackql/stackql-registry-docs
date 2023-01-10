---
title: live_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_outputs
  - media_services
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
<tr><td><b>Name</b></td><td><code>live_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.live_outputs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The JSON object that contains the properties required to create a live output. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LiveOutputs_Get` | `SELECT` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Gets a live output. |
| `LiveOutputs_List` | `SELECT` | `accountName, api-version, liveEventName, resourceGroupName, subscriptionId` | Lists the live outputs of a live event. |
| `LiveOutputs_Create` | `INSERT` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Creates a new live output. |
| `LiveOutputs_Delete` | `DELETE` | `accountName, api-version, liveEventName, liveOutputName, resourceGroupName, subscriptionId` | Deletes a live output. Deleting a live output does not delete the asset the live output is writing to. |
| `LiveOutputs_AsyncOperation` | `EXEC` | `accountName, api-version, operationId, resourceGroupName, subscriptionId` | Get a Live Output operation status. |
| `LiveOutputs_OperationLocation` | `EXEC` | `accountName, api-version, liveEventName, liveOutputName, operationId, resourceGroupName, subscriptionId` | Get a Live Output operation status. |
