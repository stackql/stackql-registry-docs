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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `resources` | `array` | The list of matching Features |
| `nextPageToken` | `string` | A token to request the next page of resources from the `ListFeatures` method. The value of an empty string means that there are no more resources to return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_features_list` | `SELECT` | `locationsId, projectsId` | Lists Features in a given project and location. |
| `projects_locations_features_create` | `INSERT` | `locationsId, projectsId` | Adds a new Feature. |
| `projects_locations_features_delete` | `DELETE` | `featuresId, locationsId, projectsId` | Removes a Feature. |
| `projects_locations_features_get` | `EXEC` | `featuresId, locationsId, projectsId` | Gets details of a single Feature. |
| `projects_locations_features_patch` | `EXEC` | `featuresId, locationsId, projectsId` | Updates an existing Feature. |
