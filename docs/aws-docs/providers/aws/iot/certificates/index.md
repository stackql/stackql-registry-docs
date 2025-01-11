---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - iot
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
<tr><td><b>Description</b></td><td>Use the AWS::IoT::Certificate resource to declare an AWS IoT X.509 certificate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ca_certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_signing_request" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html"><code>AWS::IoT::Certificate</code></a>.

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
    <td><CopyableCode code="Status, region" /></td>
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
Gets all <code>certificates</code> in a region.
```sql
SELECT
region,
ca_certificate_pem,
certificate_pem,
certificate_signing_request,
certificate_mode,
status,
id,
arn
FROM aws.iot.certificates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>certificate</code>.
```sql
SELECT
region,
ca_certificate_pem,
certificate_pem,
certificate_signing_request,
certificate_mode,
status,
id,
arn
FROM aws.iot.certificates
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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
INSERT INTO aws.iot.certificates (
 Status,
 region
)
SELECT 
'{{ Status }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.certificates (
 CACertificatePem,
 CertificatePem,
 CertificateSigningRequest,
 CertificateMode,
 Status,
 region
)
SELECT 
 '{{ CACertificatePem }}',
 '{{ CertificatePem }}',
 '{{ CertificateSigningRequest }}',
 '{{ CertificateMode }}',
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
  - name: certificate
    props:
      - name: CACertificatePem
        value: '{{ CACertificatePem }}'
      - name: CertificatePem
        value: '{{ CertificatePem }}'
      - name: CertificateSigningRequest
        value: '{{ CertificateSigningRequest }}'
      - name: CertificateMode
        value: '{{ CertificateMode }}'
      - name: Status
        value: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.certificates
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificates</code> resource, the following permissions are required:

### Create
```json
iot:CreateCertificateFromCsr,
iot:RegisterCertificate,
iot:RegisterCertificateWithoutCA,
iot:DescribeCertificate
```

### Read
```json
iot:DescribeCertificate
```

### Update
```json
iot:UpdateCertificate,
iot:DescribeCertificate
```

### Delete
```json
iot:DeleteCertificate,
iot:UpdateCertificate,
iot:DescribeCertificate
```

### List
```json
iot:ListCertificates
```
