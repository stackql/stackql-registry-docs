---
title: servers_details
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_details
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
<tr><td><b>Name</b></td><td><code>servers_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.analysis_services.servers_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Analysis Services resource. |
| `name` | `string` | The name of the Analysis Services resource. |
| `location` | `string` | Location of the Analysis Services resource. |
| `properties` | `object` | Properties of Analysis Services resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the Analysis Services resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
