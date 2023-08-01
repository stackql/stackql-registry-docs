---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `apiVersions` | `array` | The versions from the specified publisher. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_versions_list` | `SELECT` | `apisId, locationsId, projectsId` | Returns matching versions. |
| `projects_locations_apis_versions_create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a specified version. |
| `projects_locations_apis_versions_delete` | `DELETE` | `apisId, locationsId, projectsId, versionsId` | Removes a specified version and all of the resources that it owns. |
| `projects_locations_apis_versions_get` | `EXEC` | `apisId, locationsId, projectsId, versionsId` | Returns a specified version. |
| `projects_locations_apis_versions_patch` | `EXEC` | `apisId, locationsId, projectsId, versionsId` | Used to modify a specified version. |
