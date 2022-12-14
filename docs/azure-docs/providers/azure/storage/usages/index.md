---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - storage
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The usage names that can be used; currently limited to StorageAccount. |
| `unit` | `string` | Gets the unit of measurement. |
| `currentValue` | `integer` | Gets the current count of the allocated resources in the subscription. |
| `limit` | `integer` | Gets the maximum count of the resources that can be allocated in the subscription. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_ListByLocation` | `SELECT` | `location, subscriptionId` |
