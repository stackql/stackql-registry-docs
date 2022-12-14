---
title: geo_backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - geo_backup_policies
  - sql
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
<tr><td><b>Name</b></td><td><code>geo_backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.geo_backup_policies</code></td></tr>
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
| `GeoBackupPolicies_Get` | `SELECT` | `databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId` | Gets a geo backup policy. |
| `GeoBackupPolicies_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Returns a list of geo backup policies. |
| `GeoBackupPolicies_CreateOrUpdate` | `INSERT` | `databaseName, geoBackupPolicyName, resourceGroupName, serverName, subscriptionId, data__properties` | Updates a database geo backup policy. |
