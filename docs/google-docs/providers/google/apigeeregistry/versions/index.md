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
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `displayName` | `string` | Human-meaningful name. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| `state` | `string` | A user-definable description of the lifecycle phase of this API version. Format: free-form, but we expect single words that describe API maturity, e.g., "CONCEPT", "DESIGN", "DEVELOPMENT", "STAGING", "PRODUCTION", "DEPRECATED", "RETIRED". |
| `updateTime` | `string` | Output only. Last update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_versions_get` | `SELECT` | `apisId, locationsId, projectsId, versionsId` | Returns a specified version. |
| `projects_locations_apis_versions_list` | `SELECT` | `apisId, locationsId, projectsId` | Returns matching versions. |
| `projects_locations_apis_versions_create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a specified version. |
| `projects_locations_apis_versions_delete` | `DELETE` | `apisId, locationsId, projectsId, versionsId` | Removes a specified version and all of the resources that it owns. |
| `projects_locations_apis_versions_patch` | `EXEC` | `apisId, locationsId, projectsId, versionsId` | Used to modify a specified version. |
