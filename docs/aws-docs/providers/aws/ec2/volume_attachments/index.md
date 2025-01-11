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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>volume_attachment</code> resource or lists <code>volume_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.<br />Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.<br />If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the "running" state. To detach the root volume, stop the instance first.<br />If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volume_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td>The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an &#91;AWS::EC2::Volume&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance to which the volume attaches. This value can be a reference to an &#91;AWS::EC2::Instance&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance.</td></tr>
<tr><td><CopyableCode code="device" /></td><td><code>string</code></td><td>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-volumeattachment.html"><code>AWS::EC2::VolumeAttachment</code></a>.

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
    <td><CopyableCode code="VolumeId, InstanceId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>volume_attachments</code> in a region.
```sql
SELECT
region,
volume_id,
instance_id,
device
FROM aws.ec2.volume_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>volume_attachment</code>.
```sql
SELECT
region,
volume_id,
instance_id,
device
FROM aws.ec2.volume_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<VolumeId>|<InstanceId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volume_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.volume_attachments (
 VolumeId,
 InstanceId,
 region
)
SELECT 
'{{ VolumeId }}',
 '{{ InstanceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.volume_attachments (
 VolumeId,
 InstanceId,
 Device,
 region
)
SELECT 
 '{{ VolumeId }}',
 '{{ InstanceId }}',
 '{{ Device }}',
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
  - name: volume_attachment
    props:
      - name: VolumeId
        value: '{{ VolumeId }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: Device
        value: '{{ Device }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.volume_attachments
WHERE data__Identifier = '<VolumeId|InstanceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>volume_attachments</code> resource, the following permissions are required:

### Create
```json
ec2:AttachVolume,
ec2:DescribeVolumes
```

### Read
```json
ec2:DescribeVolumes
```

### Delete
```json
ec2:DetachVolume,
ec2:DescribeVolumes
```

### List
```json
ec2:DescribeVolumes
```
