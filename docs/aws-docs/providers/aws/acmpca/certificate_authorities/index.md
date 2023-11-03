---
title: certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authorities
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
Retrieves a list of <code>certificate_authorities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.acmpca.certificate_authorities</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the certificate authority.</td></tr><tr><td><code>KeyAlgorithm</code></td><td><code>string</code></td><td>Public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.</td></tr><tr><td><code>SigningAlgorithm</code></td><td><code>string</code></td><td>Algorithm your CA uses to sign certificate requests.</td></tr><tr><td><code>Subject</code></td><td><code>undefined</code></td><td>Structure that contains X.500 distinguished name information for your CA.</td></tr><tr><td><code>RevocationConfiguration</code></td><td><code>undefined</code></td><td>Certificate revocation information used by the CreateCertificateAuthority and UpdateCertificateAuthority actions.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>CertificateSigningRequest</code></td><td><code>string</code></td><td>The base64 PEM-encoded certificate signing request (CSR) for your certificate authority certificate.</td></tr><tr><td><code>CsrExtensions</code></td><td><code>undefined</code></td><td>Structure that contains CSR pass through extension information used by the CreateCertificateAuthority action.</td></tr><tr><td><code>KeyStorageSecurityStandard</code></td><td><code>string</code></td><td>KeyStorageSecurityStadard defines a cryptographic key management compliance standard used for handling CA keys.</td></tr><tr><td><code>UsageMode</code></td><td><code>string</code></td><td>Usage mode of the ceritificate authority.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.acmpca.certificate_authorities
WHERE region = 'us-east-1'
</pre>
