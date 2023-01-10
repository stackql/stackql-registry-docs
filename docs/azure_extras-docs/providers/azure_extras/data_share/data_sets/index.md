---
title: data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sets
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
<tr><td><b>Name</b></td><td><code>data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.data_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
| `kind` | `string` | Kind of data set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataSets_Get` | `SELECT` | `accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId` | Get a DataSet in a share |
| `DataSets_ListByShare` | `SELECT` | `accountName, api-version, resourceGroupName, shareName, subscriptionId` | List DataSets in a share |
| `DataSets_Create` | `INSERT` | `accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId, data__kind` | Create a DataSet  |
| `DataSets_Delete` | `DELETE` | `accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId` | Delete a DataSet in a share |
