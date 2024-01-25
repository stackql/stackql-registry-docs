---
title: managed_clusters_os_options
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_os_options
  - aks
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
<tr><td><b>Name</b></td><td><code>managed_clusters_os_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aks.managed_clusters_os_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the OS option resource. |
| `name` | `string` | The name of the OS option resource. |
| `properties` | `object` | The list of OS option properties. |
| `type` | `string` | The type of the OS option resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `location, subscriptionId` |
