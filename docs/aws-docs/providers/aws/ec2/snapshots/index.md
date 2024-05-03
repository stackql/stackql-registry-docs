---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
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

List of snapshots by region (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of snapshots by region (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.snapshots" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the snapshot.</td></tr>
<tr><td><CopyableCode code="data_encryption_key_id" /></td><td><code>string</code></td><td>The data encryption key identifier for the snapshot.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>Indicates whether the snapshot is encrypted.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Key Management Service (KMS) KMS key that was used to protect the volume encryption key for the parent volume.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="owner_alias" /></td><td><code>string</code></td><td>The Amazon Web Services owner alias.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="progress" /></td><td><code>string</code></td><td>The progress of the snapshot, as a percentage.</td></tr>
<tr><td><CopyableCode code="restore_expiry_time" /></td><td><code>string</code></td><td>Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.</td></tr>
<tr><td><CopyableCode code="snapshot_id" /></td><td><code>string</code></td><td>The ID of the snapshot. Each snapshot receives a unique identifier when it is created.</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>The time stamp when the snapshot was initiated.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The snapshot state.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper Key Management Service (KMS) permissions are not obtained) this field displays error state details.</td></tr>
<tr><td><CopyableCode code="storage_tier" /></td><td><code>string</code></td><td>The storage tier in which the snapshot is stored.</td></tr>
<tr><td><CopyableCode code="tag_set" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="volume_id" /></td><td><code>string</code></td><td>The ID of the volume that was used to create the snapshot.</td></tr>
<tr><td><CopyableCode code="volume_size" /></td><td><code>integer</code></td><td>The size of the volume, in GiB.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
description,
data_encryption_key_id,
encrypted,
kms_key_id,
outpost_arn,
owner_alias,
owner_id,
progress,
restore_expiry_time,
snapshot_id,
start_time,
status,
status_message,
storage_tier,
tag_set,
volume_id,
volume_size,
region
FROM aws.ec2.snapshots
WHERE region = '<region>';
```




