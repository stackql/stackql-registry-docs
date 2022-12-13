---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
  - security_insights
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
<tr><td><b>Id</b></td><td><code>azure.security_insights.metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Metadata property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Metadata_Get` | `SELECT` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Get a Metadata. |
| `Metadata_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List of all metadata |
| `Metadata_Create` | `INSERT` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Create a Metadata. |
| `Metadata_Delete` | `DELETE` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Delete a Metadata. |
| `Metadata_Update` | `EXEC` | `metadataName, resourceGroupName, subscriptionId, workspaceName` | Update an existing Metadata. |
