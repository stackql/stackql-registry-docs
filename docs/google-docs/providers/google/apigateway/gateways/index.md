---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigateway.gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Gateway. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/gateways/&#123;gateway&#125; |
| `state` | `string` | Output only. The current state of the Gateway. |
| `updateTime` | `string` | Output only. Updated time. |
| `apiConfig` | `string` | Required. Resource name of the API Config for this Gateway. Format: projects/&#123;project&#125;/locations/global/apis/&#123;api&#125;/configs/&#123;apiConfig&#125; |
| `createTime` | `string` | Output only. Created time. |
| `defaultHostname` | `string` | Output only. The default API Gateway host name of the form `&#123;gateway_id&#125;-&#123;hash&#125;.&#123;region_code&#125;.gateway.dev`. |
| `displayName` | `string` | Optional. Display name. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateways_get` | `SELECT` | `gatewaysId, locationsId, projectsId` | Gets details of a single Gateway. |
| `projects_locations_gateways_list` | `SELECT` | `locationsId, projectsId` | Lists Gateways in a given project and location. |
| `projects_locations_gateways_create` | `INSERT` | `locationsId, projectsId` | Creates a new Gateway in a given project and location. |
| `projects_locations_gateways_delete` | `DELETE` | `gatewaysId, locationsId, projectsId` | Deletes a single Gateway. |
| `projects_locations_gateways_patch` | `EXEC` | `gatewaysId, locationsId, projectsId` | Updates the parameters of a single Gateway. |
