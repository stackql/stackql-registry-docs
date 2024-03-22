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
Gets an individual <code>volume</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>volume</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.volume</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>multi_attach_enabled</code></td><td><code>boolean</code></td><td>Indicates whether Amazon EBS Multi-Attach is enabled.&lt;br&#x2F;&gt; CFNlong does not currently support updating a single-attach volume to be multi-attach enabled, updating a multi-attach enabled volume to be single-attach, or updating the size or number of I&#x2F;O operations per second (IOPS) of a multi-attach enabled volume.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The identifier of the kms-key-long to use for Amazon EBS encryption. If ``KmsKeyId`` is specified, the encrypted state must be ``true``.&lt;br&#x2F;&gt; If you omit this property and your account is enabled for encryption by default, or *Encrypted* is set to ``true``, then the volume is encrypted using the default key specified for your account. If your account does not have a default key, then the volume is encrypted using the aws-managed-key.&lt;br&#x2F;&gt; Alternatively, if you want to specify a different key, you can specify one of the following:&lt;br&#x2F;&gt;  +  Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.&lt;br&#x2F;&gt;  +  Key alias. Specify the alias for the key, prefixed with ``alias&#x2F;``. For example, for a key with the alias ``my_cmk``, use ``alias&#x2F;my_cmk``. Or to specify the aws-managed-key, use ``alias&#x2F;aws&#x2F;ebs``.&lt;br&#x2F;&gt;  +  Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key&#x2F;1234abcd-12ab-34cd-56ef-1234567890ab.&lt;br&#x2F;&gt;  +  Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias&#x2F;ExampleAlias.</td></tr>
<tr><td><code>encrypted</code></td><td><code>boolean</code></td><td>Indicates whether the volume should be encrypted. The effect of setting the encryption state to ``true`` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see &#91;Encryption by default&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSEncryption.html#encryption-by-default) in the *Amazon Elastic Compute Cloud User Guide*.&lt;br&#x2F;&gt; Encrypted Amazon EBS volumes must be attached to instances that support Amazon EBS encryption. For more information, see &#91;Supported instance types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSEncryption.html#EBSEncryption_supported_instances).</td></tr>
<tr><td><code>size</code></td><td><code>integer</code></td><td>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.&lt;br&#x2F;&gt; The following are the supported volumes sizes for each volume type:&lt;br&#x2F;&gt;  +   ``gp2`` and ``gp3``: 1 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``io1``: 4 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``io2``: 4 - 65,536 GiB&lt;br&#x2F;&gt;  +   ``st1`` and ``sc1``: 125 - 16,384 GiB&lt;br&#x2F;&gt;  +   ``standard``: 1 - 1024 GiB</td></tr>
<tr><td><code>auto_enable_io</code></td><td><code>boolean</code></td><td>Indicates whether the volume is auto-enabled for I&#x2F;O operations. By default, Amazon EBS disables I&#x2F;O to the volume from attached EC2 instances when it determines that a volume's data is potentially inconsistent. If the consistency of the volume is not a concern, and you prefer that the volume be made available immediately if it's impaired, you can configure the volume to automatically enable I&#x2F;O.</td></tr>
<tr><td><code>outpost_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Outpost.</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The ID of the Availability Zone in which to create the volume. For example, ``us-east-1a``.</td></tr>
<tr><td><code>throughput</code></td><td><code>integer</code></td><td>The throughput to provision for a volume, with a maximum of 1,000 MiB&#x2F;s.&lt;br&#x2F;&gt; This parameter is valid only for ``gp3`` volumes. The default value is 125.&lt;br&#x2F;&gt; Valid Range: Minimum value of 125. Maximum value of 1000.</td></tr>
<tr><td><code>iops</code></td><td><code>integer</code></td><td>The number of I&#x2F;O operations per second (IOPS). For ``gp3``, ``io1``, and ``io2`` volumes, this represents the number of IOPS that are provisioned for the volume. For ``gp2`` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I&#x2F;O credits for bursting.&lt;br&#x2F;&gt; The following are the supported values for each volume type:&lt;br&#x2F;&gt;  +   ``gp3``: 3,000 - 16,000 IOPS&lt;br&#x2F;&gt;  +   ``io1``: 100 - 64,000 IOPS&lt;br&#x2F;&gt;  +   ``io2``: 100 - 256,000 IOPS&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For ``io2`` volumes, you can achieve up to 256,000 IOPS on &#91;instances built on the Nitro System&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;instance-types.html#ec2-nitro-instances). On other instances, you can achieve performance up to 32,000 IOPS.&lt;br&#x2F;&gt; This parameter is required for ``io1`` and ``io2`` volumes. The default for ``gp3`` volumes is 3,000 IOPS. This parameter is not supported for ``gp2``, ``st1``, ``sc1``, or ``standard`` volumes.</td></tr>
<tr><td><code>snapshot_id</code></td><td><code>string</code></td><td>The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size.</td></tr>
<tr><td><code>volume_type</code></td><td><code>string</code></td><td>The volume type. This parameter can be one of the following values:&lt;br&#x2F;&gt;  +  General Purpose SSD: ``gp2`` | ``gp3`` &lt;br&#x2F;&gt;  +  Provisioned IOPS SSD: ``io1`` | ``io2`` &lt;br&#x2F;&gt;  +  Throughput Optimized HDD: ``st1`` &lt;br&#x2F;&gt;  +  Cold HDD: ``sc1`` &lt;br&#x2F;&gt;  +  Magnetic: ``standard`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information, see &#91;Amazon EBS volume types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;EBSVolumeTypes.html) in the *Amazon Elastic Compute Cloud User Guide*.&lt;br&#x2F;&gt; Default: ``gp2``</td></tr>
<tr><td><code>volume_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to apply to the volume during creation.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.ec2.volume
WHERE data__Identifier = '<VolumeId>';
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

### Delete
```json
ec2:DeleteVolume,
ec2:CreateSnapshot,
ec2:DescribeSnapshots,
ec2:DeleteTags,
ec2:DescribeVolumes
```

