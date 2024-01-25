---
title: servers_skus_for_new
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_skus_for_new
  - analysis_services
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
<tr><td><b>Name</b></td><td><code>servers_skus_for_new</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.analysis_services.servers_skus_for_new</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the SKU level. |
| `capacity` | `integer` | The number of instances in the read only query pool. |
| `tier` | `string` | The name of the Azure pricing tier to which the SKU applies. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
