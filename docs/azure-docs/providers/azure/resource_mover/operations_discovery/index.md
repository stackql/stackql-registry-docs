---
title: operations_discovery
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_discovery
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>operations_discovery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_mover.operations_discovery</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Gets or sets the value of next link. |
| `value` | `array` | Gets or sets the ClientDiscovery details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationsDiscovery_Get` | `SELECT` | `api-version` |
