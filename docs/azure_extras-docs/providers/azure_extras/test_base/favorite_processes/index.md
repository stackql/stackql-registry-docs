---
title: favorite_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - favorite_processes
  - test_base
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
<tr><td><b>Name</b></td><td><code>favorite_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.favorite_processes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a favorite process identifier. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FavoriteProcesses_Get` | `SELECT` | `favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a favorite process for a Test Base Package. |
| `FavoriteProcesses_List` | `SELECT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists the favorite processes for a specific package. |
| `FavoriteProcesses_Create` | `INSERT` | `favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Create or replace a favorite process for a Test Base Package. |
| `FavoriteProcesses_Delete` | `DELETE` | `favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a favorite process for a specific package. |
