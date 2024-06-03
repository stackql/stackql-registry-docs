---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the namespace `projects/&#123;project&#125;/locations/&#123;location&#125;/namespaces/&#123;namespace&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. When the namespace was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the namespace was deleted. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this Namespace. |
| <CopyableCode code="namespaceLabels" /> | `object` | Optional. Namespace-level cluster namespace labels. These labels are applied to the related namespace of the member clusters bound to the parent Scope. Scope-level labels (`namespace_labels` in the Fleet Scope resource) take precedence over Namespace-level labels if they share a key. Keys and values must be Kubernetes-conformant. |
| <CopyableCode code="scope" /> | `string` | Required. Scope associated with the namespace |
| <CopyableCode code="state" /> | `object` | NamespaceLifecycleState describes the state of a Namespace resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the namespace was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_scopes_namespaces_get" /> | `SELECT` | <CopyableCode code="locationsId, namespacesId, projectsId, scopesId" /> | Returns the details of a fleet namespace. |
| <CopyableCode code="projects_locations_scopes_namespaces_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Lists fleet namespaces. |
| <CopyableCode code="projects_locations_scopes_namespaces_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Creates a fleet namespace. |
| <CopyableCode code="projects_locations_scopes_namespaces_delete" /> | `DELETE` | <CopyableCode code="locationsId, namespacesId, projectsId, scopesId" /> | Deletes a fleet namespace. |
| <CopyableCode code="projects_locations_scopes_namespaces_patch" /> | `UPDATE` | <CopyableCode code="locationsId, namespacesId, projectsId, scopesId" /> | Updates a fleet namespace. |
| <CopyableCode code="_projects_locations_scopes_namespaces_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, scopesId" /> | Lists fleet namespaces. |
