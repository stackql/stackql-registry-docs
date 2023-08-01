---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
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
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to request the next page of resources from the `ListMemberships` method. The value of an empty string means that there are no more resources to return. |
| `resources` | `array` | The list of matching Memberships. |
| `unreachable` | `array` | List of locations that could not be reached while fetching this list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_memberships_list` | `SELECT` | `locationsId, projectsId` | Lists Memberships in a given project and location. |
| `projects_locations_memberships_create` | `INSERT` | `locationsId, projectsId` | Creates a new Membership. **This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster. |
| `projects_locations_memberships_delete` | `DELETE` | `locationsId, membershipsId, projectsId` | Removes a Membership. **This is currently only supported for GKE clusters on Google Cloud**. To unregister other clusters, follow the instructions at https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster. |
| `projects_locations_memberships_generate_connect_manifest` | `EXEC` | `locationsId, membershipsId, projectsId` | Generates the manifest for deployment of the GKE connect agent. **This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly. |
| `projects_locations_memberships_get` | `EXEC` | `locationsId, membershipsId, projectsId` | Gets the details of a Membership. |
| `projects_locations_memberships_patch` | `EXEC` | `locationsId, membershipsId, projectsId` | Updates an existing Membership. |
