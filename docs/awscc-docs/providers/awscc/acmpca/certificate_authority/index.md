---
title: certificate_authority
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority
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
Gets an individual <code>certificate_authority</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate_authority</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.acmpca.certificate_authority</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the certificate authority.</td></tr>
<tr><td><code>key_algorithm</code></td><td><code>string</code></td><td>Public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.</td></tr>
<tr><td><code>signing_algorithm</code></td><td><code>string</code></td><td>Algorithm your CA uses to sign certificate requests.</td></tr>
<tr><td><code>subject</code></td><td><code>object</code></td><td>Structure that contains X.500 distinguished name information for your CA.</td></tr>
<tr><td><code>revocation_configuration</code></td><td><code>object</code></td><td>Certificate revocation information used by the CreateCertificateAuthority and UpdateCertificateAuthority actions.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>certificate_signing_request</code></td><td><code>string</code></td><td>The base64 PEM-encoded certificate signing request (CSR) for your certificate authority certificate.</td></tr>
<tr><td><code>csr_extensions</code></td><td><code>object</code></td><td>Structure that contains CSR pass through extension information used by the CreateCertificateAuthority action.</td></tr>
<tr><td><code>key_storage_security_standard</code></td><td><code>string</code></td><td>KeyStorageSecurityStadard defines a cryptographic key management compliance standard used for handling CA keys.</td></tr>
<tr><td><code>usage_mode</code></td><td><code>string</code></td><td>Usage mode of the ceritificate authority.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>certificate_authority</code> resource, the following permissions are required:

### Read
<pre>
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr,
acm-pca:ListTags</pre>

### Update
<pre>
acm-pca:ListTags,
acm-pca:TagCertificateAuthority,
acm-pca:UntagCertificateAuthority,
acm-pca:UpdateCertificateAuthority</pre>

### Delete
<pre>
acm-pca:DeleteCertificateAuthority,
acm-pca:DescribeCertificateAuthority</pre>


## Example
```sql
SELECT
region,
arn,
type,
key_algorithm,
signing_algorithm,
subject,
revocation_configuration,
tags,
certificate_signing_request,
csr_extensions,
key_storage_security_standard,
usage_mode
FROM awscc.acmpca.certificate_authority
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
