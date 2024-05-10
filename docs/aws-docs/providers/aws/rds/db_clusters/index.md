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

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ReadEndpoint": {
  "Address": "{{ Address }}"
 },
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AvailabilityZones": [
  "{{ AvailabilityZones[0] }}"
 ],
 "AutoMinorVersionUpgrade": "{{ AutoMinorVersionUpgrade }}",
 "BacktrackWindow": "{{ BacktrackWindow }}",
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "DatabaseName": "{{ DatabaseName }}",
 "DBClusterInstanceClass": "{{ DBClusterInstanceClass }}",
 "DBInstanceParameterGroupName": "{{ DBInstanceParameterGroupName }}",
 "DBSystemId": "{{ DBSystemId }}",
 "GlobalClusterIdentifier": "{{ GlobalClusterIdentifier }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterParameterGroupName": "{{ DBClusterParameterGroupName }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "Domain": "{{ Domain }}",
 "DomainIAMRoleName": "{{ DomainIAMRoleName }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EnableGlobalWriteForwarding": "{{ EnableGlobalWriteForwarding }}",
 "EnableHttpEndpoint": "{{ EnableHttpEndpoint }}",
 "EnableIAMDatabaseAuthentication": "{{ EnableIAMDatabaseAuthentication }}",
 "Engine": "{{ Engine }}",
 "EngineMode": "{{ EngineMode }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ManageMasterUserPassword": "{{ ManageMasterUserPassword }}",
 "Iops": "{{ Iops }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "MasterUsername": "{{ MasterUsername }}",
 "MasterUserPassword": "{{ MasterUserPassword }}",
 "MasterUserSecret": {
  "SecretArn": "{{ SecretArn }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "MonitoringInterval": "{{ MonitoringInterval }}",
 "MonitoringRoleArn": "{{ MonitoringRoleArn }}",
 "NetworkType": "{{ NetworkType }}",
 "PerformanceInsightsEnabled": "{{ PerformanceInsightsEnabled }}",
 "PerformanceInsightsKmsKeyId": "{{ PerformanceInsightsKmsKeyId }}",
 "PerformanceInsightsRetentionPeriod": "{{ PerformanceInsightsRetentionPeriod }}",
 "Port": "{{ Port }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "ReplicationSourceIdentifier": "{{ ReplicationSourceIdentifier }}",
 "RestoreToTime": "{{ RestoreToTime }}",
 "RestoreType": "{{ RestoreType }}",
 "ServerlessV2ScalingConfiguration": {
  "MinCapacity": null,
  "MaxCapacity": null
 },
 "ScalingConfiguration": {
  "AutoPause": "{{ AutoPause }}",
  "MaxCapacity": "{{ MaxCapacity }}",
  "MinCapacity": "{{ MinCapacity }}",
  "SecondsBeforeTimeout": "{{ SecondsBeforeTimeout }}",
  "SecondsUntilAutoPause": "{{ SecondsUntilAutoPause }}",
  "TimeoutAction": "{{ TimeoutAction }}"
 },
 "SnapshotIdentifier": "{{ SnapshotIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "SourceRegion": "{{ SourceRegion }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
 "StorageType": "{{ StorageType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "UseLatestRestorableTime": "{{ UseLatestRestorableTime }}",
 "VpcSecurityGroupIds": [
  "{{ VpcSecurityGroupIds[0] }}"
 ]
}
>>>
--required properties only
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
{{ ReadEndpoint }},
 {{ AllocatedStorage }},
 {{ AssociatedRoles }},
 {{ AvailabilityZones }},
 {{ AutoMinorVersionUpgrade }},
 {{ BacktrackWindow }},
 {{ BackupRetentionPeriod }},
 {{ CopyTagsToSnapshot }},
 {{ DatabaseName }},
 {{ DBClusterInstanceClass }},
 {{ DBInstanceParameterGroupName }},
 {{ DBSystemId }},
 {{ GlobalClusterIdentifier }},
 {{ DBClusterIdentifier }},
 {{ DBClusterParameterGroupName }},
 {{ DBSubnetGroupName }},
 {{ DeletionProtection }},
 {{ Domain }},
 {{ DomainIAMRoleName }},
 {{ EnableCloudwatchLogsExports }},
 {{ EnableGlobalWriteForwarding }},
 {{ EnableHttpEndpoint }},
 {{ EnableIAMDatabaseAuthentication }},
 {{ Engine }},
 {{ EngineMode }},
 {{ EngineVersion }},
 {{ ManageMasterUserPassword }},
 {{ Iops }},
 {{ KmsKeyId }},
 {{ MasterUsername }},
 {{ MasterUserPassword }},
 {{ MasterUserSecret }},
 {{ MonitoringInterval }},
 {{ MonitoringRoleArn }},
 {{ NetworkType }},
 {{ PerformanceInsightsEnabled }},
 {{ PerformanceInsightsKmsKeyId }},
 {{ PerformanceInsightsRetentionPeriod }},
 {{ Port }},
 {{ PreferredBackupWindow }},
 {{ PreferredMaintenanceWindow }},
 {{ PubliclyAccessible }},
 {{ ReplicationSourceIdentifier }},
 {{ RestoreToTime }},
 {{ RestoreType }},
 {{ ServerlessV2ScalingConfiguration }},
 {{ ScalingConfiguration }},
 {{ SnapshotIdentifier }},
 {{ SourceDBClusterIdentifier }},
 {{ SourceRegion }},
 {{ StorageEncrypted }},
 {{ StorageType }},
 {{ Tags }},
 {{ UseLatestRestorableTime }},
 {{ VpcSecurityGroupIds }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ReadEndpoint": {
  "Address": "{{ Address }}"
 },
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AvailabilityZones": [
  "{{ AvailabilityZones[0] }}"
 ],
 "AutoMinorVersionUpgrade": "{{ AutoMinorVersionUpgrade }}",
 "BacktrackWindow": "{{ BacktrackWindow }}",
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "DatabaseName": "{{ DatabaseName }}",
 "DBClusterInstanceClass": "{{ DBClusterInstanceClass }}",
 "DBInstanceParameterGroupName": "{{ DBInstanceParameterGroupName }}",
 "DBSystemId": "{{ DBSystemId }}",
 "GlobalClusterIdentifier": "{{ GlobalClusterIdentifier }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterParameterGroupName": "{{ DBClusterParameterGroupName }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "Domain": "{{ Domain }}",
 "DomainIAMRoleName": "{{ DomainIAMRoleName }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EnableGlobalWriteForwarding": "{{ EnableGlobalWriteForwarding }}",
 "EnableHttpEndpoint": "{{ EnableHttpEndpoint }}",
 "EnableIAMDatabaseAuthentication": "{{ EnableIAMDatabaseAuthentication }}",
 "Engine": "{{ Engine }}",
 "EngineMode": "{{ EngineMode }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ManageMasterUserPassword": "{{ ManageMasterUserPassword }}",
 "Iops": "{{ Iops }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "MasterUsername": "{{ MasterUsername }}",
 "MasterUserPassword": "{{ MasterUserPassword }}",
 "MasterUserSecret": {
  "SecretArn": "{{ SecretArn }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "MonitoringInterval": "{{ MonitoringInterval }}",
 "MonitoringRoleArn": "{{ MonitoringRoleArn }}",
 "NetworkType": "{{ NetworkType }}",
 "PerformanceInsightsEnabled": "{{ PerformanceInsightsEnabled }}",
 "PerformanceInsightsKmsKeyId": "{{ PerformanceInsightsKmsKeyId }}",
 "PerformanceInsightsRetentionPeriod": "{{ PerformanceInsightsRetentionPeriod }}",
 "Port": "{{ Port }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "ReplicationSourceIdentifier": "{{ ReplicationSourceIdentifier }}",
 "RestoreToTime": "{{ RestoreToTime }}",
 "RestoreType": "{{ RestoreType }}",
 "ServerlessV2ScalingConfiguration": {
  "MinCapacity": null,
  "MaxCapacity": null
 },
 "ScalingConfiguration": {
  "AutoPause": "{{ AutoPause }}",
  "MaxCapacity": "{{ MaxCapacity }}",
  "MinCapacity": "{{ MinCapacity }}",
  "SecondsBeforeTimeout": "{{ SecondsBeforeTimeout }}",
  "SecondsUntilAutoPause": "{{ SecondsUntilAutoPause }}",
  "TimeoutAction": "{{ TimeoutAction }}"
 },
 "SnapshotIdentifier": "{{ SnapshotIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "SourceRegion": "{{ SourceRegion }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
 "StorageType": "{{ StorageType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "UseLatestRestorableTime": "{{ UseLatestRestorableTime }}",
 "VpcSecurityGroupIds": [
  "{{ VpcSecurityGroupIds[0] }}"
 ]
}
>>>
--all properties
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
 {{ ReadEndpoint }},
 {{ AllocatedStorage }},
 {{ AssociatedRoles }},
 {{ AvailabilityZones }},
 {{ AutoMinorVersionUpgrade }},
 {{ BacktrackWindow }},
 {{ BackupRetentionPeriod }},
 {{ CopyTagsToSnapshot }},
 {{ DatabaseName }},
 {{ DBClusterInstanceClass }},
 {{ DBInstanceParameterGroupName }},
 {{ DBSystemId }},
 {{ GlobalClusterIdentifier }},
 {{ DBClusterIdentifier }},
 {{ DBClusterParameterGroupName }},
 {{ DBSubnetGroupName }},
 {{ DeletionProtection }},
 {{ Domain }},
 {{ DomainIAMRoleName }},
 {{ EnableCloudwatchLogsExports }},
 {{ EnableGlobalWriteForwarding }},
 {{ EnableHttpEndpoint }},
 {{ EnableIAMDatabaseAuthentication }},
 {{ Engine }},
 {{ EngineMode }},
 {{ EngineVersion }},
 {{ ManageMasterUserPassword }},
 {{ Iops }},
 {{ KmsKeyId }},
 {{ MasterUsername }},
 {{ MasterUserPassword }},
 {{ MasterUserSecret }},
 {{ MonitoringInterval }},
 {{ MonitoringRoleArn }},
 {{ NetworkType }},
 {{ PerformanceInsightsEnabled }},
 {{ PerformanceInsightsKmsKeyId }},
 {{ PerformanceInsightsRetentionPeriod }},
 {{ Port }},
 {{ PreferredBackupWindow }},
 {{ PreferredMaintenanceWindow }},
 {{ PubliclyAccessible }},
 {{ ReplicationSourceIdentifier }},
 {{ RestoreToTime }},
 {{ RestoreType }},
 {{ ServerlessV2ScalingConfiguration }},
 {{ ScalingConfiguration }},
 {{ SnapshotIdentifier }},
 {{ SourceDBClusterIdentifier }},
 {{ SourceRegion }},
 {{ StorageEncrypted }},
 {{ StorageType }},
 {{ Tags }},
 {{ UseLatestRestorableTime }},
 {{ VpcSecurityGroupIds }},
 'us-east-1';
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

