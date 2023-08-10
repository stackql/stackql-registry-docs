---
title: rbacrolebindings
hide_title: false
hide_table_of_contents: false
keywords:
  - rbacrolebindings
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
<tr><td><b>Name</b></td><td><code>rbacrolebindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.rbacrolebindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the rbacrolebinding `projects/&#123;project&#125;/locations/&#123;location&#125;/namespaces/&#123;namespace&#125;/rbacrolebindings/&#123;rbacrolebinding&#125;` or `projects/&#123;project&#125;/locations/&#123;location&#125;/memberships/&#123;membership&#125;/rbacrolebindings/&#123;rbacrolebinding&#125;` |
| `state` | `object` | RBACRoleBindingLifecycleState describes the state of a RbacRoleBinding resource. |
| `updateTime` | `string` | Output only. When the rbacrolebinding was last updated. |
| `user` | `string` | user is the name of the user as seen by the kubernetes cluster, example "alice" or "alice@domain.tld" |
| `createTime` | `string` | Output only. When the rbacrolebinding was created. |
| `role` | `object` | Role is the type for Kubernetes roles |
| `uid` | `string` | Output only. Google-generated UUID for this resource. This is unique across all rbacrolebinding resources. If a rbacrolebinding resource is deleted and another resource with the same name is created, it gets a different uid. |
| `labels` | `object` | Optional. Labels for this RBACRolebinding. |
| `deleteTime` | `string` | Output only. When the rbacrolebinding was deleted. |
| `group` | `string` | group is the group, as seen by the kubernetes cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_scopes_rbacrolebindings_list` | `SELECT` | `locationsId, projectsId, scopesId` | Lists all Scope RBACRoleBindings. |
| `projects_locations_scopes_rbacrolebindings_create` | `INSERT` | `locationsId, projectsId, scopesId` | Creates a Scope RBACRoleBinding. |
| `projects_locations_scopes_rbacrolebindings_delete` | `DELETE` | `locationsId, projectsId, rbacrolebindingsId, scopesId` | Deletes a Scope RBACRoleBinding. |
| `_projects_locations_scopes_rbacrolebindings_list` | `EXEC` | `locationsId, projectsId, scopesId` | Lists all Scope RBACRoleBindings. |
| `projects_locations_scopes_rbacrolebindings_get` | `EXEC` | `locationsId, projectsId, rbacrolebindingsId, scopesId` | Returns the details of a Scope RBACRoleBinding. |
| `projects_locations_scopes_rbacrolebindings_patch` | `EXEC` | `locationsId, projectsId, rbacrolebindingsId, scopesId` | Updates a Scope RBACRoleBinding. |
