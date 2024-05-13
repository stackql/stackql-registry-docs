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
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBInstance</code> resource creates an Amazon DB instance. The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster.&lt;br&#x2F;&gt; For more information about creating an RDS DB instance, see &#91;Creating an Amazon RDS DB instance&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt; For more information about creating a DB instance in an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;AuroraUserGuide&#x2F;Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.&lt;br&#x2F;&gt; If you import an existing DB instance, and the template configuration doesn't match the actual configuration of the DB instance, AWS CloudFormation applies the changes in the template during the import operation.&lt;br&#x2F;&gt;  If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an</td></tr>
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
    <td><CopyableCode code="region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>db_instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
'{{ AllocatedStorage }}',
 '{{ AllowMajorVersionUpgrade }}',
 '{{ AssociatedRoles }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ AutomaticBackupReplicationRegion }}',
 '{{ AvailabilityZone }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CACertificateIdentifier }}',
 '{{ CertificateDetails }}',
 '{{ CertificateRotationRestart }}',
 '{{ CharacterSetName }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ CustomIAMInstanceProfile }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterSnapshotIdentifier }}',
 '{{ DBInstanceClass }}',
 '{{ DBInstanceIdentifier }}',
 '{{ DBName }}',
 '{{ DBParameterGroupName }}',
 '{{ DBSecurityGroups }}',
 '{{ DBSnapshotIdentifier }}',
 '{{ DBSubnetGroupName }}',
 '{{ DedicatedLogVolume }}',
 '{{ DeleteAutomatedBackups }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainAuthSecretArn }}',
 '{{ DomainDnsIps }}',
 '{{ DomainFqdn }}',
 '{{ DomainIAMRoleName }}',
 '{{ DomainOu }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ EnablePerformanceInsights }}',
 '{{ Endpoint }}',
 '{{ Engine }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ LicenseModel }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MaxAllocatedStorage }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ MultiAZ }}',
 '{{ NcharCharacterSetName }}',
 '{{ NetworkType }}',
 '{{ OptionGroupName }}',
 '{{ PerformanceInsightsKMSKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ ProcessorFeatures }}',
 '{{ PromotionTier }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicaMode }}',
 '{{ RestoreTime }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceDbiResourceId }}',
 '{{ SourceDBInstanceAutomatedBackupsArn }}',
 '{{ SourceDBInstanceIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ StorageThroughput }}',
 '{{ Tags }}',
 '{{ TdeCredentialArn }}',
 '{{ TdeCredentialPassword }}',
 '{{ Timezone }}',
 '{{ UseDefaultProcessorFeatures }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VPCSecurityGroups }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AllocatedStorage }}',
 '{{ AllowMajorVersionUpgrade }}',
 '{{ AssociatedRoles }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ AutomaticBackupReplicationRegion }}',
 '{{ AvailabilityZone }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CACertificateIdentifier }}',
 '{{ CertificateDetails }}',
 '{{ CertificateRotationRestart }}',
 '{{ CharacterSetName }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ CustomIAMInstanceProfile }}',
 '{{ DBClusterIdentifier }}',
 '{{ DBClusterSnapshotIdentifier }}',
 '{{ DBInstanceClass }}',
 '{{ DBInstanceIdentifier }}',
 '{{ DBName }}',
 '{{ DBParameterGroupName }}',
 '{{ DBSecurityGroups }}',
 '{{ DBSnapshotIdentifier }}',
 '{{ DBSubnetGroupName }}',
 '{{ DedicatedLogVolume }}',
 '{{ DeleteAutomatedBackups }}',
 '{{ DeletionProtection }}',
 '{{ Domain }}',
 '{{ DomainAuthSecretArn }}',
 '{{ DomainDnsIps }}',
 '{{ DomainFqdn }}',
 '{{ DomainIAMRoleName }}',
 '{{ DomainOu }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ EnablePerformanceInsights }}',
 '{{ Endpoint }}',
 '{{ Engine }}',
 '{{ EngineVersion }}',
 '{{ ManageMasterUserPassword }}',
 '{{ Iops }}',
 '{{ KmsKeyId }}',
 '{{ LicenseModel }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ MaxAllocatedStorage }}',
 '{{ MonitoringInterval }}',
 '{{ MonitoringRoleArn }}',
 '{{ MultiAZ }}',
 '{{ NcharCharacterSetName }}',
 '{{ NetworkType }}',
 '{{ OptionGroupName }}',
 '{{ PerformanceInsightsKMSKeyId }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ Port }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ ProcessorFeatures }}',
 '{{ PromotionTier }}',
 '{{ PubliclyAccessible }}',
 '{{ ReplicaMode }}',
 '{{ RestoreTime }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ SourceDbiResourceId }}',
 '{{ SourceDBInstanceAutomatedBackupsArn }}',
 '{{ SourceDBInstanceIdentifier }}',
 '{{ SourceRegion }}',
 '{{ StorageEncrypted }}',
 '{{ StorageType }}',
 '{{ StorageThroughput }}',
 '{{ Tags }}',
 '{{ TdeCredentialArn }}',
 '{{ TdeCredentialPassword }}',
 '{{ Timezone }}',
 '{{ UseDefaultProcessorFeatures }}',
 '{{ UseLatestRestorableTime }}',
 '{{ VPCSecurityGroups }}',
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
  - name: db_instance
    props:
      - name: AllocatedStorage
        value: '{{ AllocatedStorage }}'
      - name: AllowMajorVersionUpgrade
        value: '{{ AllowMajorVersionUpgrade }}'
      - name: AssociatedRoles
        value:
          - FeatureName: '{{ FeatureName }}'
            RoleArn: '{{ RoleArn }}'
      - name: AutoMinorVersionUpgrade
        value: '{{ AutoMinorVersionUpgrade }}'
      - name: AutomaticBackupReplicationRegion
        value: '{{ AutomaticBackupReplicationRegion }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: BackupRetentionPeriod
        value: '{{ BackupRetentionPeriod }}'
      - name: CACertificateIdentifier
        value: '{{ CACertificateIdentifier }}'
      - name: CertificateDetails
        value:
          CAIdentifier: '{{ CAIdentifier }}'
          ValidTill: '{{ ValidTill }}'
      - name: CertificateRotationRestart
        value: '{{ CertificateRotationRestart }}'
      - name: CharacterSetName
        value: '{{ CharacterSetName }}'
      - name: CopyTagsToSnapshot
        value: '{{ CopyTagsToSnapshot }}'
      - name: CustomIAMInstanceProfile
        value: '{{ CustomIAMInstanceProfile }}'
      - name: DBClusterIdentifier
        value: '{{ DBClusterIdentifier }}'
      - name: DBClusterSnapshotIdentifier
        value: '{{ DBClusterSnapshotIdentifier }}'
      - name: DBInstanceClass
        value: '{{ DBInstanceClass }}'
      - name: DBInstanceIdentifier
        value: '{{ DBInstanceIdentifier }}'
      - name: DBName
        value: '{{ DBName }}'
      - name: DBParameterGroupName
        value: '{{ DBParameterGroupName }}'
      - name: DBSecurityGroups
        value:
          - '{{ DBSecurityGroups[0] }}'
      - name: DBSnapshotIdentifier
        value: '{{ DBSnapshotIdentifier }}'
      - name: DBSubnetGroupName
        value: '{{ DBSubnetGroupName }}'
      - name: DedicatedLogVolume
        value: '{{ DedicatedLogVolume }}'
      - name: DeleteAutomatedBackups
        value: '{{ DeleteAutomatedBackups }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: DomainAuthSecretArn
        value: '{{ DomainAuthSecretArn }}'
      - name: DomainDnsIps
        value:
          - '{{ DomainDnsIps[0] }}'
      - name: DomainFqdn
        value: '{{ DomainFqdn }}'
      - name: DomainIAMRoleName
        value: '{{ DomainIAMRoleName }}'
      - name: DomainOu
        value: '{{ DomainOu }}'
      - name: EnableCloudwatchLogsExports
        value:
          - '{{ EnableCloudwatchLogsExports[0] }}'
      - name: EnableIAMDatabaseAuthentication
        value: '{{ EnableIAMDatabaseAuthentication }}'
      - name: EnablePerformanceInsights
        value: '{{ EnablePerformanceInsights }}'
      - name: Endpoint
        value:
          Address: '{{ Address }}'
          Port: '{{ Port }}'
          HostedZoneId: '{{ HostedZoneId }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: ManageMasterUserPassword
        value: '{{ ManageMasterUserPassword }}'
      - name: Iops
        value: '{{ Iops }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: LicenseModel
        value: '{{ LicenseModel }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: MasterUserSecret
        value:
          SecretArn: '{{ SecretArn }}'
          KmsKeyId: '{{ KmsKeyId }}'
      - name: MaxAllocatedStorage
        value: '{{ MaxAllocatedStorage }}'
      - name: MonitoringInterval
        value: '{{ MonitoringInterval }}'
      - name: MonitoringRoleArn
        value: '{{ MonitoringRoleArn }}'
      - name: MultiAZ
        value: '{{ MultiAZ }}'
      - name: NcharCharacterSetName
        value: '{{ NcharCharacterSetName }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
      - name: OptionGroupName
        value: '{{ OptionGroupName }}'
      - name: PerformanceInsightsKMSKeyId
        value: '{{ PerformanceInsightsKMSKeyId }}'
      - name: PerformanceInsightsRetentionPeriod
        value: '{{ PerformanceInsightsRetentionPeriod }}'
      - name: Port
        value: '{{ Port }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: ProcessorFeatures
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'
      - name: PromotionTier
        value: '{{ PromotionTier }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: ReplicaMode
        value: '{{ ReplicaMode }}'
      - name: RestoreTime
        value: '{{ RestoreTime }}'
      - name: SourceDBClusterIdentifier
        value: '{{ SourceDBClusterIdentifier }}'
      - name: SourceDbiResourceId
        value: '{{ SourceDbiResourceId }}'
      - name: SourceDBInstanceAutomatedBackupsArn
        value: '{{ SourceDBInstanceAutomatedBackupsArn }}'
      - name: SourceDBInstanceIdentifier
        value: '{{ SourceDBInstanceIdentifier }}'
      - name: SourceRegion
        value: '{{ SourceRegion }}'
      - name: StorageEncrypted
        value: '{{ StorageEncrypted }}'
      - name: StorageType
        value: '{{ StorageType }}'
      - name: StorageThroughput
        value: '{{ StorageThroughput }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TdeCredentialArn
        value: '{{ TdeCredentialArn }}'
      - name: TdeCredentialPassword
        value: '{{ TdeCredentialPassword }}'
      - name: Timezone
        value: '{{ Timezone }}'
      - name: UseDefaultProcessorFeatures
        value: '{{ UseDefaultProcessorFeatures }}'
      - name: UseLatestRestorableTime
        value: '{{ UseLatestRestorableTime }}'
      - name: VPCSecurityGroups
        value:
          - '{{ VPCSecurityGroups[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

