---
title: sql_pool_geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_geo_backup_policies
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_geo_backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of geo backup policy.  This is metadata used for the Azure portal experience. |
| `location` | `string` | Backup policy location. |
| `properties` | `object` | The properties of the geo backup policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolGeoBackupPolicies_Get` | `SELECT` | `geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get the specified SQL pool geo backup policy |
| `SqlPoolGeoBackupPolicies_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of SQL pool geo backup policies |
| `SqlPoolGeoBackupPolicies_CreateOrUpdate` | `INSERT` | `geoBackupPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__properties` | Updates a SQL Pool geo backup policy. |
