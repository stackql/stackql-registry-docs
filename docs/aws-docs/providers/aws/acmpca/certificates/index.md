---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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

Creates, updates, deletes or gets a <code>certificate</code> resource or lists <code>certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ACMPCA::Certificate</code> resource is used to issue a certificate using your private certificate authority. For more information, see the &#91;IssueCertificate&#93;(https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_passthrough" /></td><td><code>object</code></td><td>Specifies X.509 certificate information to be included in the issued certificate. An <code>APIPassthrough</code> or <code>APICSRPassthrough</code> template variant must be selected, or else this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the private CA issues the certificate.</td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td>The certificate signing request (CSR) for the certificate.</td></tr>
<tr><td><CopyableCode code="signing_algorithm" /></td><td><code>string</code></td><td>The name of the algorithm that will be used to sign the certificate to be issued. This parameter should not be confused with the <code>SigningAlgorithm</code> parameter used to sign a CSR in the <code>CreateCertificateAuthority</code> action. The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.</td></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td>Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, PCAshort defaults to the <code>EndEntityCertificate/V1</code> template. For more information about PCAshort templates, see &#91;Using Templates&#93;(https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html).</td></tr>
<tr><td><CopyableCode code="validity" /></td><td><code>object</code></td><td>The period of time during which the certificate will be valid.</td></tr>
<tr><td><CopyableCode code="validity_not_before" /></td><td><code>object</code></td><td>Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate. By default, when issuing a certificate, PCAshort sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The <code>ValidityNotBefore</code> parameter can be used to customize the “Not Before” value. Unlike the <code>Validity</code> parameter, the <code>ValidityNotBefore</code> parameter is optional. The <code>ValidityNotBefore</code> value is expressed as an explicit date and time, using the <code>Validity</code> type value <code>ABSOLUTE</code>.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="CertificateAuthorityArn, CertificateSigningRequest, SigningAlgorithm, Validity, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>certificate</code>.
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
FROM aws.acmpca.certificates
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<CertificateAuthorityArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.acmpca.certificates (
 CertificateAuthorityArn,
 CertificateSigningRequest,
 SigningAlgorithm,
 Validity,
 region
)
SELECT 
'{{ CertificateAuthorityArn }}',
 '{{ CertificateSigningRequest }}',
 '{{ SigningAlgorithm }}',
 '{{ Validity }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.acmpca.certificates (
 ApiPassthrough,
 CertificateAuthorityArn,
 CertificateSigningRequest,
 SigningAlgorithm,
 TemplateArn,
 Validity,
 ValidityNotBefore,
 region
)
SELECT 
 '{{ ApiPassthrough }}',
 '{{ CertificateAuthorityArn }}',
 '{{ CertificateSigningRequest }}',
 '{{ SigningAlgorithm }}',
 '{{ TemplateArn }}',
 '{{ Validity }}',
 '{{ ValidityNotBefore }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: certificate
    props:
      - name: ApiPassthrough
        value:
          Extensions:
            CertificatePolicies:
              - CertPolicyId: '{{ CertPolicyId }}'
                PolicyQualifiers:
                  - PolicyQualifierId: '{{ PolicyQualifierId }}'
                    Qualifier:
                      CpsUri: '{{ CpsUri }}'
            ExtendedKeyUsage:
              - ExtendedKeyUsageType: '{{ ExtendedKeyUsageType }}'
                ExtendedKeyUsageObjectIdentifier: null
            KeyUsage:
              DigitalSignature: '{{ DigitalSignature }}'
              NonRepudiation: '{{ NonRepudiation }}'
              KeyEncipherment: '{{ KeyEncipherment }}'
              DataEncipherment: '{{ DataEncipherment }}'
              KeyAgreement: '{{ KeyAgreement }}'
              KeyCertSign: '{{ KeyCertSign }}'
              CRLSign: '{{ CRLSign }}'
              EncipherOnly: '{{ EncipherOnly }}'
              DecipherOnly: '{{ DecipherOnly }}'
            SubjectAlternativeNames:
              - OtherName:
                  TypeId: null
                  Value: '{{ Value }}'
                Rfc822Name: '{{ Rfc822Name }}'
                DnsName: '{{ DnsName }}'
                DirectoryName:
                  Country: '{{ Country }}'
                  Organization: '{{ Organization }}'
                  OrganizationalUnit: '{{ OrganizationalUnit }}'
                  DistinguishedNameQualifier: '{{ DistinguishedNameQualifier }}'
                  State: '{{ State }}'
                  CommonName: '{{ CommonName }}'
                  SerialNumber: '{{ SerialNumber }}'
                  Locality: '{{ Locality }}'
                  Title: '{{ Title }}'
                  Surname: '{{ Surname }}'
                  GivenName: '{{ GivenName }}'
                  Initials: '{{ Initials }}'
                  Pseudonym: '{{ Pseudonym }}'
                  GenerationQualifier: '{{ GenerationQualifier }}'
                  CustomAttributes:
                    - ObjectIdentifier: null
                      Value: '{{ Value }}'
                EdiPartyName:
                  PartyName: '{{ PartyName }}'
                  NameAssigner: '{{ NameAssigner }}'
                UniformResourceIdentifier: '{{ UniformResourceIdentifier }}'
                IpAddress: '{{ IpAddress }}'
                RegisteredId: null
            CustomExtensions:
              - Critical: '{{ Critical }}'
                ObjectIdentifier: null
                Value: '{{ Value }}'
          Subject: null
      - name: CertificateAuthorityArn
        value: '{{ CertificateAuthorityArn }}'
      - name: CertificateSigningRequest
        value: '{{ CertificateSigningRequest }}'
      - name: SigningAlgorithm
        value: '{{ SigningAlgorithm }}'
      - name: TemplateArn
        value: null
      - name: Validity
        value:
          Value: null
          Type: '{{ Type }}'
      - name: ValidityNotBefore
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.acmpca.certificates
WHERE data__Identifier = '<Arn|CertificateAuthorityArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificates</code> resource, the following permissions are required:

### Create
```json
acm-pca:IssueCertificate,
acm-pca:GetCertificate
```

### Read
```json
acm-pca:GetCertificate
```

### Delete
```json
acm-pca:GetCertificate
```

