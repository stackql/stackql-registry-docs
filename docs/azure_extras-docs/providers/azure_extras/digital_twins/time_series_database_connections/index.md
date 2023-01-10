---
title: time_series_database_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series_database_connections
  - digital_twins
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
<tr><td><b>Name</b></td><td><code>time_series_database_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.digital_twins.time_series_database_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | Extension resource name. |
| `properties` | `object` | Properties of a time series database connection resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TimeSeriesDatabaseConnections_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName` | Get the description of an existing time series database connection. |
| `TimeSeriesDatabaseConnections_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get all existing time series database connections for this DigitalTwins instance. |
| `TimeSeriesDatabaseConnections_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName` | Create or update a time series database connection. |
| `TimeSeriesDatabaseConnections_Delete` | `DELETE` | `api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName` | Delete a time series database connection. |
