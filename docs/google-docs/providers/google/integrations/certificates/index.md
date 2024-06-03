---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - integrations
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Auto generated primary key |
| <CopyableCode code="description" /> | `string` | Description of the certificate |
| <CopyableCode code="certificateStatus" /> | `string` | Status of the certificate |
| <CopyableCode code="credentialId" /> | `string` | Immutable. Credential id that will be used to register with trawler INTERNAL_ONLY |
| <CopyableCode code="displayName" /> | `string` | Required. Name of the certificate |
| <CopyableCode code="rawCertificate" /> | `object` | Contains client certificate information |
| <CopyableCode code="requestorId" /> | `string` | Immutable. Requestor ID to be used to register certificate with trawler |
| <CopyableCode code="validEndTime" /> | `string` | Output only. The timestamp after which certificate will expire |
| <CopyableCode code="validStartTime" /> | `string` | Output only. The timestamp after which certificate will be valid |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_certificates_get" /> | `SELECT` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Get a certificates in the specified project. |
| <CopyableCode code="projects_locations_certificates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all the certificates that match the filter. Restrict to certificate of current client only. |
| <CopyableCode code="projects_locations_products_certificates_get" /> | `SELECT` | <CopyableCode code="certificatesId, locationsId, productsId, projectsId" /> | Get a certificates in the specified project. |
| <CopyableCode code="projects_locations_products_certificates_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | List all the certificates that match the filter. Restrict to certificate of current client only. |
| <CopyableCode code="projects_locations_certificates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new certificate. The certificate will be registered to the trawler service and will be encrypted using cloud KMS and stored in Spanner Returns the certificate. |
| <CopyableCode code="projects_locations_products_certificates_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates a new certificate. The certificate will be registered to the trawler service and will be encrypted using cloud KMS and stored in Spanner Returns the certificate. |
| <CopyableCode code="projects_locations_certificates_delete" /> | `DELETE` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Delete a certificate |
| <CopyableCode code="projects_locations_products_certificates_delete" /> | `DELETE` | <CopyableCode code="certificatesId, locationsId, productsId, projectsId" /> | Delete a certificate |
| <CopyableCode code="projects_locations_certificates_patch" /> | `UPDATE` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Updates the certificate by id. If new certificate file is updated, it will register with the trawler service, re-encrypt with cloud KMS and update the Spanner record. Other fields will directly update the Spanner record. Returns the Certificate. |
| <CopyableCode code="projects_locations_products_certificates_patch" /> | `UPDATE` | <CopyableCode code="certificatesId, locationsId, productsId, projectsId" /> | Updates the certificate by id. If new certificate file is updated, it will register with the trawler service, re-encrypt with cloud KMS and update the Spanner record. Other fields will directly update the Spanner record. Returns the Certificate. |
| <CopyableCode code="_projects_locations_certificates_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all the certificates that match the filter. Restrict to certificate of current client only. |
| <CopyableCode code="_projects_locations_products_certificates_list" /> | `EXEC` | <CopyableCode code="locationsId, productsId, projectsId" /> | List all the certificates that match the filter. Restrict to certificate of current client only. |
