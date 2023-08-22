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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Auto generated primary key |
| `description` | `string` | Description of the certificate |
| `credentialId` | `string` | Immutable. Credential id that will be used to register with trawler INTERNAL_ONLY |
| `requestorId` | `string` | Immutable. Requestor ID to be used to register certificate with trawler |
| `validEndTime` | `string` | Output only. The timestamp after which certificate will expire |
| `validStartTime` | `string` | Output only. The timestamp after which certificate will be valid |
| `displayName` | `string` | Required. Name of the certificate |
| `rawCertificate` | `object` | Contains client certificate information |
| `certificateStatus` | `string` | Status of the certificate |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_certificates_get` | `SELECT` | `certificatesId, locationsId, projectsId` | Get a certificates in the specified project. |
| `projects_locations_products_certificates_get` | `SELECT` | `certificatesId, locationsId, productsId, projectsId` | Get a certificates in the specified project. |
| `projects_locations_products_certificates_list` | `SELECT` | `locationsId, productsId, projectsId` | List all the certificates that match the filter. Restrict to certificate of current client only. |
| `projects_locations_products_certificates_create` | `INSERT` | `locationsId, productsId, projectsId` | Creates a new certificate. The certificate will be registered to the trawler service and will be encrypted using cloud KMS and stored in Spanner Returns the certificate. |
| `projects_locations_products_certificates_delete` | `DELETE` | `certificatesId, locationsId, productsId, projectsId` | Delete a certificate |
| `_projects_locations_products_certificates_list` | `EXEC` | `locationsId, productsId, projectsId` | List all the certificates that match the filter. Restrict to certificate of current client only. |
| `projects_locations_products_certificates_patch` | `EXEC` | `certificatesId, locationsId, productsId, projectsId` | Updates the certificate by id. If new certificate file is updated, it will register with the trawler service, re-encrypt with cloud KMS and update the Spanner record. Other fields will directly update the Spanner record. Returns the Certificate. |
