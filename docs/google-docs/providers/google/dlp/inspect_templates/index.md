---
title: inspect_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - inspect_templates
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
<tr><td><b>Name</b></td><td><code>inspect_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dlp.inspect_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`; |
| <CopyableCode code="description" /> | `string` | Short description (max 256 chars). |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of an inspectTemplate. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 256 chars). |
| <CopyableCode code="inspectConfig" /> | `object` | Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of an inspectTemplate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="_organizations_inspect_templates_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="_organizations_locations_inspect_templates_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="_projects_inspect_templates_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="_projects_locations_inspect_templates_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_patch" /> | `EXEC` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_patch" /> | `EXEC` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_patch" /> | `EXEC` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_patch" /> | `EXEC` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
