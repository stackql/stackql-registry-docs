
---
title: domains_ldapssettings
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_ldapssettings
  - managedidentities
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>domains_ldapssetting</code> resource or lists <code>domains_ldapssettings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_ldapssettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.managedidentities.domains_ldapssettings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the LDAPS settings. Uses the form: `projects/{project}/locations/{location}/domains/{domain}`. |
| <CopyableCode code="certificate" /> | `object` | Certificate used to configure LDAPS. |
| <CopyableCode code="certificatePassword" /> | `string` | Input only. The password used to encrypt the uploaded PFX certificate. |
| <CopyableCode code="certificatePfx" /> | `string` | Input only. The uploaded PKCS12-formatted certificate to configure LDAPS with. It will enable the domain controllers in this domain to accept LDAPS connections (either LDAP over SSL/TLS or the StartTLS operation). A valid certificate chain must form a valid x.509 certificate chain (or be comprised of a single self-signed certificate. It must be encrypted with either: 1) PBES2 + PBKDF2 + AES256 encryption and SHA256 PRF; or 2) pbeWithSHA1And3-KeyTripleDES-CBC Private key must be included for the leaf / single self-signed certificate. Note: For a fqdn your-example-domain.com, the wildcard fqdn is *.your-example-domain.com. Specifically the leaf certificate must have: - Either a blank subject or a subject with CN matching the wildcard fqdn. - Exactly two SANs - the fqdn and wildcard fqdn. - Encipherment and digital key signature key usages. - Server authentication extended key usage (OID=1.3.6.1.5.5.7.3.1) - Private key must be in one of the following formats: RSA, ECDSA, ED25519. - Private key must have appropriate key length: 2048 for RSA, 256 for ECDSA - Signature algorithm of the leaf certificate cannot be MD2, MD5 or SHA1. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of this LDAPS settings. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ldapssettings" /> | `SELECT` | <CopyableCode code="domainsId, projectsId" /> | Gets the domain ldaps settings. |
| <CopyableCode code="update_ldapssettings" /> | `UPDATE` | <CopyableCode code="domainsId, projectsId" /> | Patches a single ldaps settings. |

## `SELECT` examples

Gets the domain ldaps settings.

```sql
SELECT
name,
certificate,
certificatePassword,
certificatePfx,
state,
updateTime
FROM google.managedidentities.domains_ldapssettings
WHERE domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a domains_ldapssetting only if the necessary resources are available.

```sql
UPDATE google.managedidentities.domains_ldapssettings
SET 
name = '{{ name }}',
certificate = '{{ certificate }}',
state = '{{ state }}',
certificatePfx = '{{ certificatePfx }}',
certificatePassword = '{{ certificatePassword }}',
updateTime = '{{ updateTime }}'
WHERE 
domainsId = '{{ domainsId }}'
AND projectsId = '{{ projectsId }}';
```
