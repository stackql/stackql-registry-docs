---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.artifacts</code></td></tr>
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
| `Artifacts_Get` | `SELECT` | `artifactName, blueprintName, resourceScope` | Get a blueprint artifact. |
| `Artifacts_List` | `SELECT` | `blueprintName, resourceScope` | List artifacts for a given blueprint definition. |
| `Artifacts_CreateOrUpdate` | `INSERT` | `artifactName, blueprintName, resourceScope, data__kind` | Create or update blueprint artifact. |
| `Artifacts_Delete` | `DELETE` | `artifactName, blueprintName, resourceScope` | Delete a blueprint artifact. |
