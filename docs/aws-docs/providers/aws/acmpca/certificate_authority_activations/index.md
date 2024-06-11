---
title: certificate_authority_activations
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authority_activations
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

Creates, updates, deletes or gets a <code>certificate_authority_activation</code> resource or lists <code>certificate_authority_activations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authority_activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Used to install the certificate authority certificate and update the certificate authority status.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.acmpca.certificate_authority_activations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_authority_arn" /></td><td><code>string</code></td><td>Arn of the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td>Certificate Authority certificate that will be installed in the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="certificate_chain" /></td><td><code>string</code></td><td>Certificate chain for the Certificate Authority certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Certificate Authority.</td></tr>
<tr><td><CopyableCode code="complete_certificate_chain" /></td><td><code>string</code></td><td>The complete certificate chain, including the Certificate Authority certificate.</td></tr>
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
    <td><CopyableCode code="CertificateAuthorityArn, Certificate, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>certificate_authority_activation</code>.
```sql
SELECT
region,
certificate_authority_arn,
certificate,
certificate_chain,
status,
complete_certificate_chain
FROM aws.acmpca.certificate_authority_activations
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateAuthorityArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_authority_activation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.acmpca.certificate_authority_activations (
 CertificateAuthorityArn,
 Certificate,
 region
)
SELECT 
'{{ CertificateAuthorityArn }}',
 '{{ Certificate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.acmpca.certificate_authority_activations (
 CertificateAuthorityArn,
 Certificate,
 CertificateChain,
 Status,
 region
)
SELECT 
 '{{ CertificateAuthorityArn }}',
 '{{ Certificate }}',
 '{{ CertificateChain }}',
 '{{ Status }}',
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
  - name: certificate_authority_activation
    props:
      - name: CertificateAuthorityArn
        value: '{{ CertificateAuthorityArn }}'
      - name: Certificate
        value: '{{ Certificate }}'
      - name: CertificateChain
        value: '{{ CertificateChain }}'
      - name: Status
        value: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.acmpca.certificate_authority_activations
WHERE data__Identifier = '<CertificateAuthorityArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificate_authority_activations</code> resource, the following permissions are required:

### Create
```json
acm-pca:ImportCertificateAuthorityCertificate,
acm-pca:UpdateCertificateAuthority
```

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

