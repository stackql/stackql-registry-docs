---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `displayName` | `string` | Human-meaningful name. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `recommendedVersion` | `string` | The recommended version of the API. Format: apis/{api}/versions/{version} |
| `recommendedDeployment` | `string` | The recommended deployment of the API. Format: apis/{api}/deployments/{deployment} |
| `availability` | `string` | A user-definable description of the availability of this service. Format: free-form, but we expect single words that describe availability, e.g. "NONE", "TESTING", "PREVIEW", "GENERAL", "DEPRECATED", "SHUTDOWN". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_get` | `SELECT` | `apisId, locationsId, projectsId` | GetApi returns a specified API. |
| `projects_locations_apis_list` | `SELECT` | `locationsId, projectsId` | ListApis returns matching APIs. |
| `projects_locations_apis_create` | `INSERT` | `locationsId, projectsId` | CreateApi creates a specified API. |
| `projects_locations_apis_delete` | `DELETE` | `apisId, locationsId, projectsId` | DeleteApi removes a specified API and all of the resources that it owns. |
| `projects_locations_apis_patch` | `EXEC` | `apisId, locationsId, projectsId` | UpdateApi can be used to modify a specified API. |
