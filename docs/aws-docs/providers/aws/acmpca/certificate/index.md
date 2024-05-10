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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>certificate</code> resource, use <code>certificates</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ACMPCA::Certificate`` resource is used to issue a certificate using your private certificate authority. For more information, see the &#91;IssueCertificate&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;privateca&#x2F;latest&#x2F;APIReference&#x2F;API_IssueCertificate.html) action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_passthrough" /></td><td><code>object</code></td><td>Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the private CA issues the certificate.</td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td>The certificate signing request (CSR) for the certificate.</td></tr>
<tr><td><CopyableCode code="signing_algorithm" /></td><td><code>string</code></td><td>The name of the algorithm that will be used to sign the certificate to be issued. &lt;br&#x2F;&gt; This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign a CSR in the ``CreateCertificateAuthority`` action.&lt;br&#x2F;&gt;  The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</td></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td>Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, PCAshort defaults to the ``EndEntityCertificate&#x2F;V1`` template. For more information about PCAshort templates, see &#91;Using Templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;privateca&#x2F;latest&#x2F;userguide&#x2F;UsingTemplates.html).</td></tr>
<tr><td><CopyableCode code="validity" /></td><td><code>object</code></td><td>The period of time during which the certificate will be valid.</td></tr>
<tr><td><CopyableCode code="validity_not_before" /></td><td><code>object</code></td><td>Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate.&lt;br&#x2F;&gt; By default, when issuing a certificate, PCAshort sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The ``ValidityNotBefore`` parameter can be used to customize the “Not Before” value. &lt;br&#x2F;&gt; Unlike the ``Validity`` parameter, the ``ValidityNotBefore`` parameter is optional.&lt;br&#x2F;&gt; The ``ValidityNotBefore`` value is expressed as an explicit date and time, using the ``Validity`` type value ``ABSOLUTE``.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<CertificateAuthorityArn>';
```


## Permissions

To operate on the <code>certificate</code> resource, the following permissions are required:

### Read
```json
acm-pca:GetCertificate
```

