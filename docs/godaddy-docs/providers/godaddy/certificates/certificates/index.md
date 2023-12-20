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
| `certificate_cancel` | `EXEC` | `certificate_id` | Use the cancel call to cancel a pending certificate order. |
| `certificate_download` | `EXEC` | `certificate_id` | Download certificate |
| `certificate_reissue` | `EXEC` | `certificate_id` | Rekeying is the process by which the private and public key is changed for a certificate. It is a simplified reissue,where only the CSR is changed. Reissuing is the process by which domain  names are added or removed from a certificate.Once a request is validated and approved, the certificate  will be reissued with the new common name and sans specified. Unlimited reissues are available during the  lifetime of the certificate.New names added to a certificate that do not share the base domain of the  common name may take additional time to validate. If this API call is made before a previous pending  reissue has been validated and issued, the previous reissue request is automatically rejected and replaced  with the current request.' |
| `certificate_renew` | `EXEC` | `certificate_id` | Renewal is the process by which the validity of a certificate is extended. Renewal is only available 60 days prior to expiration of the previous certificate and 30 days after the expiration of the previous certificate.  The renewal supports modifying a set of the original certificate order information. Once a request is validated and approved, the certificate  will be issued with extended validity. Since subject alternative names can be removed during a renewal, we  require that you provide the subject alternative names you expect in the renewed certificate. New names added to a certificate that do not share the base domain of the  common name may take additional time to validate.  |
| `certificate_revoke` | `EXEC` | `certificate_id, data__reason` | Use revoke call to revoke an active certificate, if the certificate has not been issued a 404 response will be returned. |
| `certificate_validate` | `EXEC` | `data__contact, data__csr, data__period, data__productType` | Validate a pending order for certificate |
| `certificate_verifydomaincontrol` | `EXEC` | `certificate_id` | Domain control is a means for verifying the domain included in the certificate order. This resource is useful for resellers that control the domains for their customers, and can expedite the verification process. See https://www.godaddy.com/help/verifying-your-domain-ownership-for-ssl-certificate-requests-html-or-dns-7452 |
