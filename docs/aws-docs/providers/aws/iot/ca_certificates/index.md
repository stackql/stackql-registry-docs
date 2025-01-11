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

Creates, updates, deletes or gets a <code>ca_certificate</code> resource or lists <code>ca_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a CA Certificate in IoT.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.ca_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ca_certificate_pem" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="verification_certificate_pem" /></td><td><code>string</code></td><td>The private key verification certificate.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_registration_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_auto_registration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="registration_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html"><code>AWS::IoT::CACertificate</code></a>.

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
    <td><CopyableCode code="CACertificatePem, Status, region" /></td>
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
Gets all <code>ca_certificates</code> in a region.
```sql
SELECT
region,
ca_certificate_pem,
verification_certificate_pem,
status,
certificate_mode,
auto_registration_status,
remove_auto_registration,
registration_config,
id,
arn,
tags
FROM aws.iot.ca_certificates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ca_certificate</code>.
```sql
SELECT
region,
ca_certificate_pem,
verification_certificate_pem,
status,
certificate_mode,
auto_registration_status,
remove_auto_registration,
registration_config,
id,
arn,
tags
FROM aws.iot.ca_certificates
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ca_certificate</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iot:DescribeCACertificate,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateCACertificate,
iot:DescribeCACertificate,
iot:TagResource,
iot:UntagResource,
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
