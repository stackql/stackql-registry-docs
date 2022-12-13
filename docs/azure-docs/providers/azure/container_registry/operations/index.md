---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| `display` | `object` | The display information for a container registry operation. |
| `isDataAction` | `boolean` | This property indicates if the operation is an action or a data action<br />ref: https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions#management-and-data-operations |
| `origin` | `string` | The origin information of the container registry operation. |
| `properties` | `object` | The definition of Azure Monitoring properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operations_List` | `SELECT` |  |
