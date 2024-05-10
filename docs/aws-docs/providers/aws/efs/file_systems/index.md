---
title: file_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems
  - efs
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


Used to retrieve a list of <code>file_systems</code> in a region or to create or delete a <code>file_systems</code> resource, use <code>file_system</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::EFS::FileSystem`` resource creates a new, empty file system in EFSlong (EFS). You must create a mount target (&#91;AWS::EFS::MountTarget&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-efs-mounttarget.html)) to mount your EFS file system on an EC2 or other AWS cloud compute resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.file_systems" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td></td></tr>
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
file_system_id
FROM aws.efs.file_systems
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>file_system</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- file_system.iql (required properties only)
INSERT INTO aws.efs.file_systems (
 Encrypted,
 FileSystemTags,
 KmsKeyId,
 LifecyclePolicies,
 FileSystemProtection,
 PerformanceMode,
 ProvisionedThroughputInMibps,
 ThroughputMode,
 FileSystemPolicy,
 BypassPolicyLockoutSafetyCheck,
 BackupPolicy,
 AvailabilityZoneName,
 ReplicationConfiguration,
 region
)
SELECT 
'{{ Encrypted }}',
 '{{ FileSystemTags }}',
 '{{ KmsKeyId }}',
 '{{ LifecyclePolicies }}',
 '{{ FileSystemProtection }}',
 '{{ PerformanceMode }}',
 '{{ ProvisionedThroughputInMibps }}',
 '{{ ThroughputMode }}',
 '{{ FileSystemPolicy }}',
 '{{ BypassPolicyLockoutSafetyCheck }}',
 '{{ BackupPolicy }}',
 '{{ AvailabilityZoneName }}',
 '{{ ReplicationConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- file_system.iql (all properties)
INSERT INTO aws.efs.file_systems (
 Encrypted,
 FileSystemTags,
 KmsKeyId,
 LifecyclePolicies,
 FileSystemProtection,
 PerformanceMode,
 ProvisionedThroughputInMibps,
 ThroughputMode,
 FileSystemPolicy,
 BypassPolicyLockoutSafetyCheck,
 BackupPolicy,
 AvailabilityZoneName,
 ReplicationConfiguration,
 region
)
SELECT 
 '{{ Encrypted }}',
 '{{ FileSystemTags }}',
 '{{ KmsKeyId }}',
 '{{ LifecyclePolicies }}',
 '{{ FileSystemProtection }}',
 '{{ PerformanceMode }}',
 '{{ ProvisionedThroughputInMibps }}',
 '{{ ThroughputMode }}',
 '{{ FileSystemPolicy }}',
 '{{ BypassPolicyLockoutSafetyCheck }}',
 '{{ BackupPolicy }}',
 '{{ AvailabilityZoneName }}',
 '{{ ReplicationConfiguration }}',
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
  - name: file_system
    props:
      - name: Encrypted
        value: '{{ Encrypted }}'
      - name: FileSystemTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: LifecyclePolicies
        value:
          - TransitionToIA: '{{ TransitionToIA }}'
            TransitionToPrimaryStorageClass: '{{ TransitionToPrimaryStorageClass }}'
            TransitionToArchive: '{{ TransitionToArchive }}'
      - name: FileSystemProtection
        value:
          ReplicationOverwriteProtection: '{{ ReplicationOverwriteProtection }}'
      - name: PerformanceMode
        value: '{{ PerformanceMode }}'
      - name: ProvisionedThroughputInMibps
        value: null
      - name: ThroughputMode
        value: '{{ ThroughputMode }}'
      - name: FileSystemPolicy
        value: {}
      - name: BypassPolicyLockoutSafetyCheck
        value: '{{ BypassPolicyLockoutSafetyCheck }}'
      - name: BackupPolicy
        value:
          Status: '{{ Status }}'
      - name: AvailabilityZoneName
        value: '{{ AvailabilityZoneName }}'
      - name: ReplicationConfiguration
        value:
          Destinations:
            - FileSystemId: '{{ FileSystemId }}'
              Region: '{{ Region }}'
              AvailabilityZoneName: '{{ AvailabilityZoneName }}'
              KmsKeyId: '{{ KmsKeyId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.efs.file_systems
WHERE data__Identifier = '<FileSystemId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>file_systems</code> resource, the following permissions are required:

### Create
```json
elasticfilesystem:CreateFileSystem,
elasticfilesystem:DescribeReplicationConfigurations,
elasticfilesystem:TagResource,
elasticfilesystem:CreateReplicationConfiguration,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:PutBackupPolicy,
elasticfilesystem:PutFileSystemPolicy,
elasticfilesystem:PutLifecycleConfiguration,
elasticfilesystem:UpdateFileSystemProtection,
kms:DescribeKey,
kms:GenerateDataKeyWithoutPlaintext,
kms:CreateGrant
```

### Delete
```json
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DeleteFileSystem,
elasticfilesystem:DeleteReplicationConfiguration,
elasticfilesystem:DescribeReplicationConfigurations
```

### List
```json
elasticfilesystem:DescribeBackupPolicy,
elasticfilesystem:DescribeFileSystemPolicy,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeLifecycleConfiguration,
elasticfilesystem:DescribeReplicationConfigurations
```

