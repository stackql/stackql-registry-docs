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
| `kind` | `string` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| `location` | `string` | Resource location |
| `properties` | `object` | Metadata describing a web test for an Azure resource. |
| `tags` | `` | Resource tags |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, webTestName` | Get a specific Application Insights web test definition. |
| `list` | `SELECT` | `subscriptionId` | Get all Application Insights web test definitions for the specified subscription. |
| `list_by_component` | `SELECT` | `componentName, resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified component. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, webTestName` | Creates or updates an Application Insights web test definition. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, webTestName` | Deletes an Application Insights web test. |
| `_list` | `EXEC` | `subscriptionId` | Get all Application Insights web test definitions for the specified subscription. |
| `_list_by_component` | `EXEC` | `componentName, resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified component. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified resource group. |
