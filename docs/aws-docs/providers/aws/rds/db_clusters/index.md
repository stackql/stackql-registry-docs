---
title: db_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters
  - rds
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


Used to retrieve a list of <code>db_clusters</code> in a region or to create or delete a <code>db_clusters</code> resource, use <code>db_cluster</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.</td></tr>
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
db_cluster_identifier
FROM aws.rds.db_clusters
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>db_cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- db_cluster.iql (required properties only)
INSERT INTO aws.rds.db_clusters (
 ReadEndpoint,
 AllocatedStorage,
 AssociatedRoles,
 AvailabilityZones,
 AutoMinorVersionUpgrade,
 BacktrackWindow,
 BackupRetentionPeriod,
 CopyTagsToSnapshot,
 DatabaseName,
 DBClusterInstanceClass,
 DBInstanceParameterGroupName,
 DBSystemId,
 GlobalClusterIdentifier,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBSubnetGroupName,
 DeletionProtection,
 Domain,
 DomainIAMRoleName,
 EnableCloudwatchLogsExports,
 EnableGlobalWriteForwarding,
 EnableHttpEndpoint,
 EnableIAMDatabaseAuthentication,
 Engine,
 EngineMode,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MonitoringInterval,
 MonitoringRoleArn,
 NetworkType,
 PerformanceInsightsEnabled,
 PerformanceInsightsKmsKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 ReplicationSourceIdentifier,
 RestoreToTime,
 RestoreType,
 ServerlessV2ScalingConfiguration,
 ScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
'{{ ReadEndpoint }}',
 '{{ AllocatedStorage }}',
 '{{ AssociatedRoles }}',
 '{{ AvailabilityZones }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ BacktrackWindow }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DatabaseName }}',
 '{{ DBClusterInstanceClass }}',
 '{{ DBInstanceParameterGroupName }}',
 '{{ DBSystemId }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterParameterGroupName }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainIAMRoleName }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableGlobalWriteForwarding }}',
 '{{ EnableHttpEndpoint }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ Engine }}',
 '{{ EngineMode }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ NetworkType }}',
 '{{ PerformanceInsightsEnabled }}',
 '{{ PerformanceInsightsKmsKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicationSourceIdentifier }}',
 '{{ RestoreToTime }}',
 '{{ RestoreType }}',
 '{{ ServerlessV2ScalingConfiguration }}',
 '{{ ScalingConfiguration }}',
 '{{ SnapshotIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ Tags }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VpcSecurityGroupIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- db_cluster.iql (all properties)
INSERT INTO aws.rds.db_clusters (
 ReadEndpoint,
 AllocatedStorage,
 AssociatedRoles,
 AvailabilityZones,
 AutoMinorVersionUpgrade,
 BacktrackWindow,
 BackupRetentionPeriod,
 CopyTagsToSnapshot,
 DatabaseName,
 DBClusterInstanceClass,
 DBInstanceParameterGroupName,
 DBSystemId,
 GlobalClusterIdentifier,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBSubnetGroupName,
 DeletionProtection,
 Domain,
 DomainIAMRoleName,
 EnableCloudwatchLogsExports,
 EnableGlobalWriteForwarding,
 EnableHttpEndpoint,
 EnableIAMDatabaseAuthentication,
 Engine,
 EngineMode,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MonitoringInterval,
 MonitoringRoleArn,
 NetworkType,
 PerformanceInsightsEnabled,
 PerformanceInsightsKmsKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 ReplicationSourceIdentifier,
 RestoreToTime,
 RestoreType,
 ServerlessV2ScalingConfiguration,
 ScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
 '{{ ReadEndpoint }}',
 '{{ AllocatedStorage }}',
 '{{ AssociatedRoles }}',
 '{{ AvailabilityZones }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ BacktrackWindow }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DatabaseName }}',
 '{{ DBClusterInstanceClass }}',
 '{{ DBInstanceParameterGroupName }}',
 '{{ DBSystemId }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterParameterGroupName }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainIAMRoleName }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableGlobalWriteForwarding }}',
 '{{ EnableHttpEndpoint }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ Engine }}',
 '{{ EngineMode }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ NetworkType }}',
 '{{ PerformanceInsightsEnabled }}',
 '{{ PerformanceInsightsKmsKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicationSourceIdentifier }}',
 '{{ RestoreToTime }}',
 '{{ RestoreType }}',
 '{{ ServerlessV2ScalingConfiguration }}',
 '{{ ScalingConfiguration }}',
 '{{ SnapshotIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ Tags }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VpcSecurityGroupIds }}',
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
  - name: db_cluster
    props:
      - name: ReadEndpoint
        value:
          Address: '{{ Address }}'
      - name: AllocatedStorage
        value: '{{ AllocatedStorage }}'
      - name: AssociatedRoles
        value:
          - FeatureName: '{{ FeatureName }}'
            RoleArn: '{{ RoleArn }}'
      - name: AvailabilityZones
        value:
          - '{{ AvailabilityZones[0] }}'
      - name: AutoMinorVersionUpgrade
        value: '{{ AutoMinorVersionUpgrade }}'
      - name: BacktrackWindow
        value: '{{ BacktrackWindow }}'
      - name: BackupRetentionPeriod
        value: '{{ BackupRetentionPeriod }}'
      - name: CopyTagsToSnapshot
        value: '{{ CopyTagsToSnapshot }}'
      - name: DatabaseName
        value: '{{ DatabaseName }}'
      - name: DBClusterInstanceClass
        value: '{{ DBClusterInstanceClass }}'
      - name: DBInstanceParameterGroupName
        value: '{{ DBInstanceParameterGroupName }}'
      - name: DBSystemId
        value: '{{ DBSystemId }}'
      - name: GlobalClusterIdentifier
        value: '{{ GlobalClusterIdentifier }}'
      - name: DBClusterIdentifier
        value: '{{ DBClusterIdentifier }}'
      - name: DBClusterParameterGroupName
        value: '{{ DBClusterParameterGroupName }}'
      - name: DBSubnetGroupName
        value: '{{ DBSubnetGroupName }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: DomainIAMRoleName
        value: '{{ DomainIAMRoleName }}'
      - name: EnableCloudwatchLogsExports
        value:
          - '{{ EnableCloudwatchLogsExports[0] }}'
      - name: EnableGlobalWriteForwarding
        value: '{{ EnableGlobalWriteForwarding }}'
      - name: EnableHttpEndpoint
        value: '{{ EnableHttpEndpoint }}'
      - name: EnableIAMDatabaseAuthentication
        value: '{{ EnableIAMDatabaseAuthentication }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: EngineMode
        value: '{{ EngineMode }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: ManageMasterUserPassword
        value: '{{ ManageMasterUserPassword }}'
      - name: Iops
        value: '{{ Iops }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: MasterUserSecret
        value:
          SecretArn: '{{ SecretArn }}'
          KmsKeyId: '{{ KmsKeyId }}'
      - name: MonitoringInterval
        value: '{{ MonitoringInterval }}'
      - name: MonitoringRoleArn
        value: '{{ MonitoringRoleArn }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
      - name: PerformanceInsightsEnabled
        value: '{{ PerformanceInsightsEnabled }}'
      - name: PerformanceInsightsKmsKeyId
        value: '{{ PerformanceInsightsKmsKeyId }}'
      - name: PerformanceInsightsRetentionPeriod
        value: '{{ PerformanceInsightsRetentionPeriod }}'
      - name: Port
        value: '{{ Port }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: ReplicationSourceIdentifier
        value: '{{ ReplicationSourceIdentifier }}'
      - name: RestoreToTime
        value: '{{ RestoreToTime }}'
      - name: RestoreType
        value: '{{ RestoreType }}'
      - name: ServerlessV2ScalingConfiguration
        value:
          MinCapacity: null
          MaxCapacity: null
      - name: ScalingConfiguration
        value:
          AutoPause: '{{ AutoPause }}'
          MaxCapacity: '{{ MaxCapacity }}'
          MinCapacity: '{{ MinCapacity }}'
          SecondsBeforeTimeout: '{{ SecondsBeforeTimeout }}'
          SecondsUntilAutoPause: '{{ SecondsUntilAutoPause }}'
          TimeoutAction: '{{ TimeoutAction }}'
      - name: SnapshotIdentifier
        value: '{{ SnapshotIdentifier }}'
      - name: SourceDBClusterIdentifier
        value: '{{ SourceDBClusterIdentifier }}'
      - name: SourceRegion
        value: '{{ SourceRegion }}'
      - name: StorageEncrypted
        value: '{{ StorageEncrypted }}'
      - name: StorageType
        value: '{{ StorageType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UseLatestRestorableTime
        value: '{{ UseLatestRestorableTime }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.db_clusters
WHERE data__Identifier = '<DBClusterIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_clusters</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:PassRole,
rds:AddRoleToDBCluster,
rds:AddTagsToResource,
rds:CreateDBCluster,
rds:CreateDBInstance,
rds:DescribeDBClusters,
rds:DescribeEvents,
rds:EnableHttpEndpoint,
rds:ModifyDBCluster,
rds:RestoreDBClusterFromSnapshot,
rds:RestoreDBClusterToPointInTime,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### Delete
```json
rds:CreateDBClusterSnapshot,
rds:DeleteDBCluster,
rds:DeleteDBInstance,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters,
rds:RemoveFromGlobalCluster
```

### List
```json
rds:DescribeDBClusters
```

