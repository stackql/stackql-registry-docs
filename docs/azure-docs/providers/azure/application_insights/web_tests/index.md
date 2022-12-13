---
title: web_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - web_tests
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
<tr><td><b>Name</b></td><td><code>web_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.web_tests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `type` | `string` | Azure resource type |
| `kind` | `string` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| `location` | `string` | Resource location |
| `properties` | `object` | Metadata describing a web test for an Azure resource. |
| `tags` | `` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebTests_Get` | `SELECT` | `resourceGroupName, subscriptionId, webTestName` | Get a specific Application Insights web test definition. |
| `WebTests_List` | `SELECT` | `subscriptionId` | Get all Application Insights web test definitions for the specified subscription. |
| `WebTests_ListByComponent` | `SELECT` | `componentName, resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified component. |
| `WebTests_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified resource group. |
| `WebTests_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, webTestName` | Creates or updates an Application Insights web test definition. |
| `WebTests_Delete` | `DELETE` | `resourceGroupName, subscriptionId, webTestName` | Deletes an Application Insights web test. |
| `WebTests_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, webTestName` | Updates the tags associated with an Application Insights web test. |
