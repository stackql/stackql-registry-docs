---
title: published_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - published_artifacts
  - blueprint
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
<tr><td><b>Name</b></td><td><code>published_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.published_artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `kind` | `string` | Specifies the kind of blueprint artifact. |
| `type` | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PublishedArtifacts_Get` | `SELECT` | `artifactName, blueprintName, resourceScope, versionId` | Get an artifact for a published blueprint definition. |
| `PublishedArtifacts_List` | `SELECT` | `blueprintName, resourceScope, versionId` | List artifacts for a version of a published blueprint definition. |
