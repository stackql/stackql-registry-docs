---
title: volume_attachments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_attachments_list_only
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

Lists <code>volume_attachments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/volume_attachments/"><code>volume_attachments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_attachments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.<br />Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.<br />If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.<br />If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volume_attachments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td>The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an &#91;AWS::EC2::Volume&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance to which the volume attaches. This value can be a reference to an &#91;AWS::EC2::Instance&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.</td></tr>
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
Lists all <code>volume_attachments</code> in a region.
```sql
SELECT
region,
volume_id,
instance_id
FROM aws.ec2.volume_attachments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>volume_attachments_list_only</code> resource, see <a href="/providers/aws/ec2/volume_attachments/#permissions"><code>volume_attachments</code></a>

