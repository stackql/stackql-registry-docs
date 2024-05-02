---
title: volume_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_attachment
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
Gets an individual <code>volume_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.&lt;br&#x2F;&gt; Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.&lt;br&#x2F;&gt; If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.&lt;br&#x2F;&gt; If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.volume_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>volume_id</code></td><td><code>string</code></td><td>The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an &#91;AWS::EC2::Volume&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the instance to which the volume attaches. This value can be a reference to an &#91;AWS::EC2::Instance&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.</td></tr>
<tr><td><code>device</code></td><td><code>string</code></td><td>The device name (for example, ``&#x2F;dev&#x2F;sdh`` or ``xvdh``).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
volume_id,
instance_id,
device
FROM aws.ec2.volume_attachment
WHERE data__Identifier = '<VolumeId>|<InstanceId>';
```

## Permissions

To operate on the <code>volume_attachment</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVolumes
```

### Delete
```json
ec2:DetachVolume,
ec2:DescribeVolumes
```

