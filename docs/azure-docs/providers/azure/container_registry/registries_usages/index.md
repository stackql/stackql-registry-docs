---
title: registries_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - registries_usages
  - container_registry
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
<tr><td><b>Name</b></td><td><code>registries_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.registries_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the usage. |
| `currentValue` | `integer` | The current value of the usage. |
| `limit` | `integer` | The limit of the usage. |
| `unit` | `string` | The unit of measurement. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` |
