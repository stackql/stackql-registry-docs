---
title: deidentify_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - deidentify_templates
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
<tr><td><b>Name</b></td><td><code>deidentify_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.deidentify_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID` |
| <CopyableCode code="description" /> | `string` | Short description (max 256 chars). |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of an inspectTemplate. |
| <CopyableCode code="deidentifyConfig" /> | `object` | The configuration that controls how the data will change. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 256 chars). |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of an inspectTemplate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="_organizations_deidentify_templates_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="_organizations_locations_deidentify_templates_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="_projects_deidentify_templates_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="_projects_locations_deidentify_templates_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_patch" /> | `EXEC` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_patch" /> | `EXEC` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_patch" /> | `EXEC` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_patch" /> | `EXEC` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
