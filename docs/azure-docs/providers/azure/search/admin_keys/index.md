---
title: admin_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_keys
  - search
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
<tr><td><b>Name</b></td><td><code>admin_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.search.admin_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryKey` | `string` | The primary admin API key of the search service. |
| `secondaryKey` | `string` | The secondary admin API key of the search service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Gets the primary and secondary admin API keys for the specified search service. |
| `regenerate` | `EXEC` | `keyKind, resourceGroupName, searchServiceName, subscriptionId` | Regenerates either the primary or secondary admin API key. You can only regenerate one key at a time. |
