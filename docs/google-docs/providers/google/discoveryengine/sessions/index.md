---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - discoveryengine
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
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `projects/&#123;project&#125;/locations/global/collections/&#123;collection&#125;/engines/&#123;engine&#125;/sessions/*` |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the session finished. |
| <CopyableCode code="startTime" /> | `string` | Output only. The time the session started. |
| <CopyableCode code="state" /> | `string` | The state of the session. |
| <CopyableCode code="turns" /> | `array` | Turns. |
| <CopyableCode code="userPseudoId" /> | `string` | A unique identifier for tracking users. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_sessions_get" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, sessionsId" /> | Gets a Session. |
| <CopyableCode code="projects_locations_collections_data_stores_sessions_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_engines_sessions_get" /> | `SELECT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, sessionsId" /> | Gets a Session. |
| <CopyableCode code="projects_locations_collections_engines_sessions_list" /> | `SELECT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
| <CopyableCode code="projects_locations_data_stores_sessions_get" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId, sessionsId" /> | Gets a Session. |
| <CopyableCode code="projects_locations_data_stores_sessions_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_sessions_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Session. If the Session to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_engines_sessions_create" /> | `INSERT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Creates a Session. If the Session to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_data_stores_sessions_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a Session. If the Session to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_sessions_delete" /> | `DELETE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, sessionsId" /> | Deletes a Session. If the Session to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_sessions_delete" /> | `DELETE` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, sessionsId" /> | Deletes a Session. If the Session to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_sessions_delete" /> | `DELETE` | <CopyableCode code="dataStoresId, locationsId, projectsId, sessionsId" /> | Deletes a Session. If the Session to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_sessions_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId, sessionsId" /> | Updates a Session. Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_sessions_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId, sessionsId" /> | Updates a Session. Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_sessions_patch" /> | `UPDATE` | <CopyableCode code="dataStoresId, locationsId, projectsId, sessionsId" /> | Updates a Session. Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="_projects_locations_collections_data_stores_sessions_list" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
| <CopyableCode code="_projects_locations_collections_engines_sessions_list" /> | `EXEC` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
| <CopyableCode code="_projects_locations_data_stores_sessions_list" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Sessions by their parent DataStore. |
