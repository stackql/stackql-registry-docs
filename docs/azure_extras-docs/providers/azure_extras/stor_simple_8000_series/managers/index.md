---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - stor_simple_8000_series
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
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The resource name. |
| `location` | `string` | The geo location of the resource. |
| `properties` | `object` | The properties of the StorSimple Manager. |
| `tags` | `object` | The tags attached to the resource. |
| `type` | `string` | The resource type. |
| `etag` | `string` | The etag of the manager. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Managers_Get` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified manager name. |
| `Managers_List` | `SELECT` | `subscriptionId` | Retrieves all the managers in a subscription. |
| `Managers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves all the managers in a resource group. |
| `Managers_CreateOrUpdate` | `INSERT` | `managerName, resourceGroupName, subscriptionId` | Creates or updates the manager. |
| `Managers_Delete` | `DELETE` | `managerName, resourceGroupName, subscriptionId` | Deletes the manager. |
| `Managers_CreateExtendedInfo` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Creates the extended info of the manager. |
| `Managers_DeleteExtendedInfo` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Deletes the extended info of the manager. |
| `Managers_GetActivationKey` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Returns the activation key of the manager. |
| `Managers_GetDevicePublicEncryptionKey` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the public encryption key of the device. |
| `Managers_GetEncryptionSettings` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Returns the encryption settings of the manager. |
| `Managers_GetExtendedInfo` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Returns the extended information of the specified manager name. |
| `Managers_GetPublicEncryptionKey` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Returns the symmetric encrypted public encryption key of the manager. |
| `Managers_ListFeatureSupportStatus` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Lists the features and their support status |
| `Managers_ListMetricDefinition` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Gets the metric definitions for the specified manager. |
| `Managers_ListMetrics` | `EXEC` | `$filter, managerName, resourceGroupName, subscriptionId` | Gets the metrics for the specified manager. |
| `Managers_RegenerateActivationKey` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Re-generates and returns the activation key of the manager. |
| `Managers_Update` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Updates the StorSimple Manager. |
| `Managers_UpdateExtendedInfo` | `EXEC` | `If-Match, managerName, resourceGroupName, subscriptionId` | Updates the extended info of the manager. |
