---
title: bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - bindings
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
<tr><td><b>Name</b></td><td><code>bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.bindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to request the next page of resources from the `ListMembershipBindings` method. The value of an empty string means that there are no more resources to return. |
| `membershipBindings` | `array` | The list of membership_bindings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_memberships_bindings_list` | `SELECT` | `locationsId, membershipsId, projectsId` | Lists MembershipBindings. |
| `projects_locations_memberships_bindings_create` | `INSERT` | `locationsId, membershipsId, projectsId` | Creates a MembershipBinding. |
| `projects_locations_memberships_bindings_delete` | `DELETE` | `bindingsId, locationsId, membershipsId, projectsId` | Deletes a MembershipBinding. |
| `projects_locations_memberships_bindings_get` | `EXEC` | `bindingsId, locationsId, membershipsId, projectsId` | Returns the details of a MembershipBinding. |
| `projects_locations_memberships_bindings_patch` | `EXEC` | `bindingsId, locationsId, membershipsId, projectsId` | Updates a MembershipBinding. |
