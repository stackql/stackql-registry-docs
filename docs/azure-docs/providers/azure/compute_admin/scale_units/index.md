---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.scale_units</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties for a scale unit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ScaleUnits_Get` | `SELECT` | `location, scaleUnitName, subscriptionId` |
