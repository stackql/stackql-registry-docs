---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - monitors
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.monitors.monitors</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `monitorsCreate` | `EXEC` | `parentId, data__name, data__type, region` | Create a monitor or folder in the monitors library. |
| `monitorsDeleteById` | `EXEC` | `id, region` | Delete a monitor or folder from the monitors library. |
| `monitorsDeleteByIds` | `EXEC` | `ids, region` | Bulk delete a monitor or folder by the given identifiers in the monitors library. |
| `monitorsReadById` | `EXEC` | `id, region` | Get a monitor or folder from the monitors library. |
| `monitorsReadByIds` | `EXEC` | `ids, region` | Bulk read a monitor or folder by the given identifiers from the monitors library. |
| `monitorsUpdateById` | `EXEC` | `id, data__name, data__type, data__version, region` | Update a monitor or folder in the monitors library. |
