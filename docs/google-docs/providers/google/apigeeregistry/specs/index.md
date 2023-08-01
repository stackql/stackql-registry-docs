---
title: specs
hide_title: false
hide_table_of_contents: false
keywords:
  - specs
  - apigeeregistry
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
<tr><td><b>Name</b></td><td><code>specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.specs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `apiSpecs` | `array` | The specs from the specified publisher. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_versions_specs_list` | `SELECT` | `apisId, locationsId, projectsId, versionsId` | Returns matching specs. |
| `projects_locations_apis_versions_specs_create` | `INSERT` | `apisId, locationsId, projectsId, versionsId` | Creates a specified spec. |
| `projects_locations_apis_versions_specs_delete` | `DELETE` | `apisId, locationsId, projectsId, specsId, versionsId` | Removes a specified spec, all revisions, and all child resources (e.g., artifacts). |
| `projects_locations_apis_versions_specs_get` | `EXEC` | `apisId, locationsId, projectsId, specsId, versionsId` | Returns a specified spec. |
| `projects_locations_apis_versions_specs_patch` | `EXEC` | `apisId, locationsId, projectsId, specsId, versionsId` | Used to modify a specified spec. |
| `projects_locations_apis_versions_specs_rollback` | `EXEC` | `apisId, locationsId, projectsId, specsId, versionsId` | Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| `projects_locations_apis_versions_specs_tag_revision` | `EXEC` | `apisId, locationsId, projectsId, specsId, versionsId` | Adds a tag to a specified revision of a spec. |
