---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - lightsail
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
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The name for the certificate.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for the certificate.</td></tr>
<tr><td><CopyableCode code="subject_alternative_names" /></td><td><code>array</code></td><td>An array of strings that specify the alternate domains (e.g., example2.com) and subdomains (e.g., blog.example.com) for the certificate.</td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The validation status of the certificate.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="CertificateName, DomainName, region" /></td>
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
certificate_name,
domain_name,
subject_alternative_names,
certificate_arn,
status,
tags
FROM aws.lightsail.certificates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>certificate</code>.
```sql
SELECT
region,
certificate_name,
domain_name,
subject_alternative_names,
certificate_arn,
status,
tags
FROM aws.lightsail.certificates
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateName>';
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
INSERT INTO aws.lightsail.certificates (
 CertificateName,
 DomainName,
 region
)
SELECT 
'{{ CertificateName }}',
 '{{ DomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.certificates (
 CertificateName,
 DomainName,
 SubjectAlternativeNames,
 Tags,
 region
)
SELECT 
 '{{ CertificateName }}',
 '{{ DomainName }}',
 '{{ SubjectAlternativeNames }}',
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
      - name: CertificateName
        value: '{{ CertificateName }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: SubjectAlternativeNames
        value:
          - '{{ SubjectAlternativeNames[0] }}'
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
DELETE FROM aws.lightsail.certificates
WHERE data__Identifier = '<CertificateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>certificates</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateCertificate,
lightsail:GetCertificates,
lightsail:TagResource,
lightsail:UntagResource
```

### Read
```json
lightsail:GetCertificates
```

### Update
```json
lightsail:GetCertificates,
lightsail:TagResource,
lightsail:UntagResource
```

### Delete
```json
lightsail:DeleteCertificate,
lightsail:GetCertificates
```

### List
```json
lightsail:GetCertificates
```

