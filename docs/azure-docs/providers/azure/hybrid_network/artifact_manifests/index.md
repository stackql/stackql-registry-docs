---
title: artifact_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_manifests
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
<tr><td><b>Name</b></td><td><code>artifact_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.artifact_manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Artifact manifest properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Gets information about a artifact manifest resource. |
| `list_by_artifact_store` | `SELECT` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Gets information about the artifact manifest. |
| `create_or_update` | `INSERT` | `artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a artifact manifest. |
| `delete` | `DELETE` | `artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Deletes the specified artifact manifest. |
| `_list_by_artifact_store` | `EXEC` | `artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Gets information about the artifact manifest. |
| `update` | `EXEC` | `artifactManifestName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` | Updates a artifact manifest resource. |
