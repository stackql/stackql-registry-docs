---
title: artifact_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - artifact_sources
  - deployment_manager
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
<tr><td><b>Name</b></td><td><code>artifact_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.artifact_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define the artifact source. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ArtifactSources_Get` | `SELECT` | `artifactSourceName, resourceGroupName, subscriptionId` |  |
| `ArtifactSources_List` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ArtifactSources_CreateOrUpdate` | `INSERT` | `artifactSourceName, resourceGroupName, subscriptionId` | Synchronously creates a new artifact source or updates an existing artifact source. |
| `ArtifactSources_Delete` | `DELETE` | `artifactSourceName, resourceGroupName, subscriptionId` |  |
