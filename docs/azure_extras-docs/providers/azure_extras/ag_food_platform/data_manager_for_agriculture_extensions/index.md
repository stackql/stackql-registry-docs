---
title: data_manager_for_agriculture_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_manager_for_agriculture_extensions
  - ag_food_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>data_manager_for_agriculture_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.data_manager_for_agriculture_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | DataManagerForAgricultureExtension properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerForAgricultureExtensionId` | Get Data Manager For Agriculture extension. |
| `list` | `SELECT` |  | Get list of Data Manager For Agriculture extension. |
| `_list` | `EXEC` |  | Get list of Data Manager For Agriculture extension. |
