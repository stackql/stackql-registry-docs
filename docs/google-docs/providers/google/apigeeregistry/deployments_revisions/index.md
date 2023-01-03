---
title: deployments_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_revisions
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
<tr><td><b>Name</b></td><td><code>deployments_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.deployments_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name. |
| `description` | `string` | A detailed description. |
| `intendedAudience` | `string` | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `revisionUpdateTime` | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
| `endpointUri` | `string` | The address where the deployment is serving. Changes to this value will update the revision. |
| `displayName` | `string` | Human-meaningful name. |
| `externalChannelUri` | `string` | The address of the external channel of the API (e.g. the Developer Portal). Changes to this value will not affect the revision. |
| `apiSpecRevision` | `string` | The full resource name (including revision id) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: apis/{api}/deployments/{deployment} |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "apigeeregistry.googleapis.com/" and cannot be changed. |
| `createTime` | `string` | Output only. Creation timestamp; when the deployment resource was created. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. |
| `revisionCreateTime` | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| `accessGuidance` | `string` | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_apis_deployments_listRevisions` | `SELECT` | `apisId, deploymentsId, locationsId, projectsId` |
