---
title: work_item_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - work_item_configurations
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
<tr><td><b>Name</b></td><td><code>work_item_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.work_item_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ConfigProperties` | `string` | Serialized JSON object for detailed properties |
| `ConnectorId` | `string` | Connector identifier where work item is created |
| `Id` | `string` | Unique Id for work item |
| `IsDefault` | `boolean` | Boolean value indicating whether configuration is default |
| `ConfigDisplayName` | `string` | Configuration friendly name |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkItemConfigurations_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the list work item configurations that exist for the application |
| `WorkItemConfigurations_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a work item configuration for an Application Insights component. |
| `WorkItemConfigurations_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId, workItemConfigId` | Delete a work item configuration of an Application Insights component. |
| `WorkItemConfigurations_GetDefault` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets default work item configurations that exist for the application |
| `WorkItemConfigurations_GetItem` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, workItemConfigId` | Gets specified work item configuration for an Application Insights component. |
| `WorkItemConfigurations_UpdateItem` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, workItemConfigId` | Update a work item configuration for an Application Insights component. |
