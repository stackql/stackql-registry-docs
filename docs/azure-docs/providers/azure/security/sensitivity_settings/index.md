---
title: sensitivity_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sensitivity_settings
  - security
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
<tr><td><b>Name</b></td><td><code>sensitivity_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.sensitivity_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the sensitivity settings |
| `name` | `string` | The name of the sensitivity settings |
| `properties` | `object` | The sensitivity settings properties |
| `type` | `string` | The type of the sensitivity settings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `api-version` | Gets a list with a single sensitivity settings resource |
| `_list` | `EXEC` | `api-version` | Gets a list with a single sensitivity settings resource |
| `sensitivity_settings` | `EXEC` | `api-version` | Gets data sensitivity settings for sensitive data discovery |
