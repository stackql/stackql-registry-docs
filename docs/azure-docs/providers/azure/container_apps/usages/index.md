---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - container_apps
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The Usage Names. |
| `currentValue` | `number` | The current usage of the resource. |
| `limit` | `number` | The maximum permitted usage of the resource. |
| `unit` | `string` | An enum describing the unit of usage measurement. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, subscriptionId` |
| `_list` | `EXEC` | `location, subscriptionId` |
