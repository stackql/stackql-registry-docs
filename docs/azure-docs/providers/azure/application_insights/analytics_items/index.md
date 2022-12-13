---
title: analytics_items
hide_title: false
hide_table_of_contents: false
keywords:
  - analytics_items
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
<tr><td><b>Name</b></td><td><code>analytics_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.analytics_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `TimeModified` | `string` | Date and time in UTC of the last modification that was made to this item. |
| `Version` | `string` | This instance's version of the data model. This can change as new features are added. |
| `Scope` | `string` | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. |
| `TimeCreated` | `string` | Date and time in UTC when this item was created. |
| `Type` | `string` | Enum indicating the type of the Analytics item. |
| `Properties` | `object` | A set of properties that can be defined in the context of a specific item type. Each type may have its own properties. |
| `Content` | `string` | The content of this item |
| `Id` | `string` | Internally assigned unique id of the item definition. |
| `Name` | `string` | The user-defined name of the item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AnalyticsItems_List` | `SELECT` | `resourceGroupName, resourceName, scopePath, subscriptionId` | Gets a list of Analytics Items defined within an Application Insights component. |
| `AnalyticsItems_Delete` | `DELETE` | `resourceGroupName, resourceName, scopePath, subscriptionId` | Deletes a specific Analytics Items defined within an Application Insights component. |
| `AnalyticsItems_Get` | `EXEC` | `resourceGroupName, resourceName, scopePath, subscriptionId` | Gets a specific Analytics Items defined within an Application Insights component. |
| `AnalyticsItems_Put` | `EXEC` | `resourceGroupName, resourceName, scopePath, subscriptionId` | Adds or Updates a specific Analytics Item within an Application Insights component. |
