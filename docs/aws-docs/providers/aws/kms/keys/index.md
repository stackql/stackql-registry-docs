---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - kms
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


Used to retrieve a list of <code>keys</code> in a region or to create or delete a <code>keys</code> resource, use <code>key</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::KMS::Key`` resource specifies an &#91;KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#kms_keys) in KMSlong. You can use this resource to create symmetric encryption KMS keys, asymmetric KMS keys for encryption or signing, and symmetric HMAC KMS keys. You can use ``AWS::KMS::Key`` to create &#91;multi-Region primary keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html#mrk-primary-key) of all supported types. To replicate a multi-Region key, use the ``AWS::KMS::ReplicaKey`` resource.&lt;br&#x2F;&gt;  If you change the value of the ``KeySpec``, ``KeyUsage``, ``Origin``, or ``MultiRegion`` properties of an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing any of its immutable property values.&lt;br&#x2F;&gt;   KMS replaced the term *customer master key (CMK)* with ** and *KMS key*. The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.&lt;br&#x2F;&gt;  You can use symmetric encryption KMS keys to encrypt and decrypt small amounts of data, but they are more commonly used to generate data keys and data key pairs. You can also use a symmetric encryption KMS key to encrypt data stored in AWS services that are &#91;integrated with&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;kms&#x2F;features&#x2F;#AWS_Service_Integration). For more information, see &#91;Symmetric encryption KMS keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#symmetric-cmks) in the *Developer Guide*.&lt;br&#x2F;&gt; You can use asymmetric KMS keys to encrypt and decrypt data or sign messages and verify signatures. To create an asymmetric key, you must specify an asymmetric ``KeySpec`` value and a ``KeyUsage`` value. For details, see &#91;Asymmetric keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;symmetric-asymmetric.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can use HMAC KMS keys (which are also symmetric keys) to generate and verify hash-based message authentication codes. To create an HMAC key, you must specify an HMAC ``KeySpec`` value and a ``KeyUsage`` value of ``GENERATE_VERIFY_MAC``. For details, see &#91;HMAC keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;hmac.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can also create symmetric encryption, asymmetric, and HMAC multi-Region primary keys. To create a multi-Region primary key, set the ``MultiRegion`` property to ``true``. For information about multi-Region keys, see &#91;Multi-Region keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You cannot use the ``AWS::KMS::Key`` resource to specify a KMS key with &#91;imported key material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys.html) or a KMS key in a &#91;custom key store&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;custom-key-store-overview.html).&lt;br&#x2F;&gt; *Regions*&lt;br&#x2F;&gt; KMS CloudFormation resources are available in all Regions in which KMS and CFN are supported. You can use the ``AWS::KMS::Key`` resource to create and manage all KMS key types that are supported in a Region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
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
key_id
FROM aws.kms.keys
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- key.iql (required properties only)
INSERT INTO aws.kms.keys (
 Description,
 Enabled,
 EnableKeyRotation,
 KeyPolicy,
 KeyUsage,
 Origin,
 KeySpec,
 MultiRegion,
 PendingWindowInDays,
 Tags,
 BypassPolicyLockoutSafetyCheck,
 RotationPeriodInDays,
 region
)
SELECT 
'{{ Description }}',
 '{{ Enabled }}',
 '{{ EnableKeyRotation }}',
 '{{ KeyPolicy }}',
 '{{ KeyUsage }}',
 '{{ Origin }}',
 '{{ KeySpec }}',
 '{{ MultiRegion }}',
 '{{ PendingWindowInDays }}',
 '{{ Tags }}',
 '{{ BypassPolicyLockoutSafetyCheck }}',
 '{{ RotationPeriodInDays }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- key.iql (all properties)
INSERT INTO aws.kms.keys (
 Description,
 Enabled,
 EnableKeyRotation,
 KeyPolicy,
 KeyUsage,
 Origin,
 KeySpec,
 MultiRegion,
 PendingWindowInDays,
 Tags,
 BypassPolicyLockoutSafetyCheck,
 RotationPeriodInDays,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Enabled }}',
 '{{ EnableKeyRotation }}',
 '{{ KeyPolicy }}',
 '{{ KeyUsage }}',
 '{{ Origin }}',
 '{{ KeySpec }}',
 '{{ MultiRegion }}',
 '{{ PendingWindowInDays }}',
 '{{ Tags }}',
 '{{ BypassPolicyLockoutSafetyCheck }}',
 '{{ RotationPeriodInDays }}',
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
  - name: key
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: EnableKeyRotation
        value: '{{ EnableKeyRotation }}'
      - name: KeyPolicy
        value: {}
      - name: KeyUsage
        value: '{{ KeyUsage }}'
      - name: Origin
        value: '{{ Origin }}'
      - name: KeySpec
        value: '{{ KeySpec }}'
      - name: MultiRegion
        value: '{{ MultiRegion }}'
      - name: PendingWindowInDays
        value: '{{ PendingWindowInDays }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: BypassPolicyLockoutSafetyCheck
        value: '{{ BypassPolicyLockoutSafetyCheck }}'
      - name: RotationPeriodInDays
        value: '{{ RotationPeriodInDays }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kms.keys
WHERE data__Identifier = '<KeyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>keys</code> resource, the following permissions are required:

### Create
```json
kms:CreateKey,
kms:EnableKeyRotation,
kms:DisableKey,
kms:TagResource,
kms:PutKeyPolicy
```

### Delete
```json
kms:DescribeKey,
kms:ScheduleKeyDeletion
```

### List
```json
kms:ListKeys,
kms:DescribeKey
```

