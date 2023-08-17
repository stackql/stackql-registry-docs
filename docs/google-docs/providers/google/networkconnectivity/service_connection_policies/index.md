---
title: service_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_policies
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>service_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_connection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of a ServiceConnectionPolicy. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/serviceConnectionPolicies/&#123;service_connection_policy&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| `description` | `string` | A description of this resource. |
| `infrastructure` | `string` | Output only. The type of underlying resources used to create the connection. |
| `serviceClass` | `string` | The service class identifier for which this ServiceConnectionPolicy is for. The service class identifier is a unique, symbolic representation of a ServiceClass. It is provided by the Service Producer. Google services have a prefix of gcp. For example, gcp-cloud-sql. 3rd party services do not. For example, test-service-a3dfcx. |
| `updateTime` | `string` | Output only. Time when the ServiceConnectionMap was updated. |
| `labels` | `object` | User-defined labels. |
| `network` | `string` | The resource path of the consumer network. Example: - projects/&#123;projectNumOrId&#125;/global/networks/&#123;resourceId&#125;. |
| `pscConnections` | `array` | Output only. [Output only] Information about each Private Service Connect connection. |
| `createTime` | `string` | Output only. Time when the ServiceConnectionMap was created. |
| `etag` | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `pscConfig` | `object` | Configuration used for Private Service Connect connections. Used when Infrastructure is PSC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceConnectionPoliciesId` | Gets details of a single ServiceConnectionPolicy. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceConnectionPolicies in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceConnectionPolicy in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceConnectionPoliciesId` | Deletes a single ServiceConnectionPolicy. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ServiceConnectionPolicies in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceConnectionPoliciesId` | Updates the parameters of a single ServiceConnectionPolicy. |
