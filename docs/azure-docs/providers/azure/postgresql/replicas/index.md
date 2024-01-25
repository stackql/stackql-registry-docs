---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - postgresql
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
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Information describing the identities associated with this application. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a server. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` |
