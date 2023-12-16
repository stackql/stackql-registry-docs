---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - certificates
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.certificates.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `certificateId` | `string` | The unique identifier of the certificate request. Only present if no errors returned |
| `commonName` | `string` | Common name of certificate |
| `contact` | `object` |  |
| `createdAt` | `string` | The date the certificate was ordered. |
| `deniedReason` | `string` | Only present if certificate order has been denied |
| `organization` | `object` |  |
| `period` | `integer` | Validity period of order. Specified in years |
| `productType` | `string` | Certificate product type |
| `progress` | `integer` | Percentage of completion for certificate vetting |
| `revokedAt` | `string` | The revocation date of certificate (if revoked). |
| `rootType` | `string` | Root Type |
| `serialNumber` | `string` | Serial number of certificate (if issued or revoked) |
| `serialNumberHex` | `string` | Hexadecmial format for Serial number of certificate(if issued or revoked) |
| `slotSize` | `string` | Number of subject alternative names(SAN) to be included in certificate  |
| `status` | `string` | Status of certificate |
| `subjectAlternativeNames` | `array` | Contains subject alternative names set |
| `validEnd` | `string` | The end date of the certificate's validity (if issued or revoked). |
| `validStart` | `string` | The start date of the certificate's validity (if issued or revoked). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `certificate_get` | `SELECT` | `certificate_id` | Once the certificate order has been created, this method can be used to check the status of the certificate. This method can also be used to retrieve details of the certificate. |
| `certificate_create` | `INSERT` | `data__contact, data__csr, data__period, data__productType` | Creating a certificate order can be a long running asynchronous operation in the PKI workflow. The PKI API supports 2 options for getting the completion stateful actions for this asynchronous operations: 1) by polling operations -- see /v1/certificates/&#123;certificateId&#125;/actions 2) via WebHook style callback -- see '/v1/certificates/&#123;certificateId&#125;/callback'. |
