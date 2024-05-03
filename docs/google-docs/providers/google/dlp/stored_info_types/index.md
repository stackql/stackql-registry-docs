---
title: stored_info_types
hide_title: false
hide_table_of_contents: false
keywords:
  - stored_info_types
  - dlp
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
<tr><td><b>Name</b></td><td><code>stored_info_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.stored_info_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="currentVersion" /> | `object` | Version of a StoredInfoType, including the configuration used to build it, create timestamp, and current state. |
| <CopyableCode code="pendingVersions" /> | `array` | Pending versions of the stored info type. Empty if no versions are pending. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_stored_info_types_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, storedInfoTypesId" /> | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_locations_stored_info_types_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_stored_info_types_get" /> | `SELECT` | <CopyableCode code="organizationsId, storedInfoTypesId" /> | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_stored_info_types_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_locations_stored_info_types_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, storedInfoTypesId" /> | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_locations_stored_info_types_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_stored_info_types_get" /> | `SELECT` | <CopyableCode code="projectsId, storedInfoTypesId" /> | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_stored_info_types_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_locations_stored_info_types_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_stored_info_types_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_locations_stored_info_types_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_stored_info_types_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_locations_stored_info_types_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, storedInfoTypesId" /> | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_stored_info_types_delete" /> | `DELETE` | <CopyableCode code="organizationsId, storedInfoTypesId" /> | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_locations_stored_info_types_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, storedInfoTypesId" /> | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_stored_info_types_delete" /> | `DELETE` | <CopyableCode code="projectsId, storedInfoTypesId" /> | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="_organizations_locations_stored_info_types_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="_organizations_stored_info_types_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="_projects_locations_stored_info_types_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="_projects_stored_info_types_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_locations_stored_info_types_patch" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, storedInfoTypesId" /> | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="organizations_stored_info_types_patch" /> | `EXEC` | <CopyableCode code="organizationsId, storedInfoTypesId" /> | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_locations_stored_info_types_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, storedInfoTypesId" /> | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| <CopyableCode code="projects_stored_info_types_patch" /> | `EXEC` | <CopyableCode code="projectsId, storedInfoTypesId" /> | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
