---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - lab_services
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.lab_services.images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of an image resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets an image resource. |
| `list_by_lab_plan` | `SELECT` |  | Gets all images from galleries attached to a lab plan. |
| `create_or_update` | `INSERT` | `data__properties` | Updates an image resource via PUT. Creating new resources via PUT will not function. |
| `_list_by_lab_plan` | `EXEC` |  | Gets all images from galleries attached to a lab plan. |
| `update` | `EXEC` |  | Updates an image resource. |
