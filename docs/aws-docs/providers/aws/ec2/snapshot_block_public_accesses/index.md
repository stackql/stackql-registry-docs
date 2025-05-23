---
title: snapshot_block_public_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_block_public_accesses
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

Creates, updates, deletes or gets a <code>snapshot_block_public_access</code> resource or lists <code>snapshot_block_public_accesses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_block_public_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.snapshot_block_public_accesses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of EBS Snapshot Block Public Access.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The identifier for the specified AWS account.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-snapshotblockpublicaccess.html"><code>AWS::EC2::SnapshotBlockPublicAccess</code></a>.

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
    <td><CopyableCode code="State, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>snapshot_block_public_accesses</code> in a region.
```sql
SELECT
region,
state,
account_id
FROM aws.ec2.snapshot_block_public_accesses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>snapshot_block_public_access</code>.
```sql
SELECT
region,
state,
account_id
FROM aws.ec2.snapshot_block_public_accesses
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshot_block_public_access</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.snapshot_block_public_accesses (
 State,
 region
)
SELECT 
'{{ State }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.snapshot_block_public_accesses (
 State,
 region
)
SELECT 
 '{{ State }}',
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
  - name: snapshot_block_public_access
    props:
      - name: State
        value: '{{ State }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.snapshot_block_public_accesses
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>snapshot_block_public_accesses</code> resource, the following permissions are required:

### Create
```json
ec2:EnableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```

### Read
```json
ec2:GetSnapshotBlockPublicAccessState
```

### Update
```json
ec2:EnableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```

### Delete
```json
ec2:DisableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```

### List
```json
ec2:GetSnapshotBlockPublicAccessState
```
