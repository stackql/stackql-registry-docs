---
title: ca_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_certificates
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


Used to retrieve a list of <code>ca_certificates</code> in a region or to create or delete a <code>ca_certificates</code> resource, use <code>ca_certificate</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a CA Certificate in IoT.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.ca_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
id
FROM aws.iot.ca_certificates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>ca_certificate</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- ca_certificate.iql (required properties only)
INSERT INTO aws.iot.ca_certificates (
 CACertificatePem,
 Status,
 region
)
SELECT 
'{{ CACertificatePem }}',
 '{{ Status }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- ca_certificate.iql (all properties)
INSERT INTO aws.iot.ca_certificates (
 CACertificatePem,
 VerificationCertificatePem,
 Status,
 CertificateMode,
 AutoRegistrationStatus,
 RemoveAutoRegistration,
 RegistrationConfig,
 Tags,
 region
)
SELECT 
 '{{ CACertificatePem }}',
 '{{ VerificationCertificatePem }}',
 '{{ Status }}',
 '{{ CertificateMode }}',
 '{{ AutoRegistrationStatus }}',
 '{{ RemoveAutoRegistration }}',
 '{{ RegistrationConfig }}',
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
  - name: ca_certificate
    props:
      - name: CACertificatePem
        value: '{{ CACertificatePem }}'
      - name: VerificationCertificatePem
        value: '{{ VerificationCertificatePem }}'
      - name: Status
        value: '{{ Status }}'
      - name: CertificateMode
        value: '{{ CertificateMode }}'
      - name: AutoRegistrationStatus
        value: '{{ AutoRegistrationStatus }}'
      - name: RemoveAutoRegistration
        value: '{{ RemoveAutoRegistration }}'
      - name: RegistrationConfig
        value:
          TemplateBody: '{{ TemplateBody }}'
          RoleArn: '{{ RoleArn }}'
          TemplateName: '{{ TemplateName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.ca_certificates
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ca_certificates</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
iot:RegisterCACertificate,
iot:DescribeCACertificate,
iot:TagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:UpdateCACertificate,
iot:DeleteCACertificate,
iot:DescribeCACertificate
```

### List
```json
iot:ListCACertificates
```

