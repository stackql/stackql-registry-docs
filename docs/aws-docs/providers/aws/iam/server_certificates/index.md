---
title: server_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - server_certificates
  - iam
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

Creates, updates, deletes or gets a <code>server_certificate</code> resource or lists <code>server_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::ServerCertificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.server_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_body" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_chain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_certificate_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="private_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the server certificate</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servercertificate.html"><code>AWS::IAM::ServerCertificate</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>server_certificates</code> in a region.
```sql
SELECT
region,
certificate_body,
certificate_chain,
server_certificate_name,
path,
private_key,
arn,
tags
FROM aws.iam.server_certificates
;
```
Gets all properties from an individual <code>server_certificate</code>.
```sql
SELECT
region,
certificate_body,
certificate_chain,
server_certificate_name,
path,
private_key,
arn,
tags
FROM aws.iam.server_certificates
WHERE data__Identifier = '<ServerCertificateName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_certificate</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.server_certificates (
 CertificateBody,
 CertificateChain,
 ServerCertificateName,
 Path,
 PrivateKey,
 Tags,
 region
)
SELECT 
'{{ CertificateBody }}',
 '{{ CertificateChain }}',
 '{{ ServerCertificateName }}',
 '{{ Path }}',
 '{{ PrivateKey }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.server_certificates (
 CertificateBody,
 CertificateChain,
 ServerCertificateName,
 Path,
 PrivateKey,
 Tags,
 region
)
SELECT 
 '{{ CertificateBody }}',
 '{{ CertificateChain }}',
 '{{ ServerCertificateName }}',
 '{{ Path }}',
 '{{ PrivateKey }}',
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
  - name: server_certificate
    props:
      - name: CertificateBody
        value: '{{ CertificateBody }}'
      - name: CertificateChain
        value: '{{ CertificateChain }}'
      - name: ServerCertificateName
        value: '{{ ServerCertificateName }}'
      - name: Path
        value: '{{ Path }}'
      - name: PrivateKey
        value: '{{ PrivateKey }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.server_certificates
WHERE data__Identifier = '<ServerCertificateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>server_certificates</code> resource, the following permissions are required:

### Create
```json
iam:UploadServerCertificate,
iam:TagServerCertificate,
iam:GetServerCertificate
```

### Read
```json
iam:GetServerCertificate
```

### Update
```json
iam:TagServerCertificate,
iam:UntagServerCertificate,
iam:ListServerCertificateTags,
iam:GetServerCertificate
```

### Delete
```json
iam:DeleteServerCertificate
```

### List
```json
iam:ListServerCertificates,
iam:GetServerCertificate
```
