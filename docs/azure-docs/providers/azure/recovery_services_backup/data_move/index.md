---
title: data_move
hide_title: false
hide_table_of_contents: false
keywords:
  - data_move
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>data_move</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.data_move</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BMSPrepareDataMove` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName, data__dataMoveLevel, data__targetRegion, data__targetResourceId` | Prepares source vault for Data Move operation |
| `BMSTriggerDataMove` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName, data__correlationId, data__dataMoveLevel, data__sourceRegion, data__sourceResourceId` | Triggers Data Move Operation on target vault |
| `GetOperationStatus` | `EXEC` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` | Fetches operation status for data move operation on vault |
