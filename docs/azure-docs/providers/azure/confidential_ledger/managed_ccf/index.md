---
title: managed_ccf
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ccf
  - confidential_ledger
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
<tr><td><b>Name</b></td><td><code>managed_ccf</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confidential_ledger.managed_ccf</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Additional Managed CCF properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appName, resourceGroupName, subscriptionId` | Retrieves the properties of a Managed CCF app. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves the properties of all Managed CCF apps. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieves the properties of all Managed CCF. |
| `create` | `INSERT` | `appName, resourceGroupName, subscriptionId` | Creates a Managed CCF with the specified Managed CCF parameters. |
| `delete` | `DELETE` | `appName, resourceGroupName, subscriptionId` | Deletes an existing Managed CCF. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves the properties of all Managed CCF apps. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieves the properties of all Managed CCF. |
| `backup` | `EXEC` | `appName, resourceGroupName, subscriptionId, data__uri` | Backs up a Managed CCF Resource. |
| `restore` | `EXEC` | `appName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri` | Restores a Managed CCF Resource. |
| `update` | `EXEC` | `appName, resourceGroupName, subscriptionId` | Updates properties of Managed CCF |
