---
title: locations_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_capabilities
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>locations_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.locations_capabilities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `features` | `array` | The capability features. |
| `quota` | `object` | The regional quota capability. |
| `regions` | `object` | The virtual machine size compatibility features. |
| `versions` | `object` | The version capability. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `location, subscriptionId` |
