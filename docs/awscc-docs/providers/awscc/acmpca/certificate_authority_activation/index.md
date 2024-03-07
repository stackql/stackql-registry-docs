---
title: certificate_authority_activation
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority_activation
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
Gets an individual <code>certificate_authority_activation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority_activation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate_authority_activation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.acmpca.certificate_authority_activation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td>Arn of the Certificate Authority.</td></tr>
<tr><td><code>certificate</code></td><td><code>string</code></td><td>Certificate Authority certificate that will be installed in the Certificate Authority.</td></tr>
<tr><td><code>certificate_chain</code></td><td><code>string</code></td><td>Certificate chain for the Certificate Authority certificate.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the Certificate Authority.</td></tr>
<tr><td><code>complete_certificate_chain</code></td><td><code>string</code></td><td>The complete certificate chain, including the Certificate Authority certificate.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_authority_arn,
certificate,
certificate_chain,
status,
complete_certificate_chain
FROM awscc.acmpca.certificate_authority_activation
WHERE region = 'us-east-1'
AND data__Identifier = '{CertificateAuthorityArn}';
```

## Permissions

To operate on the <code>certificate_authority_activation</code> resource, the following permissions are required:

### Read
```json
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:DescribeCertificateAuthority
```

### Delete
```json
acm-pca:UpdateCertificateAuthority
```

### Update
```json
acm-pca:ImportCertificateAuthorityCertificate,
acm-pca:UpdateCertificateAuthority
```

