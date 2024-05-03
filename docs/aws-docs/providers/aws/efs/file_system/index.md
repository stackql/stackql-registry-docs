---
title: file_system
hide_title: false
hide_table_of_contents: false
keywords:
  - file_system
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

Gets or operates on an individual <code>file_system</code> resource, use <code>file_systems</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_system</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::EFS::FileSystem`` resource creates a new, empty file system in EFSlong (EFS). You must create a mount target (&#91;AWS::EFS::MountTarget&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-efs-mounttarget.html)) to mount your EFS file system on an EC2 or other AWS cloud compute resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.file_system" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying a KmsKeyId for an existing kms-key-long. If you don't specify a kms-key, then the default kms-key for EFS, ``&#x2F;aws&#x2F;elasticfilesystem``, is used to protect the encrypted file system.</td></tr>
<tr><td><CopyableCode code="file_system_tags" /></td><td><code>array</code></td><td>Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a ``"Key":"Name","Value":"&#123;value&#125;"`` key-value pair. Each key must be unique. For more information, see &#91;Tagging resources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws_tagging.html) in the *General Reference Guide*.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ID of the kms-key-long to be used to protect the encrypted file system. This parameter is only required if you want to use a nondefault kms-key. If this parameter is not specified, the default kms-key for EFS is used. This ID can be in one of the following formats:&lt;br&#x2F;&gt;  +  Key ID - A unique identifier of the key, for example ``1234abcd-12ab-34cd-56ef-1234567890ab``.&lt;br&#x2F;&gt;  +  ARN - An Amazon Resource Name (ARN) for the key, for example ``arn:aws:kms:us-west-2:111122223333:key&#x2F;1234abcd-12ab-34cd-56ef-1234567890ab``.&lt;br&#x2F;&gt;  +  Key alias - A previously created display name for a key, for example ``alias&#x2F;projectKey1``.&lt;br&#x2F;&gt;  +  Key alias ARN - An ARN for a key alias, for example ``arn:aws:kms:us-west-2:444455556666:alias&#x2F;projectKey1``.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If ``KmsKeyId`` is specified, the ``Encrypted`` parameter must be set to true.</td></tr>
<tr><td><CopyableCode code="lifecycle_policies" /></td><td><code>array</code></td><td>An array of ``LifecyclePolicy`` objects that define the file system's ``LifecycleConfiguration`` object. A ``LifecycleConfiguration`` object informs Lifecycle management of the following:&lt;br&#x2F;&gt;  +  When to move files in the file system from primary storage to IA storage.&lt;br&#x2F;&gt;  + When to move files in the file system from primary storage or IA storage to Archive storage.&lt;br&#x2F;&gt; +  When to move files that are in IA or Archive storage to primary storage.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  EFS requires that each ``LifecyclePolicy`` object have only a single transition. This means that in a request body, ``LifecyclePolicies`` needs to be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA``, ``TransitionToArchive`` ``TransitionToPrimaryStorageClass``. See the example requests in the following section for more information.</td></tr>
<tr><td><CopyableCode code="file_system_protection" /></td><td><code>object</code></td><td>Describes the protection on the file system.</td></tr>
<tr><td><CopyableCode code="performance_mode" /></td><td><code>string</code></td><td>The Performance mode of the file system. We recommend ``generalPurpose`` performance mode for all file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. The ``maxIO`` mode is not supported on One Zone file systems.&lt;br&#x2F;&gt;  Due to the higher per-operation latencies with Max I&#x2F;O, we recommend using General Purpose performance mode for all file systems.&lt;br&#x2F;&gt;  Default is ``generalPurpose``.</td></tr>
<tr><td><CopyableCode code="provisioned_throughput_in_mibps" /></td><td><code>number</code></td><td>The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if ``ThroughputMode`` is set to ``provisioned``. Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact SUP. For more information, see &#91;Amazon EFS quotas that you can increase&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;efs&#x2F;latest&#x2F;ug&#x2F;limits.html#soft-limits) in the *Amazon EFS User Guide*.</td></tr>
<tr><td><CopyableCode code="throughput_mode" /></td><td><code>string</code></td><td>Specifies the throughput mode for the file system. The mode can be ``bursting``, ``provisioned``, or ``elastic``. If you set ``ThroughputMode`` to ``provisioned``, you must also set a value for ``ProvisionedThroughputInMibps``. After you create the file system, you can decrease your file system's Provisioned throughput or change between the throughput modes, with certain time restrictions. For more information, see &#91;Specifying throughput with provisioned mode&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;efs&#x2F;latest&#x2F;ug&#x2F;performance.html#provisioned-throughput) in the *Amazon EFS User Guide*. &lt;br&#x2F;&gt; Default is ``bursting``.</td></tr>
<tr><td><CopyableCode code="file_system_policy" /></td><td><code>object</code></td><td>The ``FileSystemPolicy`` for the EFS file system. A file system policy is an IAM resource policy used to control NFS access to an EFS file system. For more information, see &#91;Using to control NFS access to Amazon EFS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;efs&#x2F;latest&#x2F;ug&#x2F;iam-access-control-nfs-efs.html) in the *Amazon EFS User Guide*.</td></tr>
<tr><td><CopyableCode code="bypass_policy_lockout_safety_check" /></td><td><code>boolean</code></td><td>(Optional) A boolean that specifies whether or not to bypass the ``FileSystemPolicy`` lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future ``PutFileSystemPolicy`` requests on this file system. Set ``BypassPolicyLockoutSafetyCheck`` to ``True`` only when you intend to prevent the IAM principal that is making the request from making subsequent ``PutFileSystemPolicy`` requests on this file system. The default value is ``False``.</td></tr>
<tr><td><CopyableCode code="backup_policy" /></td><td><code>object</code></td><td>Use the ``BackupPolicy`` to turn automatic backups on or off for the file system.</td></tr>
<tr><td><CopyableCode code="availability_zone_name" /></td><td><code>string</code></td><td>For One Zone file systems, specify the AWS Availability Zone in which to create the file system. Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone file systems, see &#91;EFS file system types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;efs&#x2F;latest&#x2F;ug&#x2F;availability-durability.html#file-system-type) in the *Amazon EFS User Guide*.&lt;br&#x2F;&gt;  One Zone file systems are not available in all Availability Zones in AWS-Regions where Amazon EFS is available.</td></tr>
<tr><td><CopyableCode code="replication_configuration" /></td><td><code>object</code></td><td>Describes the replication configuration for a specific file system.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
file_system_id,
arn,
encrypted,
file_system_tags,
kms_key_id,
lifecycle_policies,
file_system_protection,
performance_mode,
provisioned_throughput_in_mibps,
throughput_mode,
file_system_policy,
bypass_policy_lockout_safety_check,
backup_policy,
availability_zone_name,
replication_configuration
FROM aws.efs.file_system
WHERE data__Identifier = '<FileSystemId>';
```

## Permissions

To operate on the <code>file_system</code> resource, the following permissions are required:

### Read
```json
elasticfilesystem:DescribeBackupPolicy,
elasticfilesystem:DescribeFileSystemPolicy,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeLifecycleConfiguration,
elasticfilesystem:DescribeReplicationConfigurations
```

### Update
```json
elasticfilesystem:CreateReplicationConfiguration,
elasticfilesystem:DeleteFileSystemPolicy,
elasticfilesystem:DescribeBackupPolicy,
elasticfilesystem:DescribeFileSystemPolicy,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeLifecycleConfiguration,
elasticfilesystem:DescribeReplicationConfigurations,
elasticfilesystem:DeleteTags,
elasticfilesystem:DeleteReplicationConfiguration,
elasticfilesystem:ListTagsForResource,
elasticfilesystem:PutBackupPolicy,
elasticfilesystem:PutFileSystemPolicy,
elasticfilesystem:PutLifecycleConfiguration,
elasticfilesystem:TagResource,
elasticfilesystem:UntagResource,
elasticfilesystem:UpdateFileSystem,
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

