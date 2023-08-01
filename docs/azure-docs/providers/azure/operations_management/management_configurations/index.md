---
title: management_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_configurations
  - operations_management
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
<tr><td><b>Name</b></td><td><code>management_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operations_management.management_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location |
| `properties` | `object` | ManagementConfiguration properties supported by the OperationsManagement resource provider. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementConfigurations_Get` | `SELECT` | `managementConfigurationName, resourceGroupName, subscriptionId` | Retrieves the user ManagementConfiguration. |
| `ManagementConfigurations_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieves the ManagementConfigurations list. |
| `ManagementConfigurations_CreateOrUpdate` | `INSERT` | `managementConfigurationName, resourceGroupName, subscriptionId` | Creates or updates the ManagementConfiguration. |
| `ManagementConfigurations_Delete` | `DELETE` | `managementConfigurationName, resourceGroupName, subscriptionId` | Deletes the ManagementConfiguration in the subscription. |
