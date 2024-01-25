---
title: appliances_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_operations
  - resource_connector
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
<tr><td><b>Name</b></td><td><code>appliances_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_connector.appliances_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the compute operation. |
| `display` | `object` | Describes the properties of an Appliances Operation Value Display. |
| `isDataAction` | `boolean` | Is this Operation a data plane operation |
| `origin` | `string` | The origin of the compute operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
