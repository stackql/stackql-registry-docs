---
title: volume_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_tags
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

Expands all tag keys and values for <code>volumes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Elastic Block Store (Amazon EBS) volume.<br />When you use CFNlong to update an Amazon EBS volume that modifies <code>Iops</code>, <code>Size</code>, or <code>VolumeType</code>, there is a cooldown period before another operation can occur. This can cause your stack to report being in <code>UPDATE_IN_PROGRESS</code> or <code>UPDATE_ROLLBACK_IN_PROGRESS</code> for long periods of time.<br />Amazon EBS does not support sizing down an Amazon EBS volume. CFNlong does not attempt to modify an Amazon EBS volume to a smaller size on rollback.<br />Some common scenarios when you might encounter a cooldown period for Amazon EBS include:<br />+ You successfully update an Amazon EBS volume and the update succeeds. When you attempt another update within the cooldown window, that update will be subject to a cooldown period.<br />+ You successfully update an Amazon EBS volume and the update succeeds but another change in your <code>update-stack</code> call fails. The rollback will be subject to a cooldown period.<br /><br />For more information on the coo</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volume_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="multi_attach_enabled" /></td><td><code>boolean</code></td><td>Indicates whether Amazon EBS Multi-Attach is enabled.<br />CFNlong does not currently support updating a single-attach volume to be multi-attach enabled, updating a multi-attach enabled volume to be single-attach, or updating the size or number of I/O operations per second (IOPS) of a multi-attach enabled volume.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The identifier of the kms-key-long to use for Amazon EBS encryption. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.<br />If you omit this property and your account is enabled for encryption by default, or *Encrypted* is set to <code>true</code>, then the volume is encrypted using the default key specified for your account. If your account does not have a default key, then the volume is encrypted using the aws-managed-key.<br />Alternatively, if you want to specify a different key, you can specify one of the following:<br />+ Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.<br />+ Key alias. Specify the alias for the key, prefixed with <code>alias/</code>. For example, for a key with the alias <code>my_cmk</code>, use <code>alias/my_cmk</code>. Or to specify the aws-managed-key, use <code>alias/aws/ebs</code>.<br />+ Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.<br />+ Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>Indicates whether the volume should be encrypted. The effect of setting the encryption state to <code>true</code> depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see &#91;Encryption by default&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the *Amazon Elastic Compute Cloud User Guide*.<br />Encrypted Amazon EBS volumes must be attached to instances that support Amazon EBS encryption. For more information, see &#91;Supported instance types&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances).</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.<br />The following are the supported volumes sizes for each volume type:<br />+ <code>gp2</code> and <code>gp3</code>: 1 - 16,384 GiB<br />+ <code>io1</code>: 4 - 16,384 GiB<br />+ <code>io2</code>: 4 - 65,536 GiB<br />+ <code>st1</code> and <code>sc1</code>: 125 - 16,384 GiB<br />+ <code>standard</code>: 1 - 1024 GiB</td></tr>
<tr><td><CopyableCode code="auto_enable_io" /></td><td><code>boolean</code></td><td>Indicates whether the volume is auto-enabled for I/O operations. By default, Amazon EBS disables I/O to the volume from attached EC2 instances when it determines that a volume's data is potentially inconsistent. If the consistency of the volume is not a concern, and you prefer that the volume be made available immediately if it's impaired, you can configure the volume to automatically enable I/O.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Outpost.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The ID of the Availability Zone in which to create the volume. For example, <code>us-east-1a</code>.</td></tr>
<tr><td><CopyableCode code="throughput" /></td><td><code>integer</code></td><td>The throughput to provision for a volume, with a maximum of 1,000 MiB/s.<br />This parameter is valid only for <code>gp3</code> volumes. The default value is 125.<br />Valid Range: Minimum value of 125. Maximum value of 1000.</td></tr>
<tr><td><CopyableCode code="iops" /></td><td><code>integer</code></td><td>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.<br />The following are the supported values for each volume type:<br />+ <code>gp3</code>: 3,000 - 16,000 IOPS<br />+ <code>io1</code>: 100 - 64,000 IOPS<br />+ <code>io2</code>: 100 - 256,000 IOPS<br /><br />For <code>io2</code> volumes, you can achieve up to 256,000 IOPS on &#91;instances built on the Nitro System&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances). On other instances, you can achieve performance up to 32,000 IOPS.<br />This parameter is required for <code>io1</code> and <code>io2</code> volumes. The default for <code>gp3</code> volumes is 3,000 IOPS. This parameter is not supported for <code>gp2</code>, <code>st1</code>, <code>sc1</code>, or <code>standard</code> volumes.</td></tr>
<tr><td><CopyableCode code="snapshot_id" /></td><td><code>string</code></td><td>The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size.</td></tr>
<tr><td><CopyableCode code="volume_type" /></td><td><code>string</code></td><td>The volume type. This parameter can be one of the following values:<br />+ General Purpose SSD: <code>gp2</code> | <code>gp3</code> <br />+ Provisioned IOPS SSD: <code>io1</code> | <code>io2</code> <br />+ Throughput Optimized HDD: <code>st1</code> <br />+ Cold HDD: <code>sc1</code> <br />+ Magnetic: <code>standard</code> <br /><br />For more information, see &#91;Amazon EBS volume types&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html) in the *Amazon Elastic Compute Cloud User Guide*.<br />Default: <code>gp2</code></td></tr>
<tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>volumes</code> in a region.
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
tag_key,
tag_value
FROM aws.ec2.volume_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>volume_tags</code> resource, see <a href="/providers/aws/ec2/volumes/#permissions"><code>volumes</code></a>


