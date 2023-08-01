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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stored_info_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.stored_info_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `storedInfoTypes` | `array` | List of storedInfoTypes, up to page_size in ListStoredInfoTypesRequest. |
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListStoredInfoTypes request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_stored_info_types_get` | `SELECT` | `locationsId, organizationsId, storedInfoTypesId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_locations_stored_info_types_list` | `SELECT` | `locationsId, organizationsId` | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_stored_info_types_get` | `SELECT` | `organizationsId, storedInfoTypesId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_stored_info_types_list` | `SELECT` | `organizationsId` | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_locations_stored_info_types_get` | `SELECT` | `locationsId, projectsId, storedInfoTypesId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_locations_stored_info_types_list` | `SELECT` | `locationsId, projectsId` | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_stored_info_types_get` | `SELECT` | `projectsId, storedInfoTypesId` | Gets a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_stored_info_types_list` | `SELECT` | `projectsId` | Lists stored infoTypes. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_locations_stored_info_types_create` | `INSERT` | `locationsId, organizationsId` | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_stored_info_types_create` | `INSERT` | `organizationsId` | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_locations_stored_info_types_create` | `INSERT` | `locationsId, projectsId` | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_stored_info_types_create` | `INSERT` | `projectsId` | Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_locations_stored_info_types_delete` | `DELETE` | `locationsId, organizationsId, storedInfoTypesId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_stored_info_types_delete` | `DELETE` | `organizationsId, storedInfoTypesId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_locations_stored_info_types_delete` | `DELETE` | `locationsId, projectsId, storedInfoTypesId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_stored_info_types_delete` | `DELETE` | `projectsId, storedInfoTypesId` | Deletes a stored infoType. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_locations_stored_info_types_patch` | `EXEC` | `locationsId, organizationsId, storedInfoTypesId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `organizations_stored_info_types_patch` | `EXEC` | `organizationsId, storedInfoTypesId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_locations_stored_info_types_patch` | `EXEC` | `locationsId, projectsId, storedInfoTypesId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
| `projects_stored_info_types_patch` | `EXEC` | `projectsId, storedInfoTypesId` | Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/dlp/docs/creating-stored-infotypes to learn more. |
