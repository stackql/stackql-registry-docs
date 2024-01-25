---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
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
<tr><td><b>Name</b></td><td><code>metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Metadata property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Get a Metadata. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List of all metadata |
| `create` | `INSERT` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Create a Metadata. |
| `delete` | `DELETE` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Delete a Metadata. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List of all metadata |
| `update` | `EXEC` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Update an existing Metadata. |
