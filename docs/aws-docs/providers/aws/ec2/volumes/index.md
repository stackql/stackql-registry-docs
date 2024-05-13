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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>volumes</code> in a region or to create or delete a <code>volumes</code> resource, use <code>volume</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Amazon Elastic Block Store (Amazon EBS) volume.&lt;br&#x2F;&gt; When you use CFNlong to update an Amazon EBS volume that modifies <code>Iops</code>, <code>Size</code>, or <code>VolumeType</code>, there is a cooldown period before another operation can occur. This can cause your stack to report being in <code>UPDATE_IN_PROGRESS</code> or <code>UPDATE_ROLLBACK_IN_PROGRESS</code> for long periods of time.&lt;br&#x2F;&gt; Amazon EBS does not support sizing down an Amazon EBS volume. CFNlong does not attempt to modify an Amazon EBS volume to a smaller size on rollback.&lt;br&#x2F;&gt; Some common scenarios when you might encounter a cooldown period for Amazon EBS include:&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds. When you attempt another update within the cooldown window, that update will be subject to a cooldown period.&lt;br&#x2F;&gt;  +  You successfully update an Amazon EBS volume and the update succeeds but another change in your <code>update-stack</code> call fails. The rollback will be subject to a cooldown period.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information on the coo</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.volumes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="AvailabilityZone, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
volume_id
FROM aws.ec2.volumes
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>volume</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.volumes (
 AvailabilityZone,
 region
)
SELECT 
'{{ AvailabilityZone }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.volumes (
 MultiAttachEnabled,
 KmsKeyId,
 Encrypted,
 Size,
 AutoEnableIO,
 OutpostArn,
 AvailabilityZone,
 Throughput,
 Iops,
 SnapshotId,
 VolumeType,
 Tags,
 region
)
SELECT 
 '{{ MultiAttachEnabled }}',
 '{{ KmsKeyId }}',
 '{{ Encrypted }}',
 '{{ Size }}',
 '{{ AutoEnableIO }}',
 '{{ OutpostArn }}',
 '{{ AvailabilityZone }}',
 '{{ Throughput }}',
 '{{ Iops }}',
 '{{ SnapshotId }}',
 '{{ VolumeType }}',
 '{{ Tags }}',
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
  - name: volume
    props:
      - name: MultiAttachEnabled
        value: '{{ MultiAttachEnabled }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Encrypted
        value: '{{ Encrypted }}'
      - name: Size
        value: '{{ Size }}'
      - name: AutoEnableIO
        value: '{{ AutoEnableIO }}'
      - name: OutpostArn
        value: '{{ OutpostArn }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: Throughput
        value: '{{ Throughput }}'
      - name: Iops
        value: '{{ Iops }}'
      - name: SnapshotId
        value: '{{ SnapshotId }}'
      - name: VolumeType
        value: '{{ VolumeType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ec2.volumes
WHERE data__Identifier = '<VolumeId>'
AND region = 'us-east-1';
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

### Delete
```json
ec2:DeleteVolume,
ec2:CreateSnapshot,
ec2:DescribeSnapshots,
ec2:DeleteTags,
ec2:DescribeVolumes
```

### List
```json
ec2:DescribeVolumes,
ec2:DescribeTags,
ec2:DescribeVolumeAttribute
```

