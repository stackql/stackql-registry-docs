---
title: dps_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - dps_certificate
  - devices
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dps_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.devices.dps_certificate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The name of the certificate. |
| `etag` | `string` | The entity tag. |
| `properties` | `object` | The description of an X509 CA Certificate. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DpsCertificate_Get` | `SELECT` | `api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId` | Get the certificate from the provisioning service. |
| `DpsCertificate_List` | `SELECT` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Get all the certificates tied to the provisioning service. |
| `DpsCertificate_CreateOrUpdate` | `INSERT` | `api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId` | Add new certificate or update an existing certificate. |
| `DpsCertificate_Delete` | `DELETE` | `If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId` | Deletes the specified certificate associated with the Provisioning Service |
| `DpsCertificate_GenerateVerificationCode` | `EXEC` | `If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId` | Generate verification code for Proof of Possession. |
| `DpsCertificate_VerifyCertificate` | `EXEC` | `If-Match, api-version, certificateName, provisioningServiceName, resourceGroupName, subscriptionId` | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |
