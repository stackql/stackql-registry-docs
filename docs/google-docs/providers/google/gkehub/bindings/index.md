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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the membershipbinding itself `projects/&#123;project&#125;/locations/&#123;location&#125;/memberships/&#123;membership&#125;/bindings/&#123;membershipbinding&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. When the membership binding was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the membership binding was deleted. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this MembershipBinding. |
| <CopyableCode code="scope" /> | `string` | A Scope resource name in the format `projects/*/locations/*/scopes/*`. |
| <CopyableCode code="state" /> | `object` | MembershipBindingLifecycleState describes the state of a Binding resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the membership binding was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_memberships_bindings_get" /> | `SELECT` | <CopyableCode code="bindingsId, locationsId, membershipsId, projectsId" /> | Returns the details of a MembershipBinding. |
| <CopyableCode code="projects_locations_memberships_bindings_list" /> | `SELECT` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Lists MembershipBindings. |
| <CopyableCode code="projects_locations_memberships_bindings_create" /> | `INSERT` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Creates a MembershipBinding. |
| <CopyableCode code="projects_locations_memberships_bindings_delete" /> | `DELETE` | <CopyableCode code="bindingsId, locationsId, membershipsId, projectsId" /> | Deletes a MembershipBinding. |
| <CopyableCode code="_projects_locations_memberships_bindings_list" /> | `EXEC` | <CopyableCode code="locationsId, membershipsId, projectsId" /> | Lists MembershipBindings. |
| <CopyableCode code="projects_locations_memberships_bindings_patch" /> | `EXEC` | <CopyableCode code="bindingsId, locationsId, membershipsId, projectsId" /> | Updates a MembershipBinding. |
