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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_tls_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.client_tls_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/*/locations/&#123;location&#125;/clientTlsPolicies/&#123;client_tls_policy&#125;` |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="clientCertificate" /> | `object` | Specification of certificate provider. Defines the mechanism to obtain the certificate and private key for peer to peer authentication. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the resource. |
| <CopyableCode code="serverValidationCa" /> | `array` | Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate. |
| <CopyableCode code="sni" /> | `string` | Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com". |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_client_tls_policies_get" /> | `SELECT` | <CopyableCode code="clientTlsPoliciesId, locationsId, projectsId" /> | Gets details of a single ClientTlsPolicy. |
| <CopyableCode code="projects_locations_client_tls_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ClientTlsPolicies in a given project and location. |
| <CopyableCode code="projects_locations_client_tls_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ClientTlsPolicy in a given project and location. |
| <CopyableCode code="projects_locations_client_tls_policies_delete" /> | `DELETE` | <CopyableCode code="clientTlsPoliciesId, locationsId, projectsId" /> | Deletes a single ClientTlsPolicy. |
| <CopyableCode code="_projects_locations_client_tls_policies_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ClientTlsPolicies in a given project and location. |
| <CopyableCode code="projects_locations_client_tls_policies_patch" /> | `EXEC` | <CopyableCode code="clientTlsPoliciesId, locationsId, projectsId" /> | Updates the parameters of a single ClientTlsPolicy. |
