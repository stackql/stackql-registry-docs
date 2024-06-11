---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - transfer
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Certificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="usage" /></td><td><code>string</code></td><td>Specifies the usage type for the certificate.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td>Specifies the certificate body to be imported.</td></tr>
<tr><td><CopyableCode code="certificate_chain" /></td><td><code>string</code></td><td>Specifies the certificate chain to be imported.</td></tr>
<tr><td><CopyableCode code="private_key" /></td><td><code>string</code></td><td>Specifies the private key for the certificate.</td></tr>
<tr><td><CopyableCode code="active_date" /></td><td><code>string</code></td><td>Specifies the active date for the certificate.</td></tr>
<tr><td><CopyableCode code="inactive_date" /></td><td><code>string</code></td><td>Specifies the inactive date for the certificate.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the certificate.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
<tr><td><CopyableCode code="certificate_id" /></td><td><code>string</code></td><td>A unique identifier for the certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A status description for the certificate.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Describing the type of certificate. With or without a private key.</td></tr>
<tr><td><CopyableCode code="serial" /></td><td><code>string</code></td><td>Specifies Certificate's serial.</td></tr>
<tr><td><CopyableCode code="not_before_date" /></td><td><code>string</code></td><td>Specifies the not before date for the certificate.</td></tr>
<tr><td><CopyableCode code="not_after_date" /></td><td><code>string</code></td><td>Specifies the not after date for the certificate.</td></tr>
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
    <td><CopyableCode code="Certificate, Usage, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>certificates</code> in a region.
```sql
SELECT
region,
certificate_id
FROM aws.transfer.certificates
WHERE region = 'us-east-1';
```
Gets all properties from a <code>certificate</code>.
```sql
SELECT
region,
usage,
certificate,
certificate_chain,
private_key,
active_date,
inactive_date,
description,
tags,
arn,
certificate_id,
status,
type,
serial,
not_before_date,
not_after_date
FROM aws.transfer.certificates
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateId>';
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
INSERT INTO aws.transfer.certificates (
 Usage,
 Certificate,
 region
)
SELECT 
'{{ Usage }}',
 '{{ Certificate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.transfer.certificates (
 Usage,
 Certificate,
 CertificateChain,
 PrivateKey,
 ActiveDate,
 InactiveDate,
 Description,
 Tags,
 region
)
SELECT 
 '{{ Usage }}',
 '{{ Certificate }}',
 '{{ CertificateChain }}',
 '{{ PrivateKey }}',
 '{{ ActiveDate }}',
 '{{ InactiveDate }}',
 '{{ Description }}',
 '{{ Tags }}',
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
      - name: Usage
        value: '{{ Usage }}'
      - name: Certificate
        value: '{{ Certificate }}'
      - name: CertificateChain
        value: '{{ CertificateChain }}'
      - name: PrivateKey
        value: '{{ PrivateKey }}'
      - name: ActiveDate
        value: '{{ ActiveDate }}'
      - name: InactiveDate
        value: '{{ InactiveDate }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.transfer.certificates
WHERE data__Identifier = '<CertificateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificates</code> resource, the following permissions are required:

### Create
```json
transfer:ImportCertificate,
transfer:TagResource
```

### Read
```json
transfer:DescribeCertificate
```

### Update
```json
transfer:UpdateCertificate,
transfer:UnTagResource,
transfer:TagResource
```

### Delete
```json
transfer:DeleteCertificate
```

### List
```json
transfer:ListCertificates
```

