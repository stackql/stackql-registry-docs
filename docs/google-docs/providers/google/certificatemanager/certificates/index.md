---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - certificatemanager
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
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*/locations/*/certificates/*`. |
| `description` | `string` | One or more paragraphs of text description of a certificate. |
| `expireTime` | `string` | Output only. The expiry timestamp of a Certificate. |
| `scope` | `string` | Immutable. The scope of the certificate. |
| `createTime` | `string` | Output only. The creation timestamp of a Certificate. |
| `labels` | `object` | Set of labels associated with a Certificate. |
| `managed` | `object` | Configuration and state of a Managed Certificate. Certificate Manager provisions and renews Managed Certificates automatically, for as long as it's authorized to do so. |
| `updateTime` | `string` | Output only. The last update timestamp of a Certificate. |
| `selfManaged` | `object` | Certificate data for a SelfManaged Certificate. SelfManaged Certificates are uploaded by the user. Updating such certificates before they expire remains the user's responsibility. |
| `pemCertificate` | `string` | Output only. The PEM-encoded certificate chain. |
| `sanDnsnames` | `array` | Output only. The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6). Managed certificates that haven't been provisioned yet have this field populated with a value of the managed.domains field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificatesId, locationsId, projectsId` | Gets details of a single Certificate. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Certificates in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Certificate in a given project and location. |
| `delete` | `DELETE` | `certificatesId, locationsId, projectsId` | Deletes a single Certificate. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Certificates in a given project and location. |
| `patch` | `EXEC` | `certificatesId, locationsId, projectsId` | Updates a Certificate. |
