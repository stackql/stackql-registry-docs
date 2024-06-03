---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkehub.fleets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full, unique resource name of this fleet in the format of `projects/&#123;project&#125;/locations/&#123;location&#125;/fleets/&#123;fleet&#125;`. Each Google Cloud project can have at most one fleet resource, named "default". |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Fleet was created. |
| <CopyableCode code="defaultClusterConfig" /> | `object` | DefaultClusterConfig describes the default cluster configurations to be applied to all clusters born-in-fleet. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. When the Fleet was deleted. |
| <CopyableCode code="displayName" /> | `string` | Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `Production Fleet` |
| <CopyableCode code="labels" /> | `object` | Optional. Labels for this Fleet. |
| <CopyableCode code="state" /> | `object` | FleetLifecycleState describes the state of a Fleet resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid. |
| <CopyableCode code="updateTime" /> | `string` | Output only. When the Fleet was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_fleets_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Returns all fleets within an organization or a project that the caller has access to. |
| <CopyableCode code="projects_locations_fleets_get" /> | `SELECT` | <CopyableCode code="fleetsId, locationsId, projectsId" /> | Returns the details of a fleet. |
| <CopyableCode code="projects_locations_fleets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns all fleets within an organization or a project that the caller has access to. |
| <CopyableCode code="projects_locations_fleets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a fleet. |
| <CopyableCode code="projects_locations_fleets_delete" /> | `DELETE` | <CopyableCode code="fleetsId, locationsId, projectsId" /> | Removes a Fleet. There must be no memberships remaining in the Fleet. |
| <CopyableCode code="projects_locations_fleets_patch" /> | `UPDATE` | <CopyableCode code="fleetsId, locationsId, projectsId" /> | Updates a fleet. |
| <CopyableCode code="_organizations_locations_fleets_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Returns all fleets within an organization or a project that the caller has access to. |
| <CopyableCode code="_projects_locations_fleets_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns all fleets within an organization or a project that the caller has access to. |
