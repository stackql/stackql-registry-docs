---
title: certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authorities
  - iam
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.certificate_authorities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description of the certificate authority. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="certificate_chain_filename" /> | `string` | The file name of the uploaded pem file for this certificate authority. |
| <CopyableCode code="crl_source" /> | `string` | The source specifies whether the Certificate Revocation List (CRL) is updated from<br />either local file uploaded (LOCAL) or from url of CRL (URL). |
| <CopyableCode code="crl_updated_at" /> | `string` | The timestamp for when CRL was last updated. |
| <CopyableCode code="crl_url" /> | `string` | The url from which to fetch the CRL for the certificate authority if crl_source is URL. |
| <CopyableCode code="display_name" /> | `string` | The human-readable name of the certificate authority. |
| <CopyableCode code="expiration_dates" /> | `array` | The expiration dates of certificates in the chain. |
| <CopyableCode code="fingerprints" /> | `array` | The fingerprints for each certificate in the certificate chain. These are SHA-1 encoded<br />strings that act as unique identifiers for the certificates in the chain. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="serial_numbers" /> | `array` | The serial numbers for each certificate in the certificate chain. |
| <CopyableCode code="state" /> | `string` | The current state of the certificate authority. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2certificate_authority" /> | `SELECT` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a certificate authority. |
| <CopyableCode code="list_iam_v2certificate_authorities" /> | `SELECT` |  | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all certificate authorities. |
| <CopyableCode code="create_iam_v2certificate_authority" /> | `INSERT` |  | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create a certificate authority. |
| <CopyableCode code="delete_iam_v2certificate_authority" /> | `DELETE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a certificate authority. |
| <CopyableCode code="update_iam_v2certificate_authority" /> | `EXEC` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a certificate authority.<br /><br /> |
