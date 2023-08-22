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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the namespace `projects/&#123;project&#125;/locations/&#123;location&#125;/namespaces/&#123;namespace&#125;` |
| `labels` | `object` | Optional. Labels for this Namespace. |
| `uid` | `string` | Output only. Google-generated UUID for this resource. This is unique across all namespace resources. If a namespace resource is deleted and another resource with the same name is created, it gets a different uid. |
| `deleteTime` | `string` | Output only. When the namespace was deleted. |
| `scope` | `string` | Required. Scope associated with the namespace |
| `updateTime` | `string` | Output only. When the namespace was last updated. |
| `namespaceLabels` | `object` | Optional. Namespace-level cluster namespace labels. These labels are applied to the related namespace of the member clusters bound to the parent Scope. Scope-level labels (`namespace_labels` in the Fleet Scope resource) take precedence over Namespace-level labels if they share a key. Keys and values must be Kubernetes-conformant. |
| `state` | `object` | NamespaceLifecycleState describes the state of a Namespace resource. |
| `createTime` | `string` | Output only. When the namespace was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_scopes_namespaces_get` | `SELECT` | `locationsId, namespacesId, projectsId, scopesId` | Returns the details of a fleet namespace. |
| `projects_locations_scopes_namespaces_list` | `SELECT` | `locationsId, projectsId, scopesId` | Lists fleet namespaces. |
| `projects_locations_scopes_namespaces_create` | `INSERT` | `locationsId, projectsId, scopesId` | Creates a fleet namespace. |
| `projects_locations_scopes_namespaces_delete` | `DELETE` | `locationsId, namespacesId, projectsId, scopesId` | Deletes a fleet namespace. |
| `_projects_locations_scopes_namespaces_list` | `EXEC` | `locationsId, projectsId, scopesId` | Lists fleet namespaces. |
| `projects_locations_scopes_namespaces_patch` | `EXEC` | `locationsId, namespacesId, projectsId, scopesId` | Updates a fleet namespace. |
