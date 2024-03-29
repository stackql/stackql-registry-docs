---
title: generate_detailed_cost_report_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_detailed_cost_report_operation_results
  - cost_management
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
<tr><td><b>Name</b></td><td><code>generate_detailed_cost_report_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.generate_detailed_cost_report_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ARM resource id of the long running operation. |
| `name` | `string` | The name of the long running operation. |
| `properties` | `object` | The URL to download the generated report. |
| `type` | `string` | The type of the long running operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `operationId, scope` |
