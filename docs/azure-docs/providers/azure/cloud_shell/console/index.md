---
title: console
hide_title: false
hide_table_of_contents: false
keywords:
  - console
  - cloud_shell
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
<tr><td><b>Name</b></td><td><code>console</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cloud_shell.console</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consoleName` | Gets the console for the user. |
| `delete` | `DELETE` | `consoleName` | Deletes the console |
| `keep_alive` | `EXEC` | `consoleName` | Keep console alive |
| `put` | `EXEC` | `consoleName, data__properties` | Puts a request for a console |
