---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - connectors
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
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Connector. Format: projects/{project}/locations/{location}/providers/{provider}/connectors/{connector} |
| `description` | `string` | Output only. Description of the resource. |
| `updateTime` | `string` | Output only. Updated time. |
| `labels` | `object` | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `externalUri` | `string` | Output only. Link to external page. |
| `displayName` | `string` | Output only. Display name. |
| `documentationUri` | `string` | Output only. Link to documentation page. |
| `createTime` | `string` | Output only. Created time. |
| `launchStage` | `string` | Output only. Flag to mark the version indicating the launch stage. |
| `webAssetsLocation` | `string` | Output only. Cloud storage location of icons etc consumed by UI. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_providers_connectors_get` | `SELECT` | `connectorsId, projectsId, providersId` | Gets details of a single Connector. |
| `projects_locations_global_providers_connectors_list` | `SELECT` | `projectsId, providersId` | Lists Connectors in a given project and location. |
