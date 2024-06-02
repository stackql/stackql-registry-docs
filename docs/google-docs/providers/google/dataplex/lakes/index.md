---
title: lakes
hide_title: false
hide_table_of_contents: false
keywords:
  - lakes
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
<tr><td><b>Name</b></td><td><code>lakes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataplex.lakes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the lake, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the lake. |
| <CopyableCode code="assetStatus" /> | `object` | Aggregated status of the underlying assets of a lake or zone. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the lake was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the lake. |
| <CopyableCode code="metastore" /> | `object` | Settings to manage association of Dataproc Metastore with a lake. |
| <CopyableCode code="metastoreStatus" /> | `object` | Status of Lake and Dataproc Metastore service instance association. |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the lake. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the lake was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_get" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Retrieves a lake resource. |
| <CopyableCode code="projects_locations_lakes_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists lake resources in a project and location. |
| <CopyableCode code="projects_locations_lakes_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a lake resource. |
| <CopyableCode code="projects_locations_lakes_delete" /> | `DELETE` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted. |
| <CopyableCode code="_projects_locations_lakes_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists lake resources in a project and location. |
| <CopyableCode code="projects_locations_lakes_patch" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Updates a lake resource. |
