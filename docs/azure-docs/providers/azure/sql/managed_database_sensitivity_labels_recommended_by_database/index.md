---
title: managed_database_sensitivity_labels_recommended_by_database
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_sensitivity_labels_recommended_by_database
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
<tr><td><b>Name</b></td><td><code>managed_database_sensitivity_labels_recommended_by_database</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_sensitivity_labels_recommended_by_database</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | Resource that manages the sensitivity label. |
| `properties` | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` |
