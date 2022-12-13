---
title: ou_container_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - ou_container_operations
  - aad_domain_services
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
<tr><td><b>Name</b></td><td><code>ou_container_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_domain_services.ou_container_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| `origin` | `string` | The origin of the operation. |
| `display` | `object` | The operation supported by Domain Services. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OuContainerOperations_List` | `SELECT` |  |
