---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - certificates
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.certificates.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a certificate. |
| <CopyableCode code="name" /> | `string` | A unique human-readable name referring to a certificate. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the certificate was created. |
| <CopyableCode code="dns_names" /> | `array` | An array of fully qualified domain names (FQDNs) for which the certificate was issued. |
| <CopyableCode code="not_after" /> | `string` | A time value given in ISO8601 combined date and time format that represents the certificate's expiration date. |
| <CopyableCode code="sha1_fingerprint" /> | `string` | A unique identifier generated from the SHA-1 fingerprint of the certificate. |
| <CopyableCode code="state" /> | `string` | A string representing the current state of the certificate. It may be `pending`, `verified`, or `error`. |
| <CopyableCode code="type" /> | `string` | A string representing the type of the certificate. The value will be `custom` for a user-uploaded certificate or `lets_encrypt` for one automatically generated with Let's Encrypt. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificate_id" /> | To show information about an existing certificate, send a GET request to `/v2/certificates/$CERTIFICATE_ID`. |
| <CopyableCode code="list" /> | `SELECT` |  | To list all of the certificates available on your account, send a GET request to `/v2/certificates`. |
| <CopyableCode code="create" /> | `INSERT` |  | To upload new SSL certificate which you have previously generated, send a POST<br />request to `/v2/certificates`.<br /><br />When uploading a user-generated certificate, the `private_key`,<br />`leaf_certificate`, and optionally the `certificate_chain` attributes should<br />be provided. The type must be set to `custom`.<br /><br />When using Let's Encrypt to create a certificate, the `dns_names` attribute<br />must be provided, and the type must be set to `lets_encrypt`.<br /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificate_id" /> | To delete a specific certificate, send a DELETE request to<br />`/v2/certificates/$CERTIFICATE_ID`.<br /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="certificate_id" /> | To show information about an existing certificate, send a GET request to `/v2/certificates/$CERTIFICATE_ID`. |
| <CopyableCode code="_list" /> | `EXEC` |  | To list all of the certificates available on your account, send a GET request to `/v2/certificates`. |
