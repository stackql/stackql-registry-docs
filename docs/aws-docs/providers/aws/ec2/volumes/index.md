---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
Retrieves a list of <code>volumes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Elastic Block Store (Amazon EBS) volume.&lt;br&#x2F;&gt; When you use CFNlong to update an Amazon EBS volume that modifies ``Iops``, ``Size``, or ``VolumeType``, there is a cooldown period before another operation can occur. This can cause your stack to report being in ``UPDATE_IN_PROGRESS`` or ``UPDATE_ROLLBACK_IN_PROGRESS`` for long periods of time.&lt;br&#x2F;&gt; Amazon EBS does not support sizing down an Amazon EBS volume. CFNlong does not attempt to modify an Amazon EBS volume to a smaller size on rollback.&lt;br&#x2F;&gt; Some common scenarios when you might encounter a cooldown period for Amazon EBS include:&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds. When you attempt another update within the cooldown window, that update will be subject to a cooldown period.&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds but another change in your ``update-stack`` call fails. The rollback will be subject to a cooldown period.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information on the coo</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.volumes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>volume_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
volume_id
FROM aws.ec2.volumes
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>volumes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVolume,
ec2:DescribeVolumes,
ec2:DescribeVolumeAttribute,
ec2:ModifyVolumeAttribute,
ec2:CreateTags,
kms:GenerateDataKeyWithoutPlaintext,
kms:CreateGrant
```

### List
```json
ec2:DescribeVolumes,
ec2:DescribeTags,
ec2:DescribeVolumeAttribute
```

