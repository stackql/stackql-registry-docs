---
title: volume
hide_title: false
hide_table_of_contents: false
keywords:
  - volume
  - ec2
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


Gets or updates an individual <code>volume</code> resource, use <code>volumes</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Elastic Block Store (Amazon EBS) volume.&lt;br&#x2F;&gt; When you use CFNlong to update an Amazon EBS volume that modifies ``Iops``, ``Size``, or ``VolumeType``, there is a cooldown period before another operation can occur. This can cause your stack to report being in ``UPDATE_IN_PROGRESS`` or ``UPDATE_ROLLBACK_IN_PROGRESS`` for long periods of time.&lt;br&#x2F;&gt; Amazon EBS does not support sizing down an Amazon EBS volume. CFNlong does not attempt to modify an Amazon EBS volume to a smaller size on rollback.&lt;br&#x2F;&gt; Some common scenarios when you might encounter a cooldown period for Amazon EBS include:&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds. When you attempt another update within the cooldown window, that update will be subject to a cooldown period.&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds but another change in your ``update-stack`` call fails. The rollback will be subject to a cooldown period.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information on the coo</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volume" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="multi_attach_enabled" /></td><td><code>boolean</code></td><td>Indicates whether Amazon EBS Multi-Attach is enabled.&lt;br&#x2F;&gt; CFNlong does not currently support updating a single-attach volume to be multi-attach enabled, updating a multi-attach enabled volume to be single-attach, or updating the size or number of I&#x2F;O operations per second (IOPS) of a multi-attach enabled volume.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The identifier of the kms-key-long to use for Amazon EBS encryption. If ``KmsKeyId`` is specified, the encrypted state must be ``true``.&lt;br&#x2F;&gt; If you omit this property and your account is enabled for encryption by default, or *Encrypted* is set to ``true``, then the volume is encrypted using the default key specified for your account. If your account does not have a default key, then the volume is encrypted using the aws-managed-key.&lt;br&#x2F;&gt; Alternatively, if you want to specify a different key, you can specify one of the following:&lt;br&#x2F;&gt;  +  Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.&lt;br&#x2F;&gt;  +  Key alias. Specify the alias for the key, prefixed with ``alias&#x2F;``. For example, for a key with the alias ``my_cmk``, use ``alias&#x2F;my_cmk``. Or to specify the aws-managed-key, use ``alias&#x2F;aws&#x2F;ebs``.&lt;br&#x2F;&gt;  +  Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key&#x2F;1234abcd-12ab-34cd-56ef-1234567890ab.&lt;br&#x2F;&gt;  +  Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias&#x2F;ExampleAlias.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>Indicates whether the volume should be encrypted. The effect of setting the encryption state to ``true`` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see &#91;Encryption by default&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSEncryption.html#encryption-by-default) in the *Amazon Elastic Compute Cloud User Guide*.&lt;br&#x2F;&gt; Encrypted Amazon EBS volumes must be attached to instances that support Amazon EBS encryption. For more information, see &#91;Supported instance types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSEncryption.html#EBSEncryption_supported_instances).</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.&lt;br&#x2F;&gt; The following are the supported volumes sizes for each volume type:&lt;br&#x2F;&gt;  +   ``gp2`` and ``gp3``: 1 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``io1``: 4 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``io2``: 4 - 65,536 GiB&lt;br&#x2F;&gt;  +   ``st1`` and ``sc1``: 125 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``standard``: 1 - 1024 GiB</td></tr>
<tr><td><CopyableCode code="auto_enable_io" /></td><td><code>boolean</code></td><td>Indicates whether the volume is auto-enabled for I&#x2F;O operations. By default, Amazon EBS disables I&#x2F;O to the volume from attached EC2 instances when it determines that a volume's data is potentially inconsistent. If the consistency of the volume is not a concern, and you prefer that the volume be made available immediately if it's impaired, you can configure the volume to automatically enable I&#x2F;O.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Outpost.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The ID of the Availability Zone in which to create the volume. For example, ``us-east-1a``.</td></tr>
<tr><td><CopyableCode code="throughput" /></td><td><code>integer</code></td><td>The throughput to provision for a volume, with a maximum of 1,000 MiB&#x2F;s.&lt;br&#x2F;&gt; This parameter is valid only for ``gp3`` volumes. The default value is 125.&lt;br&#x2F;&gt; Valid Range: Minimum value of 125. Maximum value of 1000.</td></tr>
<tr><td><CopyableCode code="iops" /></td><td><code>integer</code></td><td>The number of I&#x2F;O operations per second (IOPS). For ``gp3``, ``io1``, and ``io2`` volumes, this represents the number of IOPS that are provisioned for the volume. For ``gp2`` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I&#x2F;O credits for bursting.&lt;br&#x2F;&gt; The following are the supported values for each volume type:&lt;br&#x2F;&gt;  +   ``gp3``: 3,000 - 16,000 IOPS&lt;br&#x2F;&gt;  +   ``io1``: 100 - 64,000 IOPS&lt;br&#x2F;&gt;  +   ``io2``: 100 - 256,000 IOPS&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For ``io2`` volumes, you can achieve up to 256,000 IOPS on &#91;instances built on the Nitro System&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;instance-types.html#ec2-nitro-instances). On other instances, you can achieve performance up to 32,000 IOPS.&lt;br&#x2F;&gt; This parameter is required for ``io1`` and ``io2`` volumes. The default for ``gp3`` volumes is 3,000 IOPS. This parameter is not supported for ``gp2``, ``st1``, ``sc1``, or ``standard`` volumes.</td></tr>
<tr><td><CopyableCode code="snapshot_id" /></td><td><code>string</code></td><td>The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size.</td></tr>
<tr><td><CopyableCode code="volume_type" /></td><td><code>string</code></td><td>The volume type. This parameter can be one of the following values:&lt;br&#x2F;&gt;  +  General Purpose SSD: ``gp2`` | ``gp3`` &lt;br&#x2F;&gt;  +  Provisioned IOPS SSD: ``io1`` | ``io2`` &lt;br&#x2F;&gt;  +  Throughput Optimized HDD: ``st1`` &lt;br&#x2F;&gt;  +  Cold HDD: ``sc1`` &lt;br&#x2F;&gt;  +  Magnetic: ``standard`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information, see &#91;Amazon EBS volume types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSVolumeTypes.html) in the *Amazon Elastic Compute Cloud User Guide*.&lt;br&#x2F;&gt; Default: ``gp2``</td></tr>
<tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the volume during creation.</td></tr>
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
multi_attach_enabled,
kms_key_id,
encrypted,
size,
auto_enable_io,
outpost_arn,
availability_zone,
throughput,
iops,
snapshot_id,
volume_type,
volume_id,
tags
FROM aws.ec2.volume
WHERE region = 'us-east-1' AND data__Identifier = '<VolumeId>';
```


## Permissions

To operate on the <code>volume</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVolumes,
ec2:DescribeVolumeAttribute,
ec2:DescribeTags
```

### Update
```json
ec2:ModifyVolume,
ec2:ModifyVolumeAttribute,
ec2:DescribeVolumeAttribute,
ec2:DescribeVolumesModifications,
ec2:DescribeVolumes,
ec2:CreateTags,
ec2:DeleteTags
```

