---
title: content_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - content_packages
  - sentinel
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
<tr><td><b>Name</b></td><td><code>content_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.content_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes package properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageId, resourceGroupName, subscriptionId, workspaceName` | Gets an installed packages by its id. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all installed packages. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all installed packages. |
