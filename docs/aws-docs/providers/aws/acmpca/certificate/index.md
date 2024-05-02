---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
Gets an individual <code>certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ACMPCA::Certificate`` resource is used to issue a certificate using your private certificate authority. For more information, see the &#91;IssueCertificate&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;privateca&#x2F;latest&#x2F;APIReference&#x2F;API_IssueCertificate.html) action.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.acmpca.certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_passthrough</code></td><td><code>object</code></td><td>Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.</td></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the private CA issues the certificate.</td></tr>
<tr><td><code>certificate_signing_request</code></td><td><code>string</code></td><td>The certificate signing request (CSR) for the certificate.</td></tr>
<tr><td><code>signing_algorithm</code></td><td><code>string</code></td><td>The name of the algorithm that will be used to sign the certificate to be issued. &lt;br&#x2F;&gt; This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign a CSR in the ``CreateCertificateAuthority`` action.&lt;br&#x2F;&gt;  The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</td></tr>
<tr><td><code>template_arn</code></td><td><code>string</code></td><td>Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, PCAshort defaults to the ``EndEntityCertificate&#x2F;V1`` template. For more information about PCAshort templates, see &#91;Using Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;privateca&#x2F;latest&#x2F;userguide&#x2F;UsingTemplates.html).</td></tr>
<tr><td><code>validity</code></td><td><code>object</code></td><td>The period of time during which the certificate will be valid.</td></tr>
<tr><td><code>validity_not_before</code></td><td><code>object</code></td><td>Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate.&lt;br&#x2F;&gt; By default, when issuing a certificate, PCAshort sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The ``ValidityNotBefore`` parameter can be used to customize the “Not Before” value. &lt;br&#x2F;&gt; Unlike the ``Validity`` parameter, the ``ValidityNotBefore`` parameter is optional.&lt;br&#x2F;&gt; The ``ValidityNotBefore`` value is expressed as an explicit date and time, using the ``Validity`` type value ``ABSOLUTE``.</td></tr>
<tr><td><code>certificate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
api_passthrough,
certificate_authority_arn,
certificate_signing_request,
signing_algorithm,
template_arn,
validity,
validity_not_before,
certificate,
arn
FROM aws.acmpca.certificate
WHERE data__Identifier = '<Arn>|<CertificateAuthorityArn>';
```

## Permissions

To operate on the <code>certificate</code> resource, the following permissions are required:

### Read
```json
acm-pca:GetCertificate
```

### Delete
```json
acm-pca:GetCertificate
```

