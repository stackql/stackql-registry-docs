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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deidentify_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.deidentify_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID` |
| `description` | `string` | Short description (max 256 chars). |
| `displayName` | `string` | Display name (max 256 chars). |
| `updateTime` | `string` | Output only. The last update timestamp of an inspectTemplate. |
| `createTime` | `string` | Output only. The creation timestamp of an inspectTemplate. |
| `deidentifyConfig` | `object` | The configuration that controls how the data will change. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_deidentify_templates_get` | `SELECT` | `deidentifyTemplatesId, organizationsId` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentify_templates_list` | `SELECT` | `organizationsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentify_templates_get` | `SELECT` | `deidentifyTemplatesId, locationsId, organizationsId` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentify_templates_list` | `SELECT` | `locationsId, organizationsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentify_templates_get` | `SELECT` | `deidentifyTemplatesId, projectsId` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentify_templates_list` | `SELECT` | `projectsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentify_templates_get` | `SELECT` | `deidentifyTemplatesId, locationsId, projectsId` | Gets a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentify_templates_list` | `SELECT` | `locationsId, projectsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentify_templates_create` | `INSERT` | `organizationsId` | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentify_templates_create` | `INSERT` | `locationsId, organizationsId` | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentify_templates_create` | `INSERT` | `projectsId` | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentify_templates_create` | `INSERT` | `locationsId, projectsId` | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentify_templates_delete` | `DELETE` | `deidentifyTemplatesId, organizationsId` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentify_templates_delete` | `DELETE` | `deidentifyTemplatesId, locationsId, organizationsId` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentify_templates_delete` | `DELETE` | `deidentifyTemplatesId, projectsId` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentify_templates_delete` | `DELETE` | `deidentifyTemplatesId, locationsId, projectsId` | Deletes a DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `_organizations_deidentify_templates_list` | `EXEC` | `organizationsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `_organizations_locations_deidentify_templates_list` | `EXEC` | `locationsId, organizationsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `_projects_deidentify_templates_list` | `EXEC` | `projectsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `_projects_locations_deidentify_templates_list` | `EXEC` | `locationsId, projectsId` | Lists DeidentifyTemplates. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_deidentify_templates_patch` | `EXEC` | `deidentifyTemplatesId, organizationsId` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `organizations_locations_deidentify_templates_patch` | `EXEC` | `deidentifyTemplatesId, locationsId, organizationsId` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_deidentify_templates_patch` | `EXEC` | `deidentifyTemplatesId, projectsId` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
| `projects_locations_deidentify_templates_patch` | `EXEC` | `deidentifyTemplatesId, locationsId, projectsId` | Updates the DeidentifyTemplate. See https://cloud.google.com/dlp/docs/creating-templates-deid to learn more. |
