---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of the Test Base Package. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a Test Base Package. |
| `list_by_test_base_account` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the packages under a Test Base Account. |
| `create` | `INSERT` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Create or replace (overwrite/recreate, with potential downtime) a Test Base Package. |
| `delete` | `DELETE` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes a Test Base Package. |
| `_list_by_test_base_account` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the packages under a Test Base Account. |
| `hard_delete` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Hard Delete a Test Base Package. |
| `run_test` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Trigger a test run on the package. |
| `update` | `EXEC` | `packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Update an existing Test Base Package. |
