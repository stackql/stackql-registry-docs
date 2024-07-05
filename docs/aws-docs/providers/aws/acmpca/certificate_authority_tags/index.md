---
title: certificate_authority_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority_tags
  - acmpca
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>certificate_authorities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Private certificate authority.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate_authority_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the certificate authority.</td></tr>
<tr><td><CopyableCode code="key_algorithm" /></td><td><code>string</code></td><td>Public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.</td></tr>
<tr><td><CopyableCode code="signing_algorithm" /></td><td><code>string</code></td><td>Algorithm your CA uses to sign certificate requests.</td></tr>
<tr><td><CopyableCode code="subject" /></td><td><code>object</code></td><td>Structure that contains X.500 distinguished name information for your CA.</td></tr>
<tr><td><CopyableCode code="revocation_configuration" /></td><td><code>object</code></td><td>Certificate revocation information used by the CreateCertificateAuthority and UpdateCertificateAuthority actions.</td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td>The base64 PEM-encoded certificate signing request (CSR) for your certificate authority certificate.</td></tr>
<tr><td><CopyableCode code="csr_extensions" /></td><td><code>object</code></td><td>Structure that contains CSR pass through extension information used by the CreateCertificateAuthority action.</td></tr>
<tr><td><CopyableCode code="key_storage_security_standard" /></td><td><code>string</code></td><td>KeyStorageSecurityStadard defines a cryptographic key management compliance standard used for handling CA keys.</td></tr>
<tr><td><CopyableCode code="usage_mode" /></td><td><code>string</code></td><td>Usage mode of the ceritificate authority.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>certificate_authorities</code> in a region.
```sql
SELECT
region,
arn,
type,
key_algorithm,
signing_algorithm,
subject,
revocation_configuration,
certificate_signing_request,
csr_extensions,
key_storage_security_standard,
usage_mode,
tag_key,
tag_value
FROM aws.acmpca.certificate_authority_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>certificate_authority_tags</code> resource, see <a href="/providers/aws/acmpca/certificate_authorities/#permissions"><code>certificate_authorities</code></a>


