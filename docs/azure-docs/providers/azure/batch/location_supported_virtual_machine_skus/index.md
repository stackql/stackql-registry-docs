---
title: location_supported_virtual_machine_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - location_supported_virtual_machine_skus
  - batch
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
<tr><td><b>Name</b></td><td><code>location_supported_virtual_machine_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.location_supported_virtual_machine_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the SKU. |
| `capabilities` | `array` | A collection of capabilities which this SKU supports. |
| `familyName` | `string` | The family name of the SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `locationName, subscriptionId` |
| `_list` | `EXEC` | `locationName, subscriptionId` |
