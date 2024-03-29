---
title: findings
hide_title: false
hide_table_of_contents: false
keywords:
  - findings
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.findings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resource` | `object` | Information related to the Google Cloud resource that is associated with this finding. |
| `stateChange` | `string` | State change of the finding between the points in time. |
| `finding` | `object` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_sources_findings_list` | `SELECT` | `foldersId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `organizations_sources_findings_list` | `SELECT` | `organizationsId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `projects_sources_findings_list` | `SELECT` | `projectsId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `organizations_sources_findings_create` | `INSERT` | `organizationsId, sourcesId` | Creates a finding. The corresponding source must exist for finding creation to succeed. |
| `_folders_sources_findings_list` | `EXEC` | `foldersId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `_organizations_sources_findings_list` | `EXEC` | `organizationsId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `_projects_sources_findings_list` | `EXEC` | `projectsId, sourcesId` | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| `folders_findings_bulk_mute` | `EXEC` | `foldersId` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `folders_sources_findings_group` | `EXEC` | `foldersId, sourcesId` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| `folders_sources_findings_patch` | `EXEC` | `findingsId, foldersId, sourcesId` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `folders_sources_findings_set_mute` | `EXEC` | `findingsId, foldersId, sourcesId` | Updates the mute state of a finding. |
| `folders_sources_findings_set_state` | `EXEC` | `findingsId, foldersId, sourcesId` | Updates the state of a finding. |
| `organizations_findings_bulk_mute` | `EXEC` | `organizationsId` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `organizations_sources_findings_group` | `EXEC` | `organizationsId, sourcesId` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| `organizations_sources_findings_patch` | `EXEC` | `findingsId, organizationsId, sourcesId` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `organizations_sources_findings_set_mute` | `EXEC` | `findingsId, organizationsId, sourcesId` | Updates the mute state of a finding. |
| `organizations_sources_findings_set_state` | `EXEC` | `findingsId, organizationsId, sourcesId` | Updates the state of a finding. |
| `projects_findings_bulk_mute` | `EXEC` | `projectsId` | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| `projects_sources_findings_group` | `EXEC` | `projectsId, sourcesId` | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| `projects_sources_findings_patch` | `EXEC` | `findingsId, projectsId, sourcesId` | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| `projects_sources_findings_set_mute` | `EXEC` | `findingsId, projectsId, sourcesId` | Updates the mute state of a finding. |
| `projects_sources_findings_set_state` | `EXEC` | `findingsId, projectsId, sourcesId` | Updates the state of a finding. |
