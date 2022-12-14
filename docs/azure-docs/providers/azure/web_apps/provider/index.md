---
title: provider
hide_title: false
hide_table_of_contents: false
keywords:
  - provider
  - web_apps
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
<tr><td><b>Name</b></td><td><code>provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.provider</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Provider_GetAvailableStacks` | `EXEC` |  | Description for Get available application frameworks and their versions |
| `Provider_GetAvailableStacksOnPrem` | `EXEC` | `subscriptionId` | Description for Get available application frameworks and their versions |
| `Provider_GetFunctionAppStacks` | `EXEC` |  | Description for Get available Function app frameworks and their versions |
| `Provider_GetFunctionAppStacksForLocation` | `EXEC` | `location` | Description for Get available Function app frameworks and their versions for location |
| `Provider_GetWebAppStacks` | `EXEC` |  | Description for Get available Web app frameworks and their versions |
| `Provider_GetWebAppStacksForLocation` | `EXEC` | `location` | Description for Get available Web app frameworks and their versions for location |
| `Provider_ListOperations` | `EXEC` |  | Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions |
