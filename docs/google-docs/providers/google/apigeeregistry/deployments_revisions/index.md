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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `accessGuidance` | `string` | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. |
| `displayName` | `string` | Human-meaningful name. |
| `revisionCreateTime` | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| `externalChannelUri` | `string` | The address of the external channel of the API (e.g., the Developer Portal). Changes to this value will not affect the revision. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. |
| `endpointUri` | `string` | The address where the deployment is serving. Changes to this value will update the revision. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `intendedAudience` | `string` | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| `apiSpecRevision` | `string` | The full resource name (including revision ID) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/apis/&#123;api&#125;/versions/&#123;version&#125;/specs/&#123;spec@revision&#125;` |
| `createTime` | `string` | Output only. Creation timestamp; when the deployment resource was created. |
| `revisionUpdateTime` | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_apis_deployments_list_revisions` | `SELECT` | `apisId, deploymentsId, locationsId, projectsId` |
| `_projects_locations_apis_deployments_list_revisions` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` |
