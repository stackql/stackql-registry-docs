---
title: web_apps_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_usages
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
<tr><td><b>Name</b></td><td><code>web_apps_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | Localizable string object containing the name and a localized value. |
| `currentValue` | `integer` | The current value of the resource counter. |
| `limit` | `integer` | The resource limit. |
| `nextResetTime` | `string` | Next reset time for the resource counter. |
| `unit` | `string` | Units of measurement for the quota resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId` |
