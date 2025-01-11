---
title: keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_list_only
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

Lists <code>keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/keys/"><code>keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::KMS::Key</code> resource specifies an &#91;KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in KMSlong. You can use this resource to create symmetric encryption KMS keys, asymmetric KMS keys for encryption or signing, and symmetric HMAC KMS keys. You can use <code>AWS::KMS::Key</code> to create &#91;multi-Region primary keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-primary-key) of all supported types. To replicate a multi-Region key, use the <code>AWS::KMS::ReplicaKey</code> resource.<br />If you change the value of the <code>KeySpec</code>, <code>KeyUsage</code>, <code>Origin</code>, or <code>MultiRegion</code> properties of an existing KMS key, the update request fails, regardless of the value of the &#91;UpdateReplacePolicy attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing any of its immutable property values.<br />KMS replaced the term *customer master key (CMK)* with ** and *KMS key*. The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.<br />You can use symmetric encryption KMS keys to encrypt and decrypt small amounts of data, but they are more commonly used to generate data keys and data key pairs. You can also use a symmetric encryption KMS key to encrypt data stored in AWS services that are &#91;integrated with&#93;(https://docs.aws.amazon.com//kms/features/#AWS_Service_Integration). For more information, see &#91;Symmetric encryption KMS keys&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks) in the *Developer Guide*.<br />You can use asymmetric KMS keys to encrypt and decrypt data or sign messages and verify signatures. To create an asymmetric key, you must specify an asymmetric <code>KeySpec</code> value and a <code>KeyUsage</code> value. For details, see &#91;Asymmetric keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Developer Guide*.<br />You can use HMAC KMS keys (which are also symmetric keys) to generate and verify hash-based message authentication codes. To create an HMAC key, you must specify an HMAC <code>KeySpec</code> value and a <code>KeyUsage</code> value of <code>GENERATE_VERIFY_MAC</code>. For details, see &#91;HMAC keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) in the *Developer Guide*.<br />You can also create symmetric encryption, asymmetric, and HMAC multi-Region primary keys. To create a multi-Region primary key, set the <code>MultiRegion</code> property to <code>true</code>. For information about multi-Region keys, see &#91;Multi-Region keys in&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Developer Guide*.<br />You cannot use the <code>AWS::KMS::Key</code> resource to specify a KMS key with &#91;imported key material&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) or a KMS key in a &#91;custom key store&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html).<br />*Regions* <br />KMS CloudFormation resources are available in all Regions in which KMS and CFN are supported. You can use the <code>AWS::KMS::Key</code> resource to create and manage all KMS key types that are supported in a Region.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>keys</code> in a region.
```sql
SELECT
region,
key_id
FROM aws.kms.keys_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>keys_list_only</code> resource, see <a href="/providers/aws/kms/keys/#permissions"><code>keys</code></a>

