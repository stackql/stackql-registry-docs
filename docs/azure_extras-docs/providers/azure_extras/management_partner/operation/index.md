---
title: operation
hide_title: false
hide_table_of_contents: false
keywords:
  - operation
  - management_partner
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.management_partner.operation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | this is the operation response name |
| `origin` | `string` | the is operation response origin information |
| `display` | `object` | this is the management partner operation |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Operation_List` | `SELECT` |  |
