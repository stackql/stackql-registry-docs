---
title: web_apps_function
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_function
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_function</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_function</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | FunctionEnvelope resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `functionName, name, resourceGroupName, subscriptionId` | Description for Get function information by its ID for web site, or a deployment slot. |
| `create` | `INSERT` | `functionName, name, resourceGroupName, subscriptionId` | Description for Create function for web site, or a deployment slot. |
| `delete` | `DELETE` | `functionName, name, resourceGroupName, subscriptionId` | Description for Delete a function for web site, or a deployment slot. |
