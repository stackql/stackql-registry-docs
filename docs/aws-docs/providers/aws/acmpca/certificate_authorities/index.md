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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>certificate_authority</code> resource or lists <code>certificate_authorities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Private certificate authority.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate_authorities" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the certificate authority.</td></tr>
<tr><td><CopyableCode code="key_algorithm" /></td><td><code>string</code></td><td>Public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.</td></tr>
<tr><td><CopyableCode code="signing_algorithm" /></td><td><code>string</code></td><td>Algorithm your CA uses to sign certificate requests.</td></tr>
<tr><td><CopyableCode code="subject" /></td><td><code>object</code></td><td>Structure that contains X.500 distinguished name information for your CA.</td></tr>
<tr><td><CopyableCode code="revocation_configuration" /></td><td><code>object</code></td><td>Certificate revocation information used by the CreateCertificateAuthority and UpdateCertificateAuthority actions.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td>The base64 PEM-encoded certificate signing request (CSR) for your certificate authority certificate.</td></tr>
<tr><td><CopyableCode code="csr_extensions" /></td><td><code>object</code></td><td>Structure that contains CSR pass through extension information used by the CreateCertificateAuthority action.</td></tr>
<tr><td><CopyableCode code="key_storage_security_standard" /></td><td><code>string</code></td><td>KeyStorageSecurityStadard defines a cryptographic key management compliance standard used for handling CA keys.</td></tr>
<tr><td><CopyableCode code="usage_mode" /></td><td><code>string</code></td><td>Usage mode of the ceritificate authority.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html"><code>AWS::ACMPCA::CertificateAuthority</code></a>.

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
    <td><CopyableCode code="Type, KeyAlgorithm, SigningAlgorithm, Subject, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>certificate_authorities</code> in a region.
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
FROM aws.acmpca.certificate_authorities
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>certificate_authority</code>.
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
FROM aws.acmpca.certificate_authorities
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_authority</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.acmpca.certificate_authorities (
 Type,
 KeyAlgorithm,
 SigningAlgorithm,
 Subject,
 region
)
SELECT 
'{{ Type }}',
 '{{ KeyAlgorithm }}',
 '{{ SigningAlgorithm }}',
 '{{ Subject }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.acmpca.certificate_authorities (
 Type,
 KeyAlgorithm,
 SigningAlgorithm,
 Subject,
 RevocationConfiguration,
 Tags,
 CsrExtensions,
 KeyStorageSecurityStandard,
 UsageMode,
 region
)
SELECT 
 '{{ Type }}',
 '{{ KeyAlgorithm }}',
 '{{ SigningAlgorithm }}',
 '{{ Subject }}',
 '{{ RevocationConfiguration }}',
 '{{ Tags }}',
 '{{ CsrExtensions }}',
 '{{ KeyStorageSecurityStandard }}',
 '{{ UsageMode }}',
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
  - name: certificate_authority
    props:
      - name: Type
        value: '{{ Type }}'
      - name: KeyAlgorithm
        value: '{{ KeyAlgorithm }}'
      - name: SigningAlgorithm
        value: '{{ SigningAlgorithm }}'
      - name: Subject
        value:
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
            - ObjectIdentifier: '{{ ObjectIdentifier }}'
              Value: '{{ Value }}'
      - name: RevocationConfiguration
        value:
          CrlConfiguration:
            Enabled: '{{ Enabled }}'
            ExpirationInDays: '{{ ExpirationInDays }}'
            CustomCname: '{{ CustomCname }}'
            S3BucketName: '{{ S3BucketName }}'
            S3ObjectAcl: '{{ S3ObjectAcl }}'
            CrlDistributionPointExtensionConfiguration:
              OmitExtension: '{{ OmitExtension }}'
          OcspConfiguration:
            Enabled: '{{ Enabled }}'
            OcspCustomCname: '{{ OcspCustomCname }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CsrExtensions
        value:
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
          SubjectInformationAccess:
            - AccessMethod:
                CustomObjectIdentifier: null
                AccessMethodType: '{{ AccessMethodType }}'
              AccessLocation:
                OtherName:
                  TypeId: null
                  Value: '{{ Value }}'
                Rfc822Name: '{{ Rfc822Name }}'
                DnsName: '{{ DnsName }}'
                DirectoryName: null
                EdiPartyName:
                  PartyName: '{{ PartyName }}'
                  NameAssigner: '{{ NameAssigner }}'
                UniformResourceIdentifier: '{{ UniformResourceIdentifier }}'
                IpAddress: '{{ IpAddress }}'
                RegisteredId: null
      - name: KeyStorageSecurityStandard
        value: '{{ KeyStorageSecurityStandard }}'
      - name: UsageMode
        value: '{{ UsageMode }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.acmpca.certificate_authorities
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificate_authorities</code> resource, the following permissions are required:

### Create
```json
acm-pca:CreateCertificateAuthority,
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr
```

### Read
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr,
acm-pca:ListTags
```

### Update
```json
acm-pca:ListTags,
acm-pca:TagCertificateAuthority,
acm-pca:UntagCertificateAuthority,
acm-pca:UpdateCertificateAuthority
```

### Delete
```json
acm-pca:DeleteCertificateAuthority,
acm-pca:DescribeCertificateAuthority
```

### List
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCsr,
acm-pca:ListCertificateAuthorities,
acm-pca:ListTags
```
