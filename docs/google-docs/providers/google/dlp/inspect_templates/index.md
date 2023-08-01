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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inspect_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.inspect_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inspectTemplates` | `array` | List of inspectTemplates, up to page_size in ListInspectTemplatesRequest. |
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListInspectTemplates request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_inspect_templates_get` | `SELECT` | `inspectTemplatesId, organizationsId` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspect_templates_list` | `SELECT` | `organizationsId` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspect_templates_get` | `SELECT` | `inspectTemplatesId, locationsId, organizationsId` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspect_templates_list` | `SELECT` | `locationsId, organizationsId` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspect_templates_get` | `SELECT` | `inspectTemplatesId, projectsId` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspect_templates_list` | `SELECT` | `projectsId` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspect_templates_get` | `SELECT` | `inspectTemplatesId, locationsId, projectsId` | Gets an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspect_templates_list` | `SELECT` | `locationsId, projectsId` | Lists InspectTemplates. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspect_templates_create` | `INSERT` | `organizationsId` | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspect_templates_create` | `INSERT` | `locationsId, organizationsId` | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspect_templates_create` | `INSERT` | `projectsId` | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspect_templates_create` | `INSERT` | `locationsId, projectsId` | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspect_templates_delete` | `DELETE` | `inspectTemplatesId, organizationsId` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspect_templates_delete` | `DELETE` | `inspectTemplatesId, locationsId, organizationsId` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspect_templates_delete` | `DELETE` | `inspectTemplatesId, projectsId` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspect_templates_delete` | `DELETE` | `inspectTemplatesId, locationsId, projectsId` | Deletes an InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_inspect_templates_patch` | `EXEC` | `inspectTemplatesId, organizationsId` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `organizations_locations_inspect_templates_patch` | `EXEC` | `inspectTemplatesId, locationsId, organizationsId` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_inspect_templates_patch` | `EXEC` | `inspectTemplatesId, projectsId` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
| `projects_locations_inspect_templates_patch` | `EXEC` | `inspectTemplatesId, locationsId, projectsId` | Updates the InspectTemplate. See https://cloud.google.com/dlp/docs/creating-templates to learn more. |
