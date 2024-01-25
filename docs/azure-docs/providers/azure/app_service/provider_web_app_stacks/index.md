---
title: provider_web_app_stacks
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_web_app_stacks
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
<tr><td><b>Name</b></td><td><code>provider_web_app_stacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.provider_web_app_stacks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Web App stack location. |
| `properties` | `object` | WebAppStack resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |
| `_get` | `EXEC` |  |
