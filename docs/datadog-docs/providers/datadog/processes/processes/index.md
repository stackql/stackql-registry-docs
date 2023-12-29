---
title: processes
hide_title: false
hide_table_of_contents: false
keywords:
  - processes
  - processes
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.processes.processes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Process ID. |
| `attributes` | `object` | Attributes for a process summary. |
| `type` | `string` | Type of process summary. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_processes` | `SELECT` | `dd_site` |
| `_list_processes` | `EXEC` | `dd_site` |
