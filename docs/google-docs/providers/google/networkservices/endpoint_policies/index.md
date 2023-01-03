---
title: endpoint_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_policies
  - networkservices
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
<tr><td><b>Name</b></td><td><code>endpoint_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.endpoint_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the EndpointPolicy resource. It matches pattern `projects/{project}/locations/global/endpointPolicies/{endpoint_policy}`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `clientTlsPolicy` | `string` | Optional. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set to specify the authentication for traffic from the proxy to the actual endpoints. More specifically, it is applied to the outgoing traffic from the proxy to the endpoint. This is typically used for sidecar model where the proxy identifies itself as endpoint to the control plane, with the connection between sidecar and endpoint requiring authentication. If this field is not set, authentication is disabled(open). Applicable only when EndpointPolicyType is SIDECAR_PROXY. |
| `labels` | `object` | Optional. Set of label tags associated with the EndpointPolicy resource. |
| `serverTlsPolicy` | `string` | Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to determine the authentication policy to be applied to terminate the inbound traffic at the identified backends. If this field is not set, authentication is disabled(open) for this endpoint. |
| `type` | `string` | Required. The type of endpoint policy. This is primarily used to validate the configuration. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `authorizationPolicy` | `string` | Optional. This field specifies the URL of AuthorizationPolicy resource that applies authorization policies to the inbound traffic at the matched endpoints. Refer to Authorization. If this field is not specified, authorization is disabled(no authz checks) for this endpoint. |
| `endpointMatcher` | `object` | A definition of a matcher that selects endpoints to which the policies should be applied. |
| `trafficPortSelector` | `object` | Specification of a port-based selector. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_endpointPolicies_get` | `SELECT` | `endpointPoliciesId, locationsId, projectsId` | Gets details of a single EndpointPolicy. |
| `projects_locations_endpointPolicies_list` | `SELECT` | `locationsId, projectsId` | Lists EndpointPolicies in a given project and location. |
| `projects_locations_endpointPolicies_create` | `INSERT` | `locationsId, projectsId` | Creates a new EndpointPolicy in a given project and location. |
| `projects_locations_endpointPolicies_delete` | `DELETE` | `endpointPoliciesId, locationsId, projectsId` | Deletes a single EndpointPolicy. |
| `projects_locations_endpointPolicies_patch` | `EXEC` | `endpointPoliciesId, locationsId, projectsId` | Updates the parameters of a single EndpointPolicy. |
