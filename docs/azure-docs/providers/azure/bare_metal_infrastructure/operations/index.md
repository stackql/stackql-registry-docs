---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - bare_metal_infrastructure
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bare_metal_infrastructure.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the operation being performed on this particular object. This name should match the action name that appears in RBAC / the event service. |
| `display` | `object` | Detailed BareMetal operation information |
| `isDataAction` | `boolean` | indicates whether an operation is a data action or not. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
