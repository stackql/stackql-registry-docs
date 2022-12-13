---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.components</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `type` | `string` | Azure resource type |
| `etag` | `string` | Resource etag |
| `kind` | `string` | The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties that define an Application Insights component resource. |
| `tags` | `` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Components_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns an Application Insights component. |
| `Components_List` | `SELECT` | `subscriptionId` | Gets a list of all Application Insights components within a subscription. |
| `Components_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Application Insights components within a resource group. |
| `Components_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, data__kind` | Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| `Components_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes an Application Insights component. |
| `Components_GetPurgeStatus` | `EXEC` | `purgeId, resourceGroupName, resourceName, subscriptionId` | Get status for an ongoing purge operation. |
| `Components_Purge` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__filters, data__table` | Purges data in an Application Insights component by a set of user-defined filters.<br /><br />In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.<br />Note: this operation is intended for Classic resources, for  workspace-based Application Insights resource please run purge operation (directly on the workspace)(https://docs.microsoft.com/en-us/rest/api/loganalytics/workspace-purge/purge) , scoped to specific resource id. |
| `Components_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates an existing component's tags. To update other fields use the CreateOrUpdate method. |
