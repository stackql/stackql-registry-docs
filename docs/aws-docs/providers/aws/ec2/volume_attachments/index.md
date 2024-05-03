---
title: volume_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_attachments
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

Used to retrieve a list of <code>volume_attachments</code> in a region or create a <code>volume_attachments</code> resource, use <code>volume_attachment</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.&lt;br&#x2F;&gt; Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.&lt;br&#x2F;&gt; If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.&lt;br&#x2F;&gt; If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volume_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="volume_id" /></td><td><code>undefined</code></td><td>The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an &#91;AWS::EC2::Volume&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>undefined</code></td><td>The ID of the instance to which the volume attaches. This value can be a reference to an &#91;AWS::EC2::Instance&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
volume_id,
instance_id
FROM aws.ec2.volume_attachments
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>volume_attachments</code> resource, the following permissions are required:

### Create
```json
ec2:AttachVolume,
ec2:DescribeVolumes
```

### List
```json
ec2:DescribeVolumes
```
