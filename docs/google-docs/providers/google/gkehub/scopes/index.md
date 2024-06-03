---
title: scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - scopes
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
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the scope `projects/&#123;project&#125;/locations/&#123;location&#125;/scopes/&#123;scope&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. When the scope was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the scope was deleted. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this Scope. |
| <CopyableCode code="namespaceLabels" /> | `object` | Optional. Scope-level cluster namespace labels. For the member clusters bound to the Scope, these labels are applied to each namespace under the Scope. Scope-level labels take precedence over Namespace-level labels (`namespace_labels` in the Fleet Namespace resource) if they share a key. Keys and values must be Kubernetes-conformant. |
| <CopyableCode code="state" /> | `object` | ScopeLifecycleState describes the state of a Scope resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the scope was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_scopes_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Returns the details of a Scope. |
| <CopyableCode code="projects_locations_scopes_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Scopes. |
| <CopyableCode code="projects_locations_scopes_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Scope. |
| <CopyableCode code="projects_locations_scopes_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Deletes a Scope. |
| <CopyableCode code="projects_locations_scopes_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Updates a scopes. |
| <CopyableCode code="_projects_locations_scopes_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Scopes. |
