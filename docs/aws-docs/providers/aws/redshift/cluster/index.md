---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - redshift
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


Gets or updates an individual <code>cluster</code> resource, use <code>clusters</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.cluster" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><CopyableCode code="cluster_namespace_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster namespace.</td></tr>
<tr><td><CopyableCode code="master_username" /></td><td><code>string</code></td><td>The user name associated with the master user account for the cluster that is being created. The user name can't be PUBLIC and first character must be a letter.</td></tr>
<tr><td><CopyableCode code="master_user_password" /></td><td><code>string</code></td><td>The password associated with the master user account for the cluster that is being created. You can't use MasterUserPassword if ManageMasterPassword is true. Password must be between 8 and 64 characters in length, should have at least one uppercase letter.Must contain at least one lowercase letter.Must contain one number.Can be any printable ASCII character.</td></tr>
<tr><td><CopyableCode code="node_type" /></td><td><code>string</code></td><td>The node type to be provisioned for the cluster.Valid Values: ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge | dc2.large | dc2.8xlarge | ra3.4xlarge | ra3.16xlarge</td></tr>
<tr><td><CopyableCode code="allow_version_upgrade" /></td><td><code>boolean</code></td><td>Major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default value is True</td></tr>
<tr><td><CopyableCode code="automated_snapshot_retention_period" /></td><td><code>integer</code></td><td>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Default value is 1</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint</td></tr>
<tr><td><CopyableCode code="cluster_parameter_group_name" /></td><td><code>string</code></td><td>The name of the parameter group to be associated with this cluster.</td></tr>
<tr><td><CopyableCode code="cluster_type" /></td><td><code>string</code></td><td>The type of the cluster. When cluster type is specified as single-node, the NumberOfNodes parameter is not required and if multi-node, the NumberOfNodes parameter is required</td></tr>
<tr><td><CopyableCode code="cluster_version" /></td><td><code>string</code></td><td>The version of the Amazon Redshift engine software that you want to deploy on the cluster.The version selected runs on all the nodes in the cluster.</td></tr>
<tr><td><CopyableCode code="cluster_subnet_group_name" /></td><td><code>string</code></td><td>The name of a cluster subnet group to be associated with this cluster.</td></tr>
<tr><td><CopyableCode code="db_name" /></td><td><code>string</code></td><td>The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database.</td></tr>
<tr><td><CopyableCode code="elastic_ip" /></td><td><code>string</code></td><td>The Elastic IP (EIP) address for the cluster.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>If true, the data in the cluster is encrypted at rest.</td></tr>
<tr><td><CopyableCode code="hsm_client_certificate_identifier" /></td><td><code>string</code></td><td>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM</td></tr>
<tr><td><CopyableCode code="hsm_configuration_identifier" /></td><td><code>string</code></td><td>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</td></tr>
<tr><td><CopyableCode code="number_of_nodes" /></td><td><code>integer</code></td><td>The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings</td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>The weekly time range (in UTC) during which automated cluster maintenance can occur.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>If true, the cluster can be accessed from a public network.</td></tr>
<tr><td><CopyableCode code="cluster_security_groups" /></td><td><code>array</code></td><td>A list of security groups to be associated with this cluster.</td></tr>
<tr><td><CopyableCode code="iam_roles" /></td><td><code>array</code></td><td>A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 50 IAM roles in a single request</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</td></tr>
<tr><td><CopyableCode code="snapshot_cluster_identifier" /></td><td><code>string</code></td><td>The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</td></tr>
<tr><td><CopyableCode code="snapshot_identifier" /></td><td><code>string</code></td><td>The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.</td></tr>
<tr><td><CopyableCode code="owner_account" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_region" /></td><td><code>string</code></td><td>The destination AWS Region that you want to copy snapshots to. Constraints: Must be the name of a valid AWS Region. For more information, see Regions and Endpoints in the Amazon Web Services &#91;https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;rande.html#redshift_region&#93; General Reference</td></tr>
<tr><td><CopyableCode code="snapshot_copy_retention_period" /></td><td><code>integer</code></td><td>The number of days to retain automated snapshots in the destination region after they are copied from the source region. &lt;br&#x2F;&gt;&lt;br&#x2F;&gt; Default is 7. &lt;br&#x2F;&gt;&lt;br&#x2F;&gt; Constraints: Must be at least 1 and no more than 35.</td></tr>
<tr><td><CopyableCode code="snapshot_copy_grant_name" /></td><td><code>string</code></td><td>The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.</td></tr>
<tr><td><CopyableCode code="manual_snapshot_retention_period" /></td><td><code>integer</code></td><td>The number of days to retain newly copied snapshots in the destination AWS Region after they are copied from the source AWS Region. If the value is -1, the manual snapshot is retained indefinitely.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The value must be either -1 or an integer between 1 and 3,653.</td></tr>
<tr><td><CopyableCode code="snapshot_copy_manual" /></td><td><code>boolean</code></td><td>Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.</td></tr>
<tr><td><CopyableCode code="availability_zone_relocation" /></td><td><code>boolean</code></td><td>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.</td></tr>
<tr><td><CopyableCode code="availability_zone_relocation_status" /></td><td><code>string</code></td><td>The availability zone relocation status of the cluster</td></tr>
<tr><td><CopyableCode code="aqua_configuration_status" /></td><td><code>string</code></td><td>The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) after the cluster is restored. Possible values include the following.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;enabled - Use AQUA if it is available for the current Region and Amazon Redshift node type.&lt;br&#x2F;&gt;disabled - Don't use AQUA.&lt;br&#x2F;&gt;auto - Amazon Redshift determines whether to use AQUA.&lt;br&#x2F;&gt;</td></tr>
<tr><td><CopyableCode code="classic" /></td><td><code>boolean</code></td><td>A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to false , the resize type is elastic.</td></tr>
<tr><td><CopyableCode code="enhanced_vpc_routing" /></td><td><code>boolean</code></td><td>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If this option is true , enhanced VPC routing is enabled.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Default: false</td></tr>
<tr><td><CopyableCode code="maintenance_track_name" /></td><td><code>string</code></td><td>The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the PendingModifiedValues for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.</td></tr>
<tr><td><CopyableCode code="defer_maintenance" /></td><td><code>boolean</code></td><td>A boolean indicating whether to enable the deferred maintenance window.</td></tr>
<tr><td><CopyableCode code="defer_maintenance_identifier" /></td><td><code>string</code></td><td>A unique identifier for the deferred maintenance window.</td></tr>
<tr><td><CopyableCode code="defer_maintenance_start_time" /></td><td><code>string</code></td><td>A timestamp indicating the start time for the deferred maintenance window.</td></tr>
<tr><td><CopyableCode code="defer_maintenance_end_time" /></td><td><code>string</code></td><td>A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can't specify a duration.</td></tr>
<tr><td><CopyableCode code="defer_maintenance_duration" /></td><td><code>integer</code></td><td>An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 45 days or less.</td></tr>
<tr><td><CopyableCode code="revision_target" /></td><td><code>string</code></td><td>The identifier of the database revision. You can retrieve this value from the response to the DescribeClusterDbRevisions request.</td></tr>
<tr><td><CopyableCode code="resource_action" /></td><td><code>string</code></td><td>The Redshift operation to be performed. Resource Action supports pause-cluster, resume-cluster, failover-primary-compute APIs</td></tr>
<tr><td><CopyableCode code="rotate_encryption_key" /></td><td><code>boolean</code></td><td>A boolean indicating if we want to rotate Encryption Keys.</td></tr>
<tr><td><CopyableCode code="multi_az" /></td><td><code>boolean</code></td><td>A boolean indicating if the redshift cluster is multi-az or not. If you don't provide this parameter or set the value to false, the redshift cluster will be single-az.</td></tr>
<tr><td><CopyableCode code="namespace_resource_policy" /></td><td><code>object</code></td><td>The namespace resource policy document that will be attached to a Redshift cluster.</td></tr>
<tr><td><CopyableCode code="manage_master_password" /></td><td><code>boolean</code></td><td>A boolean indicating if the redshift cluster's admin user credentials is managed by Redshift or not. You can't use MasterUserPassword if ManageMasterPassword is true. If ManageMasterPassword is false or not set, Amazon Redshift uses MasterUserPassword for the admin user account's password.</td></tr>
<tr><td><CopyableCode code="master_password_secret_kms_key_id" /></td><td><code>string</code></td><td>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin user credentials secret.</td></tr>
<tr><td><CopyableCode code="master_password_secret_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the cluster's admin user credentials secret.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cluster_identifier,
cluster_namespace_arn,
master_username,
master_user_password,
node_type,
allow_version_upgrade,
automated_snapshot_retention_period,
availability_zone,
cluster_parameter_group_name,
cluster_type,
cluster_version,
cluster_subnet_group_name,
db_name,
elastic_ip,
encrypted,
hsm_client_certificate_identifier,
hsm_configuration_identifier,
kms_key_id,
number_of_nodes,
port,
preferred_maintenance_window,
publicly_accessible,
cluster_security_groups,
iam_roles,
tags,
vpc_security_group_ids,
snapshot_cluster_identifier,
snapshot_identifier,
owner_account,
logging_properties,
endpoint,
destination_region,
snapshot_copy_retention_period,
snapshot_copy_grant_name,
manual_snapshot_retention_period,
snapshot_copy_manual,
availability_zone_relocation,
availability_zone_relocation_status,
aqua_configuration_status,
classic,
enhanced_vpc_routing,
maintenance_track_name,
defer_maintenance,
defer_maintenance_identifier,
defer_maintenance_start_time,
defer_maintenance_end_time,
defer_maintenance_duration,
revision_target,
resource_action,
rotate_encryption_key,
multi_az,
namespace_resource_policy,
manage_master_password,
master_password_secret_kms_key_id,
master_password_secret_arn
FROM aws.redshift.cluster
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterIdentifier>';
```


## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeClusters,
redshift:DescribeLoggingStatus,
redshift:DescribeSnapshotCopyGrant,
redshift:DescribeClusterDbRevisions,
redshift:DescribeTags,
redshift:GetResourcePolicy
```

### Update
```json
iam:PassRole,
redshift:DescribeClusters,
redshift:ModifyCluster,
redshift:ModifyClusterIamRoles,
redshift:EnableLogging,
redshift:CreateTags,
redshift:DeleteTags,
redshift:DescribeTags,
redshift:DisableLogging,
redshift:DescribeLoggingStatus,
redshift:RebootCluster,
redshift:EnableSnapshotCopy,
redshift:DisableSnapshotCopy,
redshift:ModifySnapshotCopyRetentionPeriod,
redshift:ModifyAquaConfiguration,
redshift:ResizeCluster,
redshift:ModifyClusterMaintenance,
redshift:DescribeClusterDbRevisions,
redshift:ModifyClusterDbRevisions,
redshift:PauseCluster,
redshift:ResumeCluster,
redshift:RotateEncryptionKey,
redshift:FailoverPrimaryCompute,
redshift:PutResourcePolicy,
redshift:GetResourcePolicy,
redshift:DeleteResourcePolicy,
cloudwatch:PutMetricData
```

