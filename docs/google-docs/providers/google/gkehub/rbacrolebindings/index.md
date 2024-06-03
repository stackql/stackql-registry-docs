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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rbacrolebindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.rbacrolebindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the rbacrolebinding `projects/&#123;project&#125;/locations/&#123;location&#125;/scopes/&#123;scope&#125;/rbacrolebindings/&#123;rbacrolebinding&#125;` or `projects/&#123;project&#125;/locations/&#123;location&#125;/memberships/&#123;membership&#125;/rbacrolebindings/&#123;rbacrolebinding&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. When the rbacrolebinding was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the rbacrolebinding was deleted. |
| <CopyableCode code="group" /> | `string` | group is the group, as seen by the kubernetes cluster. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this RBACRolebinding. |
| <CopyableCode code="role" /> | `object` | Role is the type for Kubernetes roles |
| <CopyableCode code="state" /> | `object` | RBACRoleBindingLifecycleState describes the state of a RbacRoleBinding resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all rbacrolebinding resources. If a rbacrolebinding resource is deleted and another resource with the same name is created, it gets a different uid. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the rbacrolebinding was last updated. |
| <CopyableCode code="user" /> | `string` | user is the name of the user as seen by the kubernetes cluster, example "alice" or "alice@domain.tld" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_scopes_rbacrolebindings_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, rbacrolebindingsId, scopesId" /> | Returns the details of a Scope RBACRoleBinding. |
| <CopyableCode code="projects_locations_scopes_rbacrolebindings_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Lists all Scope RBACRoleBindings. |
| <CopyableCode code="projects_locations_scopes_rbacrolebindings_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Creates a Scope RBACRoleBinding. |
| <CopyableCode code="projects_locations_scopes_rbacrolebindings_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, rbacrolebindingsId, scopesId" /> | Deletes a Scope RBACRoleBinding. |
| <CopyableCode code="projects_locations_scopes_rbacrolebindings_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, rbacrolebindingsId, scopesId" /> | Updates a Scope RBACRoleBinding. |
| <CopyableCode code="_projects_locations_scopes_rbacrolebindings_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Lists all Scope RBACRoleBindings. |
