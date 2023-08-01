---
title: data_set_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_set_mappings
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
<tr><td><b>Name</b></td><td><code>data_set_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.data_set_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `type` | `string` | Type of the azure resource |
| `kind` | `string` | Kind of data set mapping. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataSetMappings_Get` | `SELECT` | `accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId` | Get a DataSetMapping in a shareSubscription |
| `DataSetMappings_ListByShareSubscription` | `SELECT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` | List DataSetMappings in a share subscription |
| `DataSetMappings_Create` | `INSERT` | `accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId, data__kind` | Create a DataSetMapping  |
| `DataSetMappings_Delete` | `DELETE` | `accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId` | Delete a DataSetMapping in a shareSubscription |
