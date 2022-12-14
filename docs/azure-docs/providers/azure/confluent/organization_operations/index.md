---
title: organization_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_operations
  - confluent
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
<tr><td><b>Name</b></td><td><code>organization_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confluent.organization_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125; |
| `display` | `object` | The object that represents the operation. |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OrganizationOperations_List` | `SELECT` |  |
