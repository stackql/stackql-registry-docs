---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - dataplex
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataplex.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the environment, of the form: projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/environment/&#123;environment_id&#125; |
| <CopyableCode code="description" /> | `string` | Optional. Description of the environment. |
| <CopyableCode code="createTime" /> | `string` | Output only. Environment creation time. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="endpoints" /> | `object` | URI Endpoints to access sessions associated with the Environment. |
| <CopyableCode code="infrastructureSpec" /> | `object` | Configuration for the underlying infrastructure used to run workloads. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the environment. |
| <CopyableCode code="sessionSpec" /> | `object` | Configuration for sessions created for this environment. |
| <CopyableCode code="sessionStatus" /> | `object` | Status of sessions created for this environment. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the environment. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the environment. This ID will be different if the environment is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the environment was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_environments_get" /> | `SELECT` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Get environment resource. |
| <CopyableCode code="projects_locations_lakes_environments_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists environments under the given lake. |
| <CopyableCode code="projects_locations_lakes_environments_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Create an environment resource. |
| <CopyableCode code="projects_locations_lakes_environments_delete" /> | `DELETE` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Delete the environment resource. All the child resources must have been deleted before environment deletion can be initiated. |
| <CopyableCode code="_projects_locations_lakes_environments_list" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists environments under the given lake. |
| <CopyableCode code="projects_locations_lakes_environments_patch" /> | `EXEC` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Update the environment resource. |
