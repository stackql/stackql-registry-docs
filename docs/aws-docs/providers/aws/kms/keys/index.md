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

Creates, updates, deletes or gets a <code>key</code> resource or lists <code>keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::KMS::Key</code> resource specifies an &#91;KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in KMSlong. You can use this resource to create symmetric encryption KMS keys, asymmetric KMS keys for encryption or signing, and symmetric HMAC KMS keys. You can use <code>AWS::KMS::Key</code> to create &#91;multi-Region primary keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-primary-key) of all supported types. To replicate a multi-Region key, use the <code>AWS::KMS::ReplicaKey</code> resource.<br />If you change the value of the <code>KeySpec</code>, <code>KeyUsage</code>, <code>Origin</code>, or <code>MultiRegion</code> properties of an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing any of its immutable property values.<br />KMS replaced the term *customer master key (CMK)* with ** and *KMS key*. The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.<br />You can use symmetric encryption KMS keys to encrypt and decrypt small amounts of data, but they are more commonly used to generate data keys and data key pairs. You can also use a symmetric encryption KMS key to encrypt data stored in AWS services that are &#91;integrated with&#93;(https://docs.aws.amazon.com//kms/features/#AWS_Service_Integration). For more information, see &#91;Symmetric encryption KMS keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks) in the *Developer Guide*.<br />You can use asymmetric KMS keys to encrypt and decrypt data or sign messages and verify signatures. To create an asymmetric key, you must specify an asymmetric <code>KeySpec</code> value and a <code>KeyUsage</code> value. For details, see &#91;Asymmetric keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Developer Guide*.<br />You can use HMAC KMS keys (which are also symmetric keys) to generate and verify hash-based message authentication codes. To create an HMAC key, you must specify an HMAC <code>KeySpec</code> value and a <code>KeyUsage</code> value of <code>GENERATE_VERIFY_MAC</code>. For details, see &#91;HMAC keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) in the *Developer Guide*.<br />You can also create symmetric encryption, asymmetric, and HMAC multi-Region primary keys. To create a multi-Region primary key, set the <code>MultiRegion</code> property to <code>true</code>. For information about multi-Region keys, see &#91;Multi-Region keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Developer Guide*.<br />You cannot use the <code>AWS::KMS::Key</code> resource to specify a KMS key with &#91;imported key material&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) or a KMS key in a &#91;custom key store&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html).<br />*Regions* <br />KMS CloudFormation resources are available in all Regions in which KMS and CFN are supported. You can use the <code>AWS::KMS::Key</code> resource to create and manage all KMS key types that are supported in a Region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the KMS key. Use a description that helps you to distinguish this KMS key from others in the account, such as its intended use.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the KMS key is enabled. Disabled KMS keys cannot be used in cryptographic operations.<br />When <code>Enabled</code> is <code>true</code>, the *key state* of the KMS key is <code>Enabled</code>. When <code>Enabled</code> is <code>false</code>, the key state of the KMS key is <code>Disabled</code>. The default value is <code>true</code>.<br />The actual key state of the KMS key might be affected by actions taken outside of CloudFormation, such as running the &#91;EnableKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html), &#91;DisableKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKey.html), or &#91;ScheduleKeyDeletion&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html) operations.<br />For information about the key states of a KMS key, see &#91;Key state: Effect on your KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="enable_key_rotation" /></td><td><code>boolean</code></td><td>Enables automatic rotation of the key material for the specified KMS key. By default, automatic key rotation is not enabled.<br />KMS supports automatic rotation only for symmetric encryption KMS keys (<code>KeySpec</code> = <code>SYMMETRIC_DEFAULT</code>). For asymmetric KMS keys, HMAC KMS keys, and KMS keys with Origin <code>EXTERNAL</code>, omit the <code>EnableKeyRotation</code> property or set it to <code>false</code>.<br />To enable automatic key rotation of the key material for a multi-Region KMS key, set <code>EnableKeyRotation</code> to <code>true</code> on the primary key (created by using <code>AWS::KMS::Key</code>). KMS copies the rotation status to all replica keys. For details, see &#91;Rotating multi-Region keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-manage.html#multi-region-rotate) in the *Developer Guide*.<br />When you enable automatic rotation, KMS automatically creates new key material for the KMS key one year after the enable date and every year thereafter. KMS retains all key material until you delete the KMS key. For detailed information about automatic key rotation, see &#91;Rotating KMS keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="key_policy" /></td><td><code>object</code></td><td>The key policy to attach to the KMS key.<br />If you provide a key policy, it must meet the following criteria:<br />+ The key policy must allow the caller to make a subsequent &#91;PutKeyPolicy&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see &#91;Default key policy&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam) in the *Developer Guide*. (To omit this condition, set <code>BypassPolicyLockoutSafetyCheck</code> to true.)<br />+ Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see &#91;Changes that I make are not always immediately visible&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *User Guide*.<br /><br />If you do not provide a key policy, KMS attaches a default key policy to the KMS key. For more information, see &#91;Default key policy&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) in the *Developer Guide*.<br />A key policy document can include only the following characters:<br />+ Printable ASCII characters<br />+ Printable characters in the Basic Latin and Latin-1 Supplement character set<br />+ The tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>) special characters<br /><br />*Minimum*: <code>1</code> <br />*Maximum*: <code>32768</code></td></tr>
<tr><td><CopyableCode code="key_usage" /></td><td><code>string</code></td><td>Determines the &#91;cryptographic operations&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) for which you can use the KMS key. The default value is <code>ENCRYPT_DECRYPT</code>. This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the <code>KeyUsage</code> value after the KMS key is created.<br />If you change the value of the <code>KeyUsage</code> property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.<br />Select only one valid value.<br />+ For symmetric encryption KMS keys, omit the parameter or specify <code>ENCRYPT_DECRYPT</code>.<br />+ For HMAC KMS keys (symmetric), specify <code>GENERATE_VERIFY_MAC</code>.<br />+ For asymmetric KMS keys with RSA key pairs, specify <code>ENCRYPT_DECRYPT</code> or <code>SIGN_VERIFY</code>.<br />+ For asymmetric KMS keys with NIST-recommended elliptic curve key pairs, specify <code>SIGN_VERIFY</code> or <code>KEY_AGREEMENT</code>.<br />+ For asymmetric KMS keys with <code>ECC_SECG_P256K1</code> key pairs specify <code>SIGN_VERIFY</code>.<br />+ For asymmetric KMS keys with SM2 key pairs (China Regions only), specify <code>ENCRYPT_DECRYPT</code>, <code>SIGN_VERIFY</code>, or <code>KEY_AGREEMENT</code>.</td></tr>
<tr><td><CopyableCode code="origin" /></td><td><code>string</code></td><td>The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is <code>AWS_KMS</code>, which means that KMS creates the key material.<br />To &#91;create a KMS key with no key material&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html) (for imported key material), set this value to <code>EXTERNAL</code>. For more information about importing key material into KMS, see &#91;Importing Key Material&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *Developer Guide*.<br />You can ignore <code>ENABLED</code> when Origin is <code>EXTERNAL</code>. When a KMS key with Origin <code>EXTERNAL</code> is created, the key state is <code>PENDING_IMPORT</code> and <code>ENABLED</code> is <code>false</code>. After you import the key material, <code>ENABLED</code> updated to <code>true</code>. The KMS key can then be used for Cryptographic Operations. <br />CFN doesn't support creating an <code>Origin</code> parameter of the <code>AWS_CLOUDHSM</code> or <code>EXTERNAL_KEY_STORE</code> values.</td></tr>
<tr><td><CopyableCode code="key_spec" /></td><td><code>string</code></td><td>Specifies the type of KMS key to create. The default value, <code>SYMMETRIC_DEFAULT</code>, creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, <code>SYMMETRIC_DEFAULT</code> creates a 128-bit symmetric key that uses SM4 encryption. You can't change the <code>KeySpec</code> value after the KMS key is created. For help choosing a key spec for your KMS key, see &#91;Choosing a KMS key type&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html) in the *Developer Guide*.<br />The <code>KeySpec</code> property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see &#91;condition keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms) in the *Developer Guide*.<br />If you change the value of the <code>KeySpec</code> property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.<br />&#91;services that are integrated with&#93;(https://docs.aws.amazon.com/kms/features/#AWS_Service_Integration) use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see &#91;Identifying asymmetric KMS keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html) in the *Developer Guide*.<br />KMS supports the following key specs for KMS keys:<br />+ Symmetric encryption key (default)<br />+ <code>SYMMETRIC_DEFAULT</code> (AES-256-GCM)<br /><br />+ HMAC keys (symmetric)<br />+ <code>HMAC_224</code> <br />+ <code>HMAC_256</code> <br />+ <code>HMAC_384</code> <br />+ <code>HMAC_512</code> <br /><br />+ Asymmetric RSA key pairs (encryption and decryption *or* signing and verification)<br />+ <code>RSA_2048</code> <br />+ <code>RSA_3072</code> <br />+ <code>RSA_4096</code> <br /><br />+ Asymmetric NIST-recommended elliptic curve key pairs (signing and verification *or* deriving shared secrets)<br />+ <code>ECC_NIST_P256</code> (secp256r1)<br />+ <code>ECC_NIST_P384</code> (secp384r1)<br />+ <code>ECC_NIST_P521</code> (secp521r1)<br /><br />+ Other asymmetric elliptic curve key pairs (signing and verification)<br />+ <code>ECC_SECG_P256K1</code> (secp256k1), commonly used for cryptocurrencies.<br /><br />+ SM2 key pairs (encryption and decryption *or* signing and verification *or* deriving shared secrets)<br />+ <code>SM2</code> (China Regions only)</td></tr>
<tr><td><CopyableCode code="multi_region" /></td><td><code>boolean</code></td><td>Creates a multi-Region primary key that you can replicate in other AWS-Regions. You can't change the <code>MultiRegion</code> value after the KMS key is created.<br />For a list of AWS-Regions in which multi-Region keys are supported, see &#91;Multi-Region keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the **.<br />If you change the value of the <code>MultiRegion</code> property on an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.<br />For a multi-Region key, set to this property to <code>true</code>. For a single-Region key, omit this property or set it to <code>false</code>. The default value is <code>false</code>.<br />*Multi-Region keys* are an KMS feature that lets you create multiple interoperable KMS keys in different AWS-Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them to encrypt data in one AWS-Region and decrypt it in a different AWS-Region without making a cross-Region call or exposing the plaintext data. For more information, see &#91;Multi-Region keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Developer Guide*.<br />You can create a symmetric encryption, HMAC, or asymmetric multi-Region KMS key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store.<br />To create a replica of this primary key in a different AWS-Region , create an &#91;AWS::KMS::ReplicaKey&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html) resource in a CloudFormation stack in the replica Region. Specify the key ARN of this primary key.</td></tr>
<tr><td><CopyableCode code="pending_window_in_days" /></td><td><code>integer</code></td><td>Specifies the number of days in the waiting period before KMS deletes a KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.<br />When you remove a KMS key from a CloudFormation stack, KMS schedules the KMS key for deletion and starts the mandatory waiting period. The <code>PendingWindowInDays</code> property determines the length of waiting period. During the waiting period, the key state of KMS key is <code>Pending Deletion</code> or <code>Pending Replica Deletion</code>, which prevents the KMS key from being used in cryptographic operations. When the waiting period expires, KMS permanently deletes the KMS key.<br />KMS will not delete a &#91;multi-Region primary key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) that has replica keys. If you remove a multi-Region primary key from a CloudFormation stack, its key state changes to <code>PendingReplicaDeletion</code> so it cannot be replicated or used in cryptographic operations. This state can persist indefinitely. When the last of its replica keys is deleted, the key state of the primary key changes to <code>PendingDeletion</code> and the waiting period specified by <code>PendingWindowInDays</code> begins. When this waiting period expires, KMS deletes the primary key. For details, see &#91;Deleting multi-Region keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-delete.html) in the *Developer Guide*.<br />You cannot use a CloudFormation template to cancel deletion of the KMS key after you remove it from the stack, regardless of the waiting period. If you specify a KMS key in your template, even one with the same name, CloudFormation creates a new KMS key. To cancel deletion of a KMS key, use the KMS console or the &#91;CancelKeyDeletion&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_CancelKeyDeletion.html) operation.<br />For information about the <code>Pending Deletion</code> and <code>Pending Replica Deletion</code> key states, see &#91;Key state: Effect on your KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Developer Guide*. For more information about deleting KMS keys, see the &#91;ScheduleKeyDeletion&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html) operation in the *API Reference* and &#91;Deleting KMS keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Assigns one or more tags to the replica key.<br />Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the *Developer Guide*.<br />For information about tags in KMS, see &#91;Tagging keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html) in the *Developer Guide*. For information about tags in CloudFormation, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bypass_policy_lockout_safety_check" /></td><td><code>boolean</code></td><td>Skips ("bypasses") the key policy lockout safety check. The default value is false.<br />Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.<br />For more information, see &#91;Default key policy&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the *Developer Guide*.<br />Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent &#91;PutKeyPolicy&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.</td></tr>
<tr><td><CopyableCode code="rotation_period_in_days" /></td><td><code>integer</code></td><td>Specifies a custom period of time between each rotation date. If no value is specified, the default value is 365 days.<br />The rotation period defines the number of days after you enable automatic key rotation that KMS will rotate your key material, and the number of days between each automatic rotation thereafter.<br />You can use the &#91;kms:RotationPeriodInDays&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-rotation-period-in-days) condition key to further constrain the values that principals can specify in the <code>RotationPeriodInDays</code> parameter.<br />For more information about rotating KMS keys and automatic rotation, see &#91;Rotating keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html"><code>AWS::KMS::Key</code></a>.

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
Gets all <code>keys</code> in a region.
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
FROM aws.kms.keys
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>key</code>.
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
FROM aws.kms.keys
WHERE region = 'us-east-1' AND data__Identifier = '<KeyId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
kms:ListKeys,
kms:DescribeKey
```
