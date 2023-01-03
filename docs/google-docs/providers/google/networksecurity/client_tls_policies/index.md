---
title: client_tls_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - client_tls_policies
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>client_tls_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.client_tls_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/clientTlsPolicies/{client_tls_policy}` |
| `description` | `string` | Optional. Free-text description of the resource. |
| `clientCertificate` | `object` | Specification of certificate provider. Defines the mechanism to obtain the certificate and private key for peer to peer authentication. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `labels` | `object` | Optional. Set of label tags associated with the resource. |
| `serverValidationCa` | `array` | Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate. |
| `sni` | `string` | Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com". |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clientTlsPolicies_get` | `SELECT` | `clientTlsPoliciesId, locationsId, projectsId` | Gets details of a single ClientTlsPolicy. |
| `projects_locations_clientTlsPolicies_list` | `SELECT` | `locationsId, projectsId` | Lists ClientTlsPolicies in a given project and location. |
| `projects_locations_clientTlsPolicies_create` | `INSERT` | `locationsId, projectsId` | Creates a new ClientTlsPolicy in a given project and location. |
| `projects_locations_clientTlsPolicies_delete` | `DELETE` | `clientTlsPoliciesId, locationsId, projectsId` | Deletes a single ClientTlsPolicy. |
| `projects_locations_clientTlsPolicies_patch` | `EXEC` | `clientTlsPoliciesId, locationsId, projectsId` | Updates the parameters of a single ClientTlsPolicy. |
