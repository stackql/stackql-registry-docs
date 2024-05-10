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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>key</code> resource, use <code>keys</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::KMS::Key`` resource specifies an &#91;KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#kms_keys) in KMSlong. You can use this resource to create symmetric encryption KMS keys, asymmetric KMS keys for encryption or signing, and symmetric HMAC KMS keys. You can use ``AWS::KMS::Key`` to create &#91;multi-Region primary keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html#mrk-primary-key) of all supported types. To replicate a multi-Region key, use the ``AWS::KMS::ReplicaKey`` resource.&lt;br&#x2F;&gt;  If you change the value of the ``KeySpec``, ``KeyUsage``, ``Origin``, or ``MultiRegion`` properties of an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing any of its immutable property values.&lt;br&#x2F;&gt;   KMS replaced the term *customer master key (CMK)* with ** and *KMS key*. The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.&lt;br&#x2F;&gt;  You can use symmetric encryption KMS keys to encrypt and decrypt small amounts of data, but they are more commonly used to generate data keys and data key pairs. You can also use a symmetric encryption KMS key to encrypt data stored in AWS services that are &#91;integrated with&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;kms&#x2F;features&#x2F;#AWS_Service_Integration). For more information, see &#91;Symmetric encryption KMS keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#symmetric-cmks) in the *Developer Guide*.&lt;br&#x2F;&gt; You can use asymmetric KMS keys to encrypt and decrypt data or sign messages and verify signatures. To create an asymmetric key, you must specify an asymmetric ``KeySpec`` value and a ``KeyUsage`` value. For details, see &#91;Asymmetric keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;symmetric-asymmetric.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can use HMAC KMS keys (which are also symmetric keys) to generate and verify hash-based message authentication codes. To create an HMAC key, you must specify an HMAC ``KeySpec`` value and a ``KeyUsage`` value of ``GENERATE_VERIFY_MAC``. For details, see &#91;HMAC keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;hmac.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can also create symmetric encryption, asymmetric, and HMAC multi-Region primary keys. To create a multi-Region primary key, set the ``MultiRegion`` property to ``true``. For information about multi-Region keys, see &#91;Multi-Region keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You cannot use the ``AWS::KMS::Key`` resource to specify a KMS key with &#91;imported key material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys.html) or a KMS key in a &#91;custom key store&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;custom-key-store-overview.html).&lt;br&#x2F;&gt; *Regions*&lt;br&#x2F;&gt; KMS CloudFormation resources are available in all Regions in which KMS and CFN are supported. You can use the ``AWS::KMS::Key`` resource to create and manage all KMS key types that are supported in a Region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.key" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the KMS key. Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations.&lt;br&#x2F;&gt; When ``Enabled`` is ``true``, the *key state* of the KMS key is ``Enabled``. When ``Enabled`` is ``false``, the key state of the KMS key is ``Disabled``. The default value is ``true``.&lt;br&#x2F;&gt; The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the &#91;EnableKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_EnableKey.html), &#91;DisableKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DisableKey.html), or &#91;ScheduleKeyDeletion&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_ScheduleKeyDeletion.html) operations.&lt;br&#x2F;&gt; For information about the key states of a KMS key, see &#91;Key state: Effect on your KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-state.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="enable_key_rotation" /></td><td><code>boolean</code></td><td>Enables automatic rotation of the key material for the specified KMS key. By default, automatic key rotation is not enabled.&lt;br&#x2F;&gt; KMS supports automatic rotation only for symmetric encryption KMS keys (``KeySpec`` = ``SYMMETRIC_DEFAULT``). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin ``EXTERNAL``, omit the ``EnableKeyRotation`` property or set it to ``false``.&lt;br&#x2F;&gt; To enable automatic key rotation of the key material for a multi-Region KMS key, set ``EnableKeyRotation`` to ``true`` on the primary key (created by using ``AWS::KMS::Key``). KMS copies the rotation status to all replica keys. For details, see &#91;Rotating multi-Region keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-manage.html#multi-region-rotate) in the *Developer Guide*.&lt;br&#x2F;&gt; When you enable automatic rotation, KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. KMS retains all key material until you delete the KMS key. For detailed information about automatic key rotation, see &#91;Rotating KMS keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;rotate-keys.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="key_policy" /></td><td><code>object</code></td><td>The key policy to attach to the KMS key.&lt;br&#x2F;&gt; If you provide a key policy, it must meet the following criteria:&lt;br&#x2F;&gt;  +  The key policy must allow the caller to make a subsequent &#91;PutKeyPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_PutKeyPolicy.html) request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see &#91;Default key policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-policies.html#key-policy-default-allow-root-enable-iam) in the *Developer Guide*. (To omit this condition, set ``BypassPolicyLockoutSafetyCheck`` to true.)&lt;br&#x2F;&gt;  +  Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see &#91;Changes that I make are not always immediately visible&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *User Guide*.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If you do not provide a key policy, KMS attaches a default key policy to the KMS key. For more information, see &#91;Default key policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-policies.html#key-policy-default) in the *Developer Guide*.&lt;br&#x2F;&gt; A key policy document can include only the following characters:&lt;br&#x2F;&gt;  +  Printable ASCII characters&lt;br&#x2F;&gt;  +  Printable characters in the Basic Latin and Latin-1 Supplement character set&lt;br&#x2F;&gt;  +  The tab (``\u0009``), line feed (``\u000A``), and carriage return (``\u000D``) special characters&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; *Minimum*: ``1``&lt;br&#x2F;&gt; *Maximum*: ``32768``</td></tr>
<tr><td><CopyableCode code="key_usage" /></td><td><code>string</code></td><td>Determines the &#91;cryptographic operations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#cryptographic-operations) for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT``. This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created.&lt;br&#x2F;&gt;  If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.&lt;br&#x2F;&gt;  Select only one valid value.&lt;br&#x2F;&gt;  +  For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT``.&lt;br&#x2F;&gt;  +  For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY``.&lt;br&#x2F;&gt;  +  For asymmetric KMS keys with ECC key material, specify ``SIGN_VERIFY``.&lt;br&#x2F;&gt;  +  For asymmetric KMS keys with SM2 (China Regions only) key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY``.&lt;br&#x2F;&gt;  +  For HMAC KMS keys, specify ``GENERATE_VERIFY_MAC``.</td></tr>
<tr><td><CopyableCode code="origin" /></td><td><code>string</code></td><td>The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is ``AWS_KMS``, which means that KMS creates the key material.&lt;br&#x2F;&gt; To &#91;create a KMS key with no key material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys-create-cmk.html) (for imported key material), set this value to ``EXTERNAL``. For more information about importing key material into KMS, see &#91;Importing Key Material&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;importing-keys.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can ignore ``ENABLED`` when Origin is ``EXTERNAL``. When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false``. After you import the key material, ``ENABLED`` updated to ``true``. The KMS key can then be used for Cryptographic Operations. &lt;br&#x2F;&gt;  CFN doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values.</td></tr>
<tr><td><CopyableCode code="key_spec" /></td><td><code>string</code></td><td>Specifies the type of KMS key to create. The default value, ``SYMMETRIC_DEFAULT``, creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see &#91;Choosing a KMS key type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;symm-asymm-choose.html) in the *Developer Guide*.&lt;br&#x2F;&gt; The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see &#91;condition keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;policy-conditions.html#conditions-kms) in the *Developer Guide*.&lt;br&#x2F;&gt;  If you change the value of the ``KeySpec`` property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.&lt;br&#x2F;&gt;   &#91;services that are integrated with&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;features&#x2F;#AWS_Service_Integration) use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see &#91;Identifying asymmetric KMS keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;find-symm-asymm.html) in the *Developer Guide*.&lt;br&#x2F;&gt;   KMS supports the following key specs for KMS keys:&lt;br&#x2F;&gt;  +  Symmetric encryption key (default)&lt;br&#x2F;&gt;  +   ``SYMMETRIC_DEFAULT`` (AES-256-GCM)&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  +  HMAC keys (symmetric)&lt;br&#x2F;&gt;  +   ``HMAC_224`` &lt;br&#x2F;&gt;  +   ``HMAC_256`` &lt;br&#x2F;&gt;  +   ``HMAC_384`` &lt;br&#x2F;&gt;  +   ``HMAC_512`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  +  Asymmetric RSA key pairs&lt;br&#x2F;&gt;  +   ``RSA_2048`` &lt;br&#x2F;&gt;  +   ``RSA_3072`` &lt;br&#x2F;&gt;  +   ``RSA_4096`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  +  Asymmetric NIST-recommended elliptic curve key pairs&lt;br&#x2F;&gt;  +   ``ECC_NIST_P256`` (secp256r1)&lt;br&#x2F;&gt;  +   ``ECC_NIST_P384`` (secp384r1)&lt;br&#x2F;&gt;  +   ``ECC_NIST_P521`` (secp521r1)&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  +  Other asymmetric elliptic curve key pairs&lt;br&#x2F;&gt;  +   ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  + SM2 key pairs (China Regions only)&lt;br&#x2F;&gt;  + ``SM2``</td></tr>
<tr><td><CopyableCode code="multi_region" /></td><td><code>boolean</code></td><td>Creates a multi-Region primary key that you can replicate in other AWS-Regions. You can't change the ``MultiRegion`` value after the KMS key is created.&lt;br&#x2F;&gt; For a list of AWS-Regions in which multi-Region keys are supported, see &#91;Multi-Region keys in&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) in the **.&lt;br&#x2F;&gt;  If you change the value of the ``MultiRegion`` property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.&lt;br&#x2F;&gt;  For a multi-Region key, set to this property to ``true``. For a single-Region key, omit this property or set it to ``false``. The default value is ``false``.&lt;br&#x2F;&gt; *Multi-Region keys* are an KMS feature that lets you create multiple interoperable KMS keys in different AWS-Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS-Region and decrypt it in a different AWS-Region without making a cross-Region call or exposing the plaintext data. For more information, see &#91;Multi-Region keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You can create a symmetric encryption, HMAC, or asymmetric multi-Region KMS key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store.&lt;br&#x2F;&gt; To create a replica of this primary key in a different AWS-Region , create an &#91;AWS::KMS::ReplicaKey&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-kms-replicakey.html) resource in a CloudFormation stack in the replica Region. Specify the key ARN of this primary key.</td></tr>
<tr><td><CopyableCode code="pending_window_in_days" /></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before KMS deletes a KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.&lt;br&#x2F;&gt; When you remove a KMS key from a CloudFormation stack, KMS schedules the KMS key for deletion and starts the mandatory waiting period. The ``PendingWindowInDays`` property determines the length of waiting period. During the waiting period, the key state of KMS key is ``Pending Deletion`` or ``Pending Replica Deletion``, which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, KMS permanently deletes the KMS key.&lt;br&#x2F;&gt; KMS will not delete a &#91;multi-Region primary key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-overview.html) that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to ``PendingReplicaDeletion`` so it cannot be replicated or used in cryptographic operations. This state can persist indefinitely. When the last of its replica keys is deleted, the key state of the primary key changes to ``PendingDeletion`` and the waiting period specified by ``PendingWindowInDays`` begins. When this waiting period expires, KMS deletes the primary key. For details, see &#91;Deleting multi-Region keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;multi-region-keys-delete.html) in the *Developer Guide*.&lt;br&#x2F;&gt; You cannot use a CloudFormation template to cancel deletion of the KMS key after you remove it from the stack, regardless of the waiting period. If you specify a KMS key in your template, even one with the same name, CloudFormation creates a new KMS key. To cancel deletion of a KMS key, use the KMS console or the &#91;CancelKeyDeletion&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_CancelKeyDeletion.html) operation.&lt;br&#x2F;&gt; For information about the ``Pending Deletion`` and ``Pending Replica Deletion`` key states, see &#91;Key state: Effect on your KMS key&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-state.html) in the *Developer Guide*. For more information about deleting KMS keys, see the &#91;ScheduleKeyDeletion&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_ScheduleKeyDeletion.html) operation in the *API Reference* and &#91;Deleting KMS keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;deleting-keys.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Assigns one or more tags to the replica key.&lt;br&#x2F;&gt;  Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;abac.html) in the *Developer Guide*.&lt;br&#x2F;&gt;  For information about tags in KMS, see &#91;Tagging keys&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;tagging-keys.html) in the *Developer Guide*. For information about tags in CloudFormation, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bypass_policy_lockout_safety_check" /></td><td><code>boolean</code></td><td>Skips ("bypasses") the key policy lockout safety check. The default value is false.&lt;br&#x2F;&gt;  Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.&lt;br&#x2F;&gt; For more information, see &#91;Default key policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;key-policy-default.html#prevent-unmanageable-key) in the *Developer Guide*.&lt;br&#x2F;&gt;  Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent &#91;PutKeyPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_PutKeyPolicy.html) request on the KMS key.</td></tr>
<tr><td><CopyableCode code="rotation_period_in_days" /></td><td><code>integer</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
bypass_policy_lockout_safety_check,
rotation_period_in_days
FROM aws.kms.key
WHERE region = 'us-east-1' AND data__Identifier = '<KeyId>';
```


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

