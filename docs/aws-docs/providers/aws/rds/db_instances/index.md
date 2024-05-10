---
title: db_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - db_instances
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


Used to retrieve a list of <code>db_instances</code> in a region or to create or delete a <code>db_instances</code> resource, use <code>db_instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::RDS::DBInstance`` resource creates an Amazon DB instance. The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster.&lt;br&#x2F;&gt; For more information about creating an RDS DB instance, see &#91;Creating an Amazon RDS DB instance&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt; For more information about creating a DB instance in an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;AuroraUserGuide&#x2F;Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.&lt;br&#x2F;&gt; If you import an existing DB instance, and the template configuration doesn't match the actual configuration of the DB instance, AWS CloudFormation applies the changes in the template during the import operation.&lt;br&#x2F;&gt;  If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_instance_identifier" /></td><td><code>string</code></td><td>A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; For information about constraints that apply to DB instance identifiers, see &#91;Naming constraints in Amazon RDS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
db_instance_identifier
FROM aws.rds.db_instances
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
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "AllowMajorVersionUpgrade": "{{ AllowMajorVersionUpgrade }}",
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AutoMinorVersionUpgrade": "{{ AutoMinorVersionUpgrade }}",
 "AutomaticBackupReplicationRegion": "{{ AutomaticBackupReplicationRegion }}",
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CACertificateIdentifier": "{{ CACertificateIdentifier }}",
 "CertificateDetails": {
  "CAIdentifier": "{{ CAIdentifier }}",
  "ValidTill": "{{ ValidTill }}"
 },
 "CertificateRotationRestart": "{{ CertificateRotationRestart }}",
 "CharacterSetName": "{{ CharacterSetName }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "CustomIAMInstanceProfile": "{{ CustomIAMInstanceProfile }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterSnapshotIdentifier": "{{ DBClusterSnapshotIdentifier }}",
 "DBInstanceClass": "{{ DBInstanceClass }}",
 "DBInstanceIdentifier": "{{ DBInstanceIdentifier }}",
 "DBName": "{{ DBName }}",
 "DBParameterGroupName": "{{ DBParameterGroupName }}",
 "DBSecurityGroups": [
  "{{ DBSecurityGroups[0] }}"
 ],
 "DBSnapshotIdentifier": "{{ DBSnapshotIdentifier }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DedicatedLogVolume": "{{ DedicatedLogVolume }}",
 "DeleteAutomatedBackups": "{{ DeleteAutomatedBackups }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "Domain": "{{ Domain }}",
 "DomainAuthSecretArn": "{{ DomainAuthSecretArn }}",
 "DomainDnsIps": [
  "{{ DomainDnsIps[0] }}"
 ],
 "DomainFqdn": "{{ DomainFqdn }}",
 "DomainIAMRoleName": "{{ DomainIAMRoleName }}",
 "DomainOu": "{{ DomainOu }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EnableIAMDatabaseAuthentication": "{{ EnableIAMDatabaseAuthentication }}",
 "EnablePerformanceInsights": "{{ EnablePerformanceInsights }}",
 "Endpoint": {
  "Address": "{{ Address }}",
  "Port": "{{ Port }}",
  "HostedZoneId": "{{ HostedZoneId }}"
 },
 "Engine": "{{ Engine }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ManageMasterUserPassword": "{{ ManageMasterUserPassword }}",
 "Iops": "{{ Iops }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "LicenseModel": "{{ LicenseModel }}",
 "MasterUsername": "{{ MasterUsername }}",
 "MasterUserPassword": "{{ MasterUserPassword }}",
 "MasterUserSecret": {
  "SecretArn": "{{ SecretArn }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "MaxAllocatedStorage": "{{ MaxAllocatedStorage }}",
 "MonitoringInterval": "{{ MonitoringInterval }}",
 "MonitoringRoleArn": "{{ MonitoringRoleArn }}",
 "MultiAZ": "{{ MultiAZ }}",
 "NcharCharacterSetName": "{{ NcharCharacterSetName }}",
 "NetworkType": "{{ NetworkType }}",
 "OptionGroupName": "{{ OptionGroupName }}",
 "PerformanceInsightsKMSKeyId": "{{ PerformanceInsightsKMSKeyId }}",
 "PerformanceInsightsRetentionPeriod": "{{ PerformanceInsightsRetentionPeriod }}",
 "Port": "{{ Port }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "ProcessorFeatures": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}"
  }
 ],
 "PromotionTier": "{{ PromotionTier }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "ReplicaMode": "{{ ReplicaMode }}",
 "RestoreTime": "{{ RestoreTime }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "SourceDbiResourceId": "{{ SourceDbiResourceId }}",
 "SourceDBInstanceAutomatedBackupsArn": "{{ SourceDBInstanceAutomatedBackupsArn }}",
 "SourceDBInstanceIdentifier": "{{ SourceDBInstanceIdentifier }}",
 "SourceRegion": "{{ SourceRegion }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
 "StorageType": "{{ StorageType }}",
 "StorageThroughput": "{{ StorageThroughput }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TdeCredentialArn": "{{ TdeCredentialArn }}",
 "TdeCredentialPassword": "{{ TdeCredentialPassword }}",
 "Timezone": "{{ Timezone }}",
 "UseDefaultProcessorFeatures": "{{ UseDefaultProcessorFeatures }}",
 "UseLatestRestorableTime": "{{ UseLatestRestorableTime }}",
 "VPCSecurityGroups": [
  "{{ VPCSecurityGroups[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.rds.db_instances (
 AllocatedStorage,
 AllowMajorVersionUpgrade,
 AssociatedRoles,
 AutoMinorVersionUpgrade,
 AutomaticBackupReplicationRegion,
 AvailabilityZone,
 BackupRetentionPeriod,
 CACertificateIdentifier,
 CertificateDetails,
 CertificateRotationRestart,
 CharacterSetName,
 CopyTagsToSnapshot,
 CustomIAMInstanceProfile,
 DBClusterIdentifier,
 DBClusterSnapshotIdentifier,
 DBInstanceClass,
 DBInstanceIdentifier,
 DBName,
 DBParameterGroupName,
 DBSecurityGroups,
 DBSnapshotIdentifier,
 DBSubnetGroupName,
 DedicatedLogVolume,
 DeleteAutomatedBackups,
 DeletionProtection,
 Domain,
 DomainAuthSecretArn,
 DomainDnsIps,
 DomainFqdn,
 DomainIAMRoleName,
 DomainOu,
 EnableCloudwatchLogsExports,
 EnableIAMDatabaseAuthentication,
 EnablePerformanceInsights,
 Endpoint,
 Engine,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 LicenseModel,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MaxAllocatedStorage,
 MonitoringInterval,
 MonitoringRoleArn,
 MultiAZ,
 NcharCharacterSetName,
 NetworkType,
 OptionGroupName,
 PerformanceInsightsKMSKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 ProcessorFeatures,
 PromotionTier,
 PubliclyAccessible,
 ReplicaMode,
 RestoreTime,
 SourceDBClusterIdentifier,
 SourceDbiResourceId,
 SourceDBInstanceAutomatedBackupsArn,
 SourceDBInstanceIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 StorageThroughput,
 Tags,
 TdeCredentialArn,
 TdeCredentialPassword,
 Timezone,
 UseDefaultProcessorFeatures,
 UseLatestRestorableTime,
 VPCSecurityGroups,
 region
)
SELECT 
{{ AllocatedStorage }},
 {{ AllowMajorVersionUpgrade }},
 {{ AssociatedRoles }},
 {{ AutoMinorVersionUpgrade }},
 {{ AutomaticBackupReplicationRegion }},
 {{ AvailabilityZone }},
 {{ BackupRetentionPeriod }},
 {{ CACertificateIdentifier }},
 {{ CertificateDetails }},
 {{ CertificateRotationRestart }},
 {{ CharacterSetName }},
 {{ CopyTagsToSnapshot }},
 {{ CustomIAMInstanceProfile }},
 {{ DBClusterIdentifier }},
 {{ DBClusterSnapshotIdentifier }},
 {{ DBInstanceClass }},
 {{ DBInstanceIdentifier }},
 {{ DBName }},
 {{ DBParameterGroupName }},
 {{ DBSecurityGroups }},
 {{ DBSnapshotIdentifier }},
 {{ DBSubnetGroupName }},
 {{ DedicatedLogVolume }},
 {{ DeleteAutomatedBackups }},
 {{ DeletionProtection }},
 {{ Domain }},
 {{ DomainAuthSecretArn }},
 {{ DomainDnsIps }},
 {{ DomainFqdn }},
 {{ DomainIAMRoleName }},
 {{ DomainOu }},
 {{ EnableCloudwatchLogsExports }},
 {{ EnableIAMDatabaseAuthentication }},
 {{ EnablePerformanceInsights }},
 {{ Endpoint }},
 {{ Engine }},
 {{ EngineVersion }},
 {{ ManageMasterUserPassword }},
 {{ Iops }},
 {{ KmsKeyId }},
 {{ LicenseModel }},
 {{ MasterUsername }},
 {{ MasterUserPassword }},
 {{ MasterUserSecret }},
 {{ MaxAllocatedStorage }},
 {{ MonitoringInterval }},
 {{ MonitoringRoleArn }},
 {{ MultiAZ }},
 {{ NcharCharacterSetName }},
 {{ NetworkType }},
 {{ OptionGroupName }},
 {{ PerformanceInsightsKMSKeyId }},
 {{ PerformanceInsightsRetentionPeriod }},
 {{ Port }},
 {{ PreferredBackupWindow }},
 {{ PreferredMaintenanceWindow }},
 {{ ProcessorFeatures }},
 {{ PromotionTier }},
 {{ PubliclyAccessible }},
 {{ ReplicaMode }},
 {{ RestoreTime }},
 {{ SourceDBClusterIdentifier }},
 {{ SourceDbiResourceId }},
 {{ SourceDBInstanceAutomatedBackupsArn }},
 {{ SourceDBInstanceIdentifier }},
 {{ SourceRegion }},
 {{ StorageEncrypted }},
 {{ StorageType }},
 {{ StorageThroughput }},
 {{ Tags }},
 {{ TdeCredentialArn }},
 {{ TdeCredentialPassword }},
 {{ Timezone }},
 {{ UseDefaultProcessorFeatures }},
 {{ UseLatestRestorableTime }},
 {{ VPCSecurityGroups }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "AllowMajorVersionUpgrade": "{{ AllowMajorVersionUpgrade }}",
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AutoMinorVersionUpgrade": "{{ AutoMinorVersionUpgrade }}",
 "AutomaticBackupReplicationRegion": "{{ AutomaticBackupReplicationRegion }}",
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CACertificateIdentifier": "{{ CACertificateIdentifier }}",
 "CertificateDetails": {
  "CAIdentifier": "{{ CAIdentifier }}",
  "ValidTill": "{{ ValidTill }}"
 },
 "CertificateRotationRestart": "{{ CertificateRotationRestart }}",
 "CharacterSetName": "{{ CharacterSetName }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "CustomIAMInstanceProfile": "{{ CustomIAMInstanceProfile }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterSnapshotIdentifier": "{{ DBClusterSnapshotIdentifier }}",
 "DBInstanceClass": "{{ DBInstanceClass }}",
 "DBInstanceIdentifier": "{{ DBInstanceIdentifier }}",
 "DBName": "{{ DBName }}",
 "DBParameterGroupName": "{{ DBParameterGroupName }}",
 "DBSecurityGroups": [
  "{{ DBSecurityGroups[0] }}"
 ],
 "DBSnapshotIdentifier": "{{ DBSnapshotIdentifier }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DedicatedLogVolume": "{{ DedicatedLogVolume }}",
 "DeleteAutomatedBackups": "{{ DeleteAutomatedBackups }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "Domain": "{{ Domain }}",
 "DomainAuthSecretArn": "{{ DomainAuthSecretArn }}",
 "DomainDnsIps": [
  "{{ DomainDnsIps[0] }}"
 ],
 "DomainFqdn": "{{ DomainFqdn }}",
 "DomainIAMRoleName": "{{ DomainIAMRoleName }}",
 "DomainOu": "{{ DomainOu }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EnableIAMDatabaseAuthentication": "{{ EnableIAMDatabaseAuthentication }}",
 "EnablePerformanceInsights": "{{ EnablePerformanceInsights }}",
 "Endpoint": {
  "Address": "{{ Address }}",
  "Port": "{{ Port }}",
  "HostedZoneId": "{{ HostedZoneId }}"
 },
 "Engine": "{{ Engine }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ManageMasterUserPassword": "{{ ManageMasterUserPassword }}",
 "Iops": "{{ Iops }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "LicenseModel": "{{ LicenseModel }}",
 "MasterUsername": "{{ MasterUsername }}",
 "MasterUserPassword": "{{ MasterUserPassword }}",
 "MasterUserSecret": {
  "SecretArn": "{{ SecretArn }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "MaxAllocatedStorage": "{{ MaxAllocatedStorage }}",
 "MonitoringInterval": "{{ MonitoringInterval }}",
 "MonitoringRoleArn": "{{ MonitoringRoleArn }}",
 "MultiAZ": "{{ MultiAZ }}",
 "NcharCharacterSetName": "{{ NcharCharacterSetName }}",
 "NetworkType": "{{ NetworkType }}",
 "OptionGroupName": "{{ OptionGroupName }}",
 "PerformanceInsightsKMSKeyId": "{{ PerformanceInsightsKMSKeyId }}",
 "PerformanceInsightsRetentionPeriod": "{{ PerformanceInsightsRetentionPeriod }}",
 "Port": "{{ Port }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "ProcessorFeatures": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}"
  }
 ],
 "PromotionTier": "{{ PromotionTier }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "ReplicaMode": "{{ ReplicaMode }}",
 "RestoreTime": "{{ RestoreTime }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "SourceDbiResourceId": "{{ SourceDbiResourceId }}",
 "SourceDBInstanceAutomatedBackupsArn": "{{ SourceDBInstanceAutomatedBackupsArn }}",
 "SourceDBInstanceIdentifier": "{{ SourceDBInstanceIdentifier }}",
 "SourceRegion": "{{ SourceRegion }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
 "StorageType": "{{ StorageType }}",
 "StorageThroughput": "{{ StorageThroughput }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TdeCredentialArn": "{{ TdeCredentialArn }}",
 "TdeCredentialPassword": "{{ TdeCredentialPassword }}",
 "Timezone": "{{ Timezone }}",
 "UseDefaultProcessorFeatures": "{{ UseDefaultProcessorFeatures }}",
 "UseLatestRestorableTime": "{{ UseLatestRestorableTime }}",
 "VPCSecurityGroups": [
  "{{ VPCSecurityGroups[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.rds.db_instances (
 AllocatedStorage,
 AllowMajorVersionUpgrade,
 AssociatedRoles,
 AutoMinorVersionUpgrade,
 AutomaticBackupReplicationRegion,
 AvailabilityZone,
 BackupRetentionPeriod,
 CACertificateIdentifier,
 CertificateDetails,
 CertificateRotationRestart,
 CharacterSetName,
 CopyTagsToSnapshot,
 CustomIAMInstanceProfile,
 DBClusterIdentifier,
 DBClusterSnapshotIdentifier,
 DBInstanceClass,
 DBInstanceIdentifier,
 DBName,
 DBParameterGroupName,
 DBSecurityGroups,
 DBSnapshotIdentifier,
 DBSubnetGroupName,
 DedicatedLogVolume,
 DeleteAutomatedBackups,
 DeletionProtection,
 Domain,
 DomainAuthSecretArn,
 DomainDnsIps,
 DomainFqdn,
 DomainIAMRoleName,
 DomainOu,
 EnableCloudwatchLogsExports,
 EnableIAMDatabaseAuthentication,
 EnablePerformanceInsights,
 Endpoint,
 Engine,
 EngineVersion,
 ManageMasterUserPassword,
 Iops,
 KmsKeyId,
 LicenseModel,
 MasterUsername,
 MasterUserPassword,
 MasterUserSecret,
 MaxAllocatedStorage,
 MonitoringInterval,
 MonitoringRoleArn,
 MultiAZ,
 NcharCharacterSetName,
 NetworkType,
 OptionGroupName,
 PerformanceInsightsKMSKeyId,
 PerformanceInsightsRetentionPeriod,
 Port,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 ProcessorFeatures,
 PromotionTier,
 PubliclyAccessible,
 ReplicaMode,
 RestoreTime,
 SourceDBClusterIdentifier,
 SourceDbiResourceId,
 SourceDBInstanceAutomatedBackupsArn,
 SourceDBInstanceIdentifier,
 SourceRegion,
 StorageEncrypted,
 StorageType,
 StorageThroughput,
 Tags,
 TdeCredentialArn,
 TdeCredentialPassword,
 Timezone,
 UseDefaultProcessorFeatures,
 UseLatestRestorableTime,
 VPCSecurityGroups,
 region
)
SELECT 
 {{ AllocatedStorage }},
 {{ AllowMajorVersionUpgrade }},
 {{ AssociatedRoles }},
 {{ AutoMinorVersionUpgrade }},
 {{ AutomaticBackupReplicationRegion }},
 {{ AvailabilityZone }},
 {{ BackupRetentionPeriod }},
 {{ CACertificateIdentifier }},
 {{ CertificateDetails }},
 {{ CertificateRotationRestart }},
 {{ CharacterSetName }},
 {{ CopyTagsToSnapshot }},
 {{ CustomIAMInstanceProfile }},
 {{ DBClusterIdentifier }},
 {{ DBClusterSnapshotIdentifier }},
 {{ DBInstanceClass }},
 {{ DBInstanceIdentifier }},
 {{ DBName }},
 {{ DBParameterGroupName }},
 {{ DBSecurityGroups }},
 {{ DBSnapshotIdentifier }},
 {{ DBSubnetGroupName }},
 {{ DedicatedLogVolume }},
 {{ DeleteAutomatedBackups }},
 {{ DeletionProtection }},
 {{ Domain }},
 {{ DomainAuthSecretArn }},
 {{ DomainDnsIps }},
 {{ DomainFqdn }},
 {{ DomainIAMRoleName }},
 {{ DomainOu }},
 {{ EnableCloudwatchLogsExports }},
 {{ EnableIAMDatabaseAuthentication }},
 {{ EnablePerformanceInsights }},
 {{ Endpoint }},
 {{ Engine }},
 {{ EngineVersion }},
 {{ ManageMasterUserPassword }},
 {{ Iops }},
 {{ KmsKeyId }},
 {{ LicenseModel }},
 {{ MasterUsername }},
 {{ MasterUserPassword }},
 {{ MasterUserSecret }},
 {{ MaxAllocatedStorage }},
 {{ MonitoringInterval }},
 {{ MonitoringRoleArn }},
 {{ MultiAZ }},
 {{ NcharCharacterSetName }},
 {{ NetworkType }},
 {{ OptionGroupName }},
 {{ PerformanceInsightsKMSKeyId }},
 {{ PerformanceInsightsRetentionPeriod }},
 {{ Port }},
 {{ PreferredBackupWindow }},
 {{ PreferredMaintenanceWindow }},
 {{ ProcessorFeatures }},
 {{ PromotionTier }},
 {{ PubliclyAccessible }},
 {{ ReplicaMode }},
 {{ RestoreTime }},
 {{ SourceDBClusterIdentifier }},
 {{ SourceDbiResourceId }},
 {{ SourceDBInstanceAutomatedBackupsArn }},
 {{ SourceDBInstanceIdentifier }},
 {{ SourceRegion }},
 {{ StorageEncrypted }},
 {{ StorageType }},
 {{ StorageThroughput }},
 {{ Tags }},
 {{ TdeCredentialArn }},
 {{ TdeCredentialPassword }},
 {{ Timezone }},
 {{ UseDefaultProcessorFeatures }},
 {{ UseLatestRestorableTime }},
 {{ VPCSecurityGroups }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.db_instances
WHERE data__Identifier = '<DBInstanceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_instances</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
iam:GetRole,
iam:ListRoles,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey,
rds:AddRoleToDBInstance,
rds:AddTagsToResource,
rds:CreateDBInstance,
rds:CreateDBInstanceReadReplica,
rds:DescribeDBInstances,
rds:DescribeDBClusters,
rds:DescribeDBClusterSnapshots,
rds:DescribeDBInstanceAutomatedBackups,
rds:DescribeDBSnapshots,
rds:DescribeEvents,
rds:ModifyDBInstance,
rds:RebootDBInstance,
rds:RestoreDBInstanceFromDBSnapshot,
rds:RestoreDBInstanceToPointInTime,
rds:StartDBInstanceAutomatedBackupsReplication,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### Delete
```json
rds:CreateDBSnapshot,
rds:DeleteDBInstance,
rds:DescribeDBInstances
```

### List
```json
rds:DescribeDBInstances
```

