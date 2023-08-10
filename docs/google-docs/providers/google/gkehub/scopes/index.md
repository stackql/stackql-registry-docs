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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkehub.scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the scope `projects/&#123;project&#125;/locations/&#123;location&#125;/scopes/&#123;scope&#125;` |
| `createTime` | `string` | Output only. When the scope was created. |
| `allMemberships` | `boolean` | If true, all Memberships in the Fleet bind to this Scope. |
| `deleteTime` | `string` | Output only. When the scope was deleted. |
| `uid` | `string` | Output only. Google-generated UUID for this resource. This is unique across all scope resources. If a scope resource is deleted and another resource with the same name is created, it gets a different uid. |
| `updateTime` | `string` | Output only. When the scope was last updated. |
| `namespaceLabels` | `object` | Optional. Scope-level cluster namespace labels. For the member clusters bound to the Scope, these labels are applied to each namespace under the Scope. Scope-level labels take precedence over Namespace-level labels (`namespace_labels` in the Fleet Namespace resource) if they share a key. Keys and values must be Kubernetes-conformant. |
| `state` | `object` | ScopeLifecycleState describes the state of a Scope resource. |
| `labels` | `object` | Optional. Labels for this Scope. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_scopes_list` | `SELECT` | `locationsId, projectsId` | Lists Scopes. |
| `projects_locations_scopes_create` | `INSERT` | `locationsId, projectsId` | Creates a Scope. |
| `projects_locations_scopes_delete` | `DELETE` | `locationsId, projectsId, scopesId` | Deletes a Scope. |
| `_projects_locations_scopes_list` | `EXEC` | `locationsId, projectsId` | Lists Scopes. |
| `projects_locations_scopes_get` | `EXEC` | `locationsId, projectsId, scopesId` | Returns the details of a Scope. |
| `projects_locations_scopes_patch` | `EXEC` | `locationsId, projectsId, scopesId` | Updates a scopes. |
