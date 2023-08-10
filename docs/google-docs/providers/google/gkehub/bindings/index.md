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
| `name` | `string` | The resource name for the membershipbinding itself `projects/&#123;project&#125;/locations/&#123;location&#125;/memberships/&#123;membership&#125;/bindings/&#123;membershipbinding&#125;` |
| `deleteTime` | `string` | Output only. When the membership binding was deleted. |
| `fleet` | `boolean` | Whether the membershipbinding is Fleet-wide; true means that this Membership should be bound to all Namespaces in this entire Fleet. |
| `uid` | `string` | Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid. |
| `createTime` | `string` | Output only. When the membership binding was created. |
| `updateTime` | `string` | Output only. When the membership binding was last updated. |
| `labels` | `object` | Optional. Labels for this MembershipBinding. |
| `state` | `object` | MembershipBindingLifecycleState describes the state of a Binding resource. |
| `scope` | `string` | A Scope resource name in the format `projects/*/locations/*/scopes/*`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_memberships_bindings_list` | `SELECT` | `locationsId, membershipsId, projectsId` | Lists MembershipBindings. |
| `projects_locations_memberships_bindings_create` | `INSERT` | `locationsId, membershipsId, projectsId` | Creates a MembershipBinding. |
| `projects_locations_memberships_bindings_delete` | `DELETE` | `bindingsId, locationsId, membershipsId, projectsId` | Deletes a MembershipBinding. |
| `_projects_locations_memberships_bindings_list` | `EXEC` | `locationsId, membershipsId, projectsId` | Lists MembershipBindings. |
| `projects_locations_memberships_bindings_get` | `EXEC` | `bindingsId, locationsId, membershipsId, projectsId` | Returns the details of a MembershipBinding. |
| `projects_locations_memberships_bindings_patch` | `EXEC` | `bindingsId, locationsId, membershipsId, projectsId` | Updates a MembershipBinding. |
