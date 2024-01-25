---
title: artifact_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_stores
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>artifact_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.artifact_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Artifact store properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Gets information about the specified artifact store. |
| `list_by_publisher` | `SELECT` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the ArtifactStores under publisher. |
| `create_or_update` | `INSERT` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a artifact store. |
| `delete` | `DELETE` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Deletes the specified artifact store. |
| `_list_by_publisher` | `EXEC` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the ArtifactStores under publisher. |
| `update` | `EXEC` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Update artifact store resource. |
