---
title: synchronization_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_settings
  - data_share
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
<tr><td><b>Name</b></td><td><code>synchronization_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.synchronization_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
| `kind` | `string` | Kind of synchronization setting. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SynchronizationSettings_Get` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId, synchronizationSettingName` | Get a synchronizationSetting in a share |
| `SynchronizationSettings_ListByShare` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List synchronizationSettings in a share |
| `SynchronizationSettings_Create` | `INSERT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId, synchronizationSettingName, data__kind` | Create a synchronizationSetting |
| `SynchronizationSettings_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, shareName, subscriptionId, synchronizationSettingName` | Delete a synchronizationSetting in a share |
