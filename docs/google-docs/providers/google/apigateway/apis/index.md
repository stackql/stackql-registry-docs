---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - apigateway
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.apis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the API. Format: projects/&#123;project&#125;/locations/global/apis/&#123;api&#125; |
| `updateTime` | `string` | Output only. Updated time. |
| `createTime` | `string` | Output only. Created time. |
| `displayName` | `string` | Optional. Display name. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `managedService` | `string` | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. |
| `state` | `string` | Output only. State of the API. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apisId, locationsId, projectsId` | Gets details of a single Api. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Apis in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Api in a given project and location. |
| `delete` | `DELETE` | `apisId, locationsId, projectsId` | Deletes a single Api. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Apis in a given project and location. |
| `patch` | `EXEC` | `apisId, locationsId, projectsId` | Updates the parameters of a single Api. |
