---
title: best_practices
hide_title: false
hide_table_of_contents: false
keywords:
  - best_practices
  - automanage
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
<tr><td><b>Name</b></td><td><code>best_practices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automanage.best_practices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully qualified ID for the best practice.  For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction |
| `name` | `string` | The name of the best practice. For example, azureBestPracticesProduction |
| `properties` | `object` | Automanage configuration profile properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource.  For example, Microsoft.Automanage/bestPractices |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bestPracticeName` | Get information about a Automanage best practice |
| `list_by_tenant` | `SELECT` |  | Retrieve a list of Automanage best practices |
| `_list_by_tenant` | `EXEC` |  | Retrieve a list of Automanage best practices |
