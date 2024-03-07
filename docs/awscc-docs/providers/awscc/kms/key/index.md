---
title: key
hide_title: false
hide_table_of_contents: false
keywords:
  - key
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
Gets an individual <code>key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kms.key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the KMS key. Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations.&lt;br&#x2F;&gt; When ``Enabled`` is ``true``, the *key state* of the KMS key is ``Enabled``. When ``Enabled`` is ``false``, the key state of the KMS key is ``Disabled``. The default value is ``true``.&lt;br&#x2F;&gt; The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the &#91;EnableKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_EnableKey.html), &#91;DisableKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DisableKey.html), or &#91;ScheduleKeyDeletion&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_ScheduleKeyDeletion.html) operations.&lt;br&#x2F;&gt; For information about the key states of a KMS key, see &#91;Key state: Effect on your KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-state.html) in the *Developer Guide*.</td></tr>
<tr><td><code>enable_key_rotation</code></td><td><code>boolean</code></td><td>Enables automatic rotation of the key material for the specified KMS key. By default, automatic key rotation is not enabled.&lt;br&#x2F;&gt; KMS supports automatic rotation only for symmetric encryption KMS keys (``KeySpec`` = ``SYMMETRIC_DEFAULT``). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin ``EXTERNAL``, omit the ``EnableKeyRotation`` property or set it to ``false``.&lt;br&#x2F;&gt; To enable automatic key rotation of the key material for a multi-Region KMS key, set ``EnableKeyRotation`` to ``true`` on the primary key (created by using ``AWS::KMS::Key``). KMS copies the rotation status to all replica keys. For details, see &#91;Rotating multi-Region keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-manage.html#multi-region-rotate) in the *Developer Guide*.&lt;br&#x2F;&gt; When you enable automatic rotation, KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. KMS retains all key material until you delete the KMS key. Fo</td></tr>
<tr><td><code>key_policy</code></td><td><code>object</code></td><td>The key policy to attach to the KMS key.&lt;br&#x2F;&gt; If you provide a key policy, it must meet the following criteria:&lt;br&#x2F;&gt;  +  The key policy must allow the caller to make a subsequent &#91;PutKeyPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_PutKeyPolicy.html) request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see &#91;Default key policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-policies.html#key-policy-default-allow-root-enable-iam) in the *Developer Guide*. (To omit this condition, set ``BypassPolicyLockoutSafetyCheck`` to true.)&lt;br&#x2F;&gt;  +  Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see &#91;</td></tr>
<tr><td><code>key_usage</code></td><td><code>string</code></td><td>Determines the &#91;cryptographic operations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#cryptographic-operations) for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT``. This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created.&lt;br&#x2F;&gt;  If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.&lt;br&#x2F;&gt;  Select only one valid value.&lt;br&#x2F;&gt;  +  For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT``.&lt;br&#x2F;&gt;  +  For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY``.&lt;br&#x2F;&gt;  +  For asymmetric KMS keys with ECC key material, specify</td></tr>
<tr><td><code>origin</code></td><td><code>string</code></td><td>The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is ``AWS_KMS``, which means that KMS creates the key material.&lt;br&#x2F;&gt; To &#91;create a KMS key with no key material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys-create-cmk.html) (for imported key material), set this value to ``EXTERNAL``. For more information about importing key material into KMS, see &#91;Importing Key Material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can ignore ``ENABLED`` when Origin is ``EXTERNAL``. When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false``. After you import the key material, ``ENABLED`` updated to ``true``. The KMS key can then be used for Cryptographic Operations. &lt;br&#x2F;&gt;  CFN doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values.</td></tr>
<tr><td><code>key_spec</code></td><td><code>string</code></td><td>Specifies the type of KMS key to create. The default value, ``SYMMETRIC_DEFAULT``, creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see &#91;Choosing a KMS key type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;symm-asymm-choose.html) in the *Developer Guide*.&lt;br&#x2F;&gt; The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see &#91;condition keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;policy-conditions.html#conditions-kms) in the *Developer Guide*.&lt;br&#x2F;&gt;  If you change the value of the ``KeySpec`` property on an existing KMS key, the u</td></tr>
<tr><td><code>multi_region</code></td><td><code>boolean</code></td><td>Creates a multi-Region primary key that you can replicate in other AWS-Regions. You can't change the ``MultiRegion`` value after the KMS key is created.&lt;br&#x2F;&gt; For a list of AWS-Regions in which multi-Region keys are supported, see &#91;Multi-Region keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) in the **.&lt;br&#x2F;&gt;  If you change the value of the ``MultiRegion`` property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.&lt;br&#x2F;&gt;  For a multi-Region key, set to this property to ``true``. For a single-Region key, omit this property or set it to ``false``. The default value is ``false``.&lt;br&#x2F;&gt; *Multi-Region keys* are an KMS feature that lets you create multiple interoperable KMS keys in different AWS-Regions. Bec</td></tr>
<tr><td><code>pending_window_in_days</code></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before KMS deletes a KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.&lt;br&#x2F;&gt; When you remove a KMS key from a CloudFormation stack, KMS schedules the KMS key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of KMS key is ``Pending Deletion`` or ``Pending Replica Deletion``, which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, KMS permanently deletes the KMS key.&lt;br&#x2F;&gt; KMS will not delete a &#91;multi-Region primary key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to ``PendingReplicaDeletion`` so it cannot be replicated or used in cryptographic ope</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Assigns one or more tags to the replica key.&lt;br&#x2F;&gt;  Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;abac.html) in the *Developer Guide*.&lt;br&#x2F;&gt;  For information about tags in KMS, see &#91;Tagging keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;tagging-keys.html) in the *Developer Guide*. For information about tags in CloudFormation, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bypass_policy_lockout_safety_check</code></td><td><code>boolean</code></td><td>Skips ("bypasses") the key policy lockout safety check. The default value is false.&lt;br&#x2F;&gt;  Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.&lt;br&#x2F;&gt; For more information, see &#91;Default key policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-policy-default.html#prevent-unmanageable-key) in the *Developer Guide*.&lt;br&#x2F;&gt;  Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent &#91;PutKeyPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_PutKeyPolicy.html) request on the KMS key.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>key</code> resource, the following permissions are required:

### Read
```json
kms:DescribeKey,
kms:GetKeyPolicy,
kms:GetKeyRotationStatus,
kms:ListResourceTags
```

### Update
```json
kms:DescribeKey,
kms:DisableKey,
kms:DisableKeyRotation,
kms:EnableKey,
kms:EnableKeyRotation,
kms:PutKeyPolicy,
kms:TagResource,
kms:UntagResource,
kms:UpdateKeyDescription,
kms:ListResourceTags
```

### Delete
```json
kms:DescribeKey,
kms:ScheduleKeyDeletion
```


## Example
```sql
SELECT
region,
description,
enabled,
enable_key_rotation,
key_policy,
key_usage,
origin,
key_spec,
multi_region,
pending_window_in_days,
tags,
arn,
key_id,
bypass_policy_lockout_safety_check
FROM awscc.kms.key
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;KeyId&gt;'
```
