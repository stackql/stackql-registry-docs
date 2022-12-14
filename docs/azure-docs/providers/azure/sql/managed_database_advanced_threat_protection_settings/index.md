---
title: managed_database_advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_advanced_threat_protection_settings
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
<tr><td><b>Name</b></td><td><code>managed_database_advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_advanced_threat_protection_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Properties of an Advanced Threat Protection state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseAdvancedThreatProtectionSettings_Get` | `SELECT` | `advancedThreatProtectionName, databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed database's Advanced Threat Protection state. |
| `ManagedDatabaseAdvancedThreatProtectionSettings_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed database's Advanced Threat Protection states. |
| `ManagedDatabaseAdvancedThreatProtectionSettings_CreateOrUpdate` | `INSERT` | `advancedThreatProtectionName, databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Creates or updates a managed database's Advanced Threat Protection state. |
