---
title: artifacts_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts_contents
  - apigeeregistry
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.artifacts_contents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extensions` | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
| `contentType` | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| `data` | `string` | The HTTP request/response body as raw binary. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_apis_artifacts_getContents` | `SELECT` | `apisId, artifactsId, locationsId, projectsId` |
| `projects_locations_apis_deployments_artifacts_getContents` | `SELECT` | `apisId, artifactsId, deploymentsId, locationsId, projectsId` |
| `projects_locations_apis_versions_artifacts_getContents` | `SELECT` | `apisId, artifactsId, locationsId, projectsId, versionsId` |
| `projects_locations_apis_versions_specs_artifacts_getContents` | `SELECT` | `apisId, artifactsId, locationsId, projectsId, specsId, versionsId` |
| `projects_locations_artifacts_getContents` | `SELECT` | `artifactsId, locationsId, projectsId` |
