---
title: project_data_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - project_data_profiles
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
<tr><td><b>Name</b></td><td><code>project_data_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dlp.project_data_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the profile. |
| <CopyableCode code="dataRiskLevel" /> | `object` | Score is a summary of all elements in the data profile. A higher number means more risk. |
| <CopyableCode code="profileLastGenerated" /> | `string` | The last time the profile was generated. |
| <CopyableCode code="profileStatus" /> | `object` | Success or errors for the profile generation. |
| <CopyableCode code="projectId" /> | `string` | Project ID that was profiled. |
| <CopyableCode code="sensitivityScore" /> | `object` | Score is calculated from of all elements in the data profile. A higher level means the data is more sensitive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_project_data_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, projectDataProfilesId" /> | Gets a project data profile. |
| <CopyableCode code="organizations_locations_project_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists project data profiles for an organization. |
| <CopyableCode code="projects_locations_project_data_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, projectDataProfilesId, projectsId" /> | Gets a project data profile. |
| <CopyableCode code="projects_locations_project_data_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists project data profiles for an organization. |
| <CopyableCode code="_organizations_locations_project_data_profiles_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists project data profiles for an organization. |
| <CopyableCode code="_projects_locations_project_data_profiles_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists project data profiles for an organization. |
