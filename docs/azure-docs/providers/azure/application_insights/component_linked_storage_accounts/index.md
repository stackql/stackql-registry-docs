---
title: component_linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - component_linked_storage_accounts
  - application_insights
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
<tr><td><b>Name</b></td><td><code>component_linked_storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.component_linked_storage_accounts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, storageType, subscriptionId` | Returns the current linked storage settings for an Application Insights component. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, storageType, subscriptionId` | Delete linked storage accounts for an Application Insights component. |
| `create_and_update` | `EXEC` | `resourceGroupName, resourceName, storageType, subscriptionId` | Replace current linked storage account for an Application Insights component. |
| `update` | `EXEC` | `resourceGroupName, resourceName, storageType, subscriptionId` | Update linked storage accounts for an Application Insights component. |
