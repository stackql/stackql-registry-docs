---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - gkehub
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full, unique name of this Feature resource in the format `projects/*/locations/*/features/*`. |
| `createTime` | `string` | Output only. When the Feature resource was created. |
| `updateTime` | `string` | Output only. When the Feature resource was last updated. |
| `deleteTime` | `string` | Output only. When the Feature resource was deleted. |
| `labels` | `object` | GCP labels for this Feature. |
| `resourceState` | `object` | FeatureResourceState describes the state of a Feature *resource* in the GkeHub API. See `FeatureState` for the "running state" of the Feature in the Hub and across Memberships. |
| `membershipSpecs` | `object` | Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused. The keys indicate which Membership the configuration is for, in the form: `projects/{p}/locations/{l}/memberships/{m}` Where {p} is the project, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} WILL match the Feature's project. {p} will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. |
| `state` | `object` | CommonFeatureState contains Hub-wide Feature status information. |
| `spec` | `object` | CommonFeatureSpec contains Hub-wide configuration information |
| `membershipStates` | `object` | Output only. Membership-specific Feature status. If this Feature does report any per-Membership status, this field may be unused. The keys indicate which Membership the state is for, in the form: `projects/{p}/locations/{l}/memberships/{m}` Where {p} is the project number, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} MUST match the Feature's project number. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_features_get` | `SELECT` | `featuresId, locationsId, projectsId` | Gets details of a single Feature. |
| `projects_locations_features_list` | `SELECT` | `locationsId, projectsId` | Lists Features in a given project and location. |
| `projects_locations_features_create` | `INSERT` | `locationsId, projectsId` | Adds a new Feature. |
| `projects_locations_features_delete` | `DELETE` | `featuresId, locationsId, projectsId` | Removes a Feature. |
| `projects_locations_features_patch` | `EXEC` | `featuresId, locationsId, projectsId` | Updates an existing Feature. |
