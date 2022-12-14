---
title: published_blueprints
hide_title: false
hide_table_of_contents: false
keywords:
  - published_blueprints
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
<tr><td><b>Name</b></td><td><code>published_blueprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.published_blueprints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `type` | `string` | Type of this resource. |
| `properties` | `object` | Schema for published blueprint definition properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PublishedBlueprints_Get` | `SELECT` | `blueprintName, resourceScope, versionId` | Get a published version of a blueprint definition. |
| `PublishedBlueprints_List` | `SELECT` | `blueprintName, resourceScope` | List published versions of given blueprint definition. |
| `PublishedBlueprints_Create` | `INSERT` | `blueprintName, resourceScope, versionId, data__properties` | Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable. |
| `PublishedBlueprints_Delete` | `DELETE` | `blueprintName, resourceScope, versionId` | Delete a published version of a blueprint definition. |
