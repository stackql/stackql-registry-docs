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
<tr><td><b>Description</b></td><td>volume_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.volume_attachment</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
volume_id,
instance_id,
device
FROM awscc.ec2.volume_attachment
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

