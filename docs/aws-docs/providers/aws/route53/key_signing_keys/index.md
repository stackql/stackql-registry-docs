---
title: key_signing_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - key_signing_keys
  - route53
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

Creates, updates, deletes or gets a <code>key_signing_key</code> resource or lists <code>key_signing_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_signing_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a key signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.key_signing_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="hosted_zone_id" /></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.</td></tr>
<tr><td><CopyableCode code="key_management_service_arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html"><code>AWS::Route53::KeySigningKey</code></a>.

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
    <td><CopyableCode code="Status, HostedZoneId, Name, KeyManagementServiceArn, region" /></td>
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
Gets all <code>key_signing_keys</code> in a region.
```sql
SELECT
region,
hosted_zone_id,
status,
name,
key_management_service_arn
FROM aws.route53.key_signing_keys
;
```
Gets all properties from an individual <code>key_signing_key</code>.
```sql
SELECT
region,
hosted_zone_id,
status,
name,
key_management_service_arn
FROM aws.route53.key_signing_keys
WHERE data__Identifier = '<HostedZoneId>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_signing_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53.key_signing_keys (
 HostedZoneId,
 Status,
 Name,
 KeyManagementServiceArn,
 region
)
SELECT 
'{{ HostedZoneId }}',
 '{{ Status }}',
 '{{ Name }}',
 '{{ KeyManagementServiceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53.key_signing_keys (
 HostedZoneId,
 Status,
 Name,
 KeyManagementServiceArn,
 region
)
SELECT 
 '{{ HostedZoneId }}',
 '{{ Status }}',
 '{{ Name }}',
 '{{ KeyManagementServiceArn }}',
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
  - name: key_signing_key
    props:
      - name: HostedZoneId
        value: '{{ HostedZoneId }}'
      - name: Status
        value: '{{ Status }}'
      - name: Name
        value: '{{ Name }}'
      - name: KeyManagementServiceArn
        value: '{{ KeyManagementServiceArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53.key_signing_keys
WHERE data__Identifier = '<HostedZoneId|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>key_signing_keys</code> resource, the following permissions are required:

### Create
```json
route53:CreateKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### Read
```json
route53:GetDNSSEC
```

### Update
```json
route53:GetDNSSEC,
route53:ActivateKeySigningKey,
route53:DeactivateKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### Delete
```json
route53:DeactivateKeySigningKey,
route53:DeleteKeySigningKey,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```

### List
```json
route53:GetDNSSEC,
route53:ListHostedZones
```
