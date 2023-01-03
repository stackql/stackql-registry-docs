---
title: realms
hide_title: false
hide_table_of_contents: false
keywords:
  - realms
  - gameservices
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
<tr><td><b>Name</b></td><td><code>realms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.realms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the realm, in the following form: `projects/{project}/locations/{locationId}/realms/{realmId}`. For example, `projects/my-project/locations/global/realms/my-realm`. |
| `description` | `string` | Human readable description of the realm. |
| `createTime` | `string` | Output only. The creation time. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | The labels associated with this realm. Each label is a key-value pair. |
| `timeZone` | `string` | Required. Time zone where all policies targeting this realm are evaluated. The value of this field must be from the [IANA time zone database](https://www.iana.org/time-zones). |
| `updateTime` | `string` | Output only. The last-modified time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_realms_get` | `SELECT` | `locationsId, projectsId, realmsId` | Gets details of a single realm. |
| `projects_locations_realms_list` | `SELECT` | `locationsId, projectsId` | Lists realms in a given project and location. |
| `projects_locations_realms_create` | `INSERT` | `locationsId, projectsId` | Creates a new realm in a given project and location. |
| `projects_locations_realms_delete` | `DELETE` | `locationsId, projectsId, realmsId` | Deletes a single realm. |
| `projects_locations_realms_patch` | `EXEC` | `locationsId, projectsId, realmsId` | Patches a single realm. |
| `projects_locations_realms_previewUpdate` | `EXEC` | `locationsId, projectsId, realmsId` | Previews patches to a single realm. |
