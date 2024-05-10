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


Used to retrieve a list of <code>certificates</code> in a region or to create or delete a <code>certificates</code> resource, use <code>certificate</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The name for the certificate.</td></tr>
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
certificate_name
FROM aws.lightsail.certificates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>certificate</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- certificate.iql (required properties only)
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
-- certificate.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
lightsail:DeleteCertificate,
lightsail:GetCertificates
```

### List
```json
lightsail:GetCertificates
```

