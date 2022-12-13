---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - iot_hub
  - azure    
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The name of the certificate. |
| `properties` | `object` | The description of an X509 CA Certificate. |
| `type` | `string` | The resource type. |
| `etag` | `string` | The entity tag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificates_Get` | `SELECT` | `api-version, certificateName, resourceGroupName, resourceName, subscriptionId` | Returns the certificate. |
| `Certificates_ListByIotHub` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Returns the list of certificates. |
| `Certificates_CreateOrUpdate` | `INSERT` | `api-version, certificateName, resourceGroupName, resourceName, subscriptionId` | Adds new or replaces existing certificate. |
| `Certificates_Delete` | `DELETE` | `If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId` | Deletes an existing X509 certificate or does nothing if it does not exist. |
| `Certificates_GenerateVerificationCode` | `EXEC` | `If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId` | Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate. |
| `Certificates_Verify` | `EXEC` | `If-Match, api-version, certificateName, resourceGroupName, resourceName, subscriptionId` | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |
