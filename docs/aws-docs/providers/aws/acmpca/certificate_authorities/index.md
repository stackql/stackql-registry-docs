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


Used to retrieve a list of <code>certificate_authorities</code> in a region or to create or delete a <code>certificate_authorities</code> resource, use <code>certificate_authority</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Private certificate authority.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate_authorities" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the certificate authority.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.acmpca.certificate_authorities
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Type": "{{ Type }}",
 "KeyAlgorithm": "{{ KeyAlgorithm }}",
 "SigningAlgorithm": "{{ SigningAlgorithm }}",
 "Subject": {
  "Country": "{{ Country }}",
  "Organization": "{{ Organization }}",
  "OrganizationalUnit": "{{ OrganizationalUnit }}",
  "DistinguishedNameQualifier": "{{ DistinguishedNameQualifier }}",
  "State": "{{ State }}",
  "CommonName": "{{ CommonName }}",
  "SerialNumber": "{{ SerialNumber }}",
  "Locality": "{{ Locality }}",
  "Title": "{{ Title }}",
  "Surname": "{{ Surname }}",
  "GivenName": "{{ GivenName }}",
  "Initials": "{{ Initials }}",
  "Pseudonym": "{{ Pseudonym }}",
  "GenerationQualifier": "{{ GenerationQualifier }}",
  "CustomAttributes": [
   {
    "ObjectIdentifier": "{{ ObjectIdentifier }}",
    "Value": "{{ Value }}"
   }
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.acmpca.certificate_authorities (
 Type,
 KeyAlgorithm,
 SigningAlgorithm,
 Subject,
 region
)
SELECT 
{{ .Type }},
 {{ .KeyAlgorithm }},
 {{ .SigningAlgorithm }},
 {{ .Subject }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Type": "{{ Type }}",
 "KeyAlgorithm": "{{ KeyAlgorithm }}",
 "SigningAlgorithm": "{{ SigningAlgorithm }}",
 "Subject": {
  "Country": "{{ Country }}",
  "Organization": "{{ Organization }}",
  "OrganizationalUnit": "{{ OrganizationalUnit }}",
  "DistinguishedNameQualifier": "{{ DistinguishedNameQualifier }}",
  "State": "{{ State }}",
  "CommonName": "{{ CommonName }}",
  "SerialNumber": "{{ SerialNumber }}",
  "Locality": "{{ Locality }}",
  "Title": "{{ Title }}",
  "Surname": "{{ Surname }}",
  "GivenName": "{{ GivenName }}",
  "Initials": "{{ Initials }}",
  "Pseudonym": "{{ Pseudonym }}",
  "GenerationQualifier": "{{ GenerationQualifier }}",
  "CustomAttributes": [
   {
    "ObjectIdentifier": "{{ ObjectIdentifier }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "RevocationConfiguration": {
  "CrlConfiguration": {
   "Enabled": "{{ Enabled }}",
   "ExpirationInDays": "{{ ExpirationInDays }}",
   "CustomCname": "{{ CustomCname }}",
   "S3BucketName": "{{ S3BucketName }}",
   "S3ObjectAcl": "{{ S3ObjectAcl }}",
   "CrlDistributionPointExtensionConfiguration": {
    "OmitExtension": "{{ OmitExtension }}"
   }
  },
  "OcspConfiguration": {
   "Enabled": "{{ Enabled }}",
   "OcspCustomCname": "{{ OcspCustomCname }}"
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CsrExtensions": {
  "KeyUsage": {
   "DigitalSignature": "{{ DigitalSignature }}",
   "NonRepudiation": "{{ NonRepudiation }}",
   "KeyEncipherment": "{{ KeyEncipherment }}",
   "DataEncipherment": "{{ DataEncipherment }}",
   "KeyAgreement": "{{ KeyAgreement }}",
   "KeyCertSign": "{{ KeyCertSign }}",
   "CRLSign": "{{ CRLSign }}",
   "EncipherOnly": "{{ EncipherOnly }}",
   "DecipherOnly": "{{ DecipherOnly }}"
  },
  "SubjectInformationAccess": [
   {
    "AccessMethod": {
     "CustomObjectIdentifier": null,
     "AccessMethodType": "{{ AccessMethodType }}"
    },
    "AccessLocation": {
     "OtherName": {
      "TypeId": null,
      "Value": "{{ Value }}"
     },
     "Rfc822Name": "{{ Rfc822Name }}",
     "DnsName": "{{ DnsName }}",
     "DirectoryName": null,
     "EdiPartyName": {
      "PartyName": "{{ PartyName }}",
      "NameAssigner": "{{ NameAssigner }}"
     },
     "UniformResourceIdentifier": "{{ UniformResourceIdentifier }}",
     "IpAddress": "{{ IpAddress }}",
     "RegisteredId": null
    }
   }
  ]
 },
 "KeyStorageSecurityStandard": "{{ KeyStorageSecurityStandard }}",
 "UsageMode": "{{ UsageMode }}"
}
>>>
--all properties
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
 {{ .Type }},
 {{ .KeyAlgorithm }},
 {{ .SigningAlgorithm }},
 {{ .Subject }},
 {{ .RevocationConfiguration }},
 {{ .Tags }},
 {{ .CsrExtensions }},
 {{ .KeyStorageSecurityStandard }},
 {{ .UsageMode }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

