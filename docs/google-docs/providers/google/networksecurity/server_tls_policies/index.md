---
title: server_tls_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_tls_policies
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>server_tls_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.server_tls_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/&#123;location&#125;/serverTlsPolicies/&#123;server_tls_policy&#125;` |
| `description` | `string` | Free-text description of the resource. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `allowOpen` | `boolean` | This field applies only for Traffic Director policies. It is must be set to false for external HTTPS load balancer policies. Determines if server allows plaintext connections. If set to true, server allows plain text connections. By default, it is set to false. This setting is not exclusive of other encryption modes. For example, if `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections. See documentation of other encryption modes to confirm compatibility. Consider using it if you wish to upgrade in place your deployment to TLS while having mixed TLS and non-TLS traffic reaching port :80. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `labels` | `object` | Set of label tags associated with the resource. |
| `mtlsPolicy` | `object` | Specification of the MTLSPolicy. |
| `serverCertificate` | `object` | Specification of certificate provider. Defines the mechanism to obtain the certificate and private key for peer to peer authentication. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_server_tls_policies_get` | `SELECT` | `locationsId, projectsId, serverTlsPoliciesId` | Gets details of a single ServerTlsPolicy. |
| `projects_locations_server_tls_policies_list` | `SELECT` | `locationsId, projectsId` | Lists ServerTlsPolicies in a given project and location. |
| `projects_locations_server_tls_policies_create` | `INSERT` | `locationsId, projectsId` | Creates a new ServerTlsPolicy in a given project and location. |
| `projects_locations_server_tls_policies_delete` | `DELETE` | `locationsId, projectsId, serverTlsPoliciesId` | Deletes a single ServerTlsPolicy. |
| `_projects_locations_server_tls_policies_list` | `EXEC` | `locationsId, projectsId` | Lists ServerTlsPolicies in a given project and location. |
| `projects_locations_server_tls_policies_patch` | `EXEC` | `locationsId, projectsId, serverTlsPoliciesId` | Updates the parameters of a single ServerTlsPolicy. |
