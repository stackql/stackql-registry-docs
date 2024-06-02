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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="securitycenter.findings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="finding" /> | `object` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding. |
| <CopyableCode code="resource" /> | `object` | Information related to the Google Cloud resource that is associated with this finding. |
| <CopyableCode code="stateChange" /> | `string` | State change of the finding between the points in time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_findings_list" /> | `SELECT` | <CopyableCode code="foldersId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_list" /> | `SELECT` | <CopyableCode code="organizationsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="projects_sources_findings_list" /> | `SELECT` | <CopyableCode code="projectsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_create" /> | `INSERT` | <CopyableCode code="organizationsId, sourcesId" /> | Creates a finding. The corresponding source must exist for finding creation to succeed. |
| <CopyableCode code="_folders_sources_findings_list" /> | `EXEC` | <CopyableCode code="foldersId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="_organizations_sources_findings_list" /> | `EXEC` | <CopyableCode code="organizationsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="_projects_sources_findings_list" /> | `EXEC` | <CopyableCode code="projectsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings |
| <CopyableCode code="folders_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="foldersId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="folders_sources_findings_group" /> | `EXEC` | <CopyableCode code="foldersId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| <CopyableCode code="folders_sources_findings_patch" /> | `EXEC` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="folders_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="folders_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Updates the state of a finding. |
| <CopyableCode code="organizations_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="organizations_sources_findings_group" /> | `EXEC` | <CopyableCode code="organizationsId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_patch" /> | `EXEC` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="organizations_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="organizations_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Updates the state of a finding. |
| <CopyableCode code="projects_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="projectsId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="projects_sources_findings_group" /> | `EXEC` | <CopyableCode code="projectsId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/&#123;organization_id&#125;/sources/-/findings, /v1/folders/&#123;folder_id&#125;/sources/-/findings, /v1/projects/&#123;project_id&#125;/sources/-/findings |
| <CopyableCode code="projects_sources_findings_patch" /> | `EXEC` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="projects_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="projects_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Updates the state of a finding. |
