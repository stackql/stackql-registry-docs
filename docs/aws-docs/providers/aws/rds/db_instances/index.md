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
Retrieves a list of <code>db_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.rds.db_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AllocatedStorage</code></td><td><code>string</code></td><td>The amount of storage (in gigabytes) to be initially allocated for the database instance.</td></tr>
<tr><td><code>AllowMajorVersionUpgrade</code></td><td><code>boolean</code></td><td>A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.</td></tr>
<tr><td><code>AssociatedRoles</code></td><td><code>array</code></td><td>The AWS Identity and Access Management (IAM) roles associated with the DB instance.</td></tr>
<tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td>A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.</td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td>The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.</td></tr>
<tr><td><code>BackupRetentionPeriod</code></td><td><code>integer</code></td><td>The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.</td></tr>
<tr><td><code>CACertificateIdentifier</code></td><td><code>string</code></td><td>The identifier of the CA certificate for this DB instance.</td></tr>
<tr><td><code>CertificateDetails</code></td><td><code>undefined</code></td><td>Returns the details of the DB instance's server certificate.</td></tr>
<tr><td><code>CertificateRotationRestart</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance is restarted when you rotate your SSL&#x2F;TLS certificate.&lt;br&#x2F;&gt;By default, the DB instance is restarted when you rotate your SSL&#x2F;TLS certificate. The certificate is not updated until the DB instance is restarted.&lt;br&#x2F;&gt;If you are using SSL&#x2F;TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL&#x2F;TLS certificate&lt;br&#x2F;&gt;This setting doesn't apply to RDS Custom.</td></tr>
<tr><td><code>CharacterSetName</code></td><td><code>string</code></td><td>For supported engines, indicates that the DB instance should be associated with the specified character set.</td></tr>
<tr><td><code>CopyTagsToSnapshot</code></td><td><code>boolean</code></td><td>A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.</td></tr>
<tr><td><code>CustomIAMInstanceProfile</code></td><td><code>string</code></td><td>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:&lt;br&#x2F;&gt; * The profile must exist in your account.&lt;br&#x2F;&gt; * The profile must have an IAM role that Amazon EC2 has permissions to assume.&lt;br&#x2F;&gt; * The instance profile name and the associated IAM role name must start with the prefix AWSRDSCustom .&lt;br&#x2F;&gt;For the list of permissions required for the IAM role, see Configure IAM and your VPC in the Amazon RDS User Guide .&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This setting is required for RDS Custom.</td></tr>
<tr><td><code>DBClusterIdentifier</code></td><td><code>string</code></td><td>The identifier of the DB cluster that the instance will belong to.</td></tr>
<tr><td><code>DBClusterSnapshotIdentifier</code></td><td><code>string</code></td><td>The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Constraints:&lt;br&#x2F;&gt; * Must match the identifier of an existing Multi-AZ DB cluster snapshot.&lt;br&#x2F;&gt; * Can't be specified when DBSnapshotIdentifier is specified.&lt;br&#x2F;&gt; * Must be specified when DBSnapshotIdentifier isn't specified.&lt;br&#x2F;&gt; * If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.&lt;br&#x2F;&gt; * Can't be the identifier of an Aurora DB cluster snapshot.&lt;br&#x2F;&gt; * Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.</td></tr>
<tr><td><code>DBInstanceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB instance.</td></tr>
<tr><td><code>DBInstanceClass</code></td><td><code>string</code></td><td>The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.</td></tr>
<tr><td><code>DBInstanceIdentifier</code></td><td><code>string</code></td><td>A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.</td></tr>
<tr><td><code>DbiResourceId</code></td><td><code>string</code></td><td>The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.</td></tr>
<tr><td><code>DBName</code></td><td><code>string</code></td><td>The meaning of this parameter differs according to the database engine you use.</td></tr>
<tr><td><code>DBParameterGroupName</code></td><td><code>string</code></td><td>The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.</td></tr>
<tr><td><code>DBSecurityGroups</code></td><td><code>array</code></td><td>A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.</td></tr>
<tr><td><code>DBSnapshotIdentifier</code></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the DB snapshot that's used to restore the DB instance. If you're restoring from a shared manual DB snapshot, you must specify the ARN of the snapshot.</td></tr>
<tr><td><code>DBSubnetGroupName</code></td><td><code>string</code></td><td>A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new VPC.</td></tr>
<tr><td><code>DBSystemId</code></td><td><code>string</code></td><td>The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.</td></tr>
<tr><td><code>DeleteAutomatedBackups</code></td><td><code>boolean</code></td><td>A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.</td></tr>
<tr><td><code>DeletionProtection</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.</td></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td>The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.</td></tr>
<tr><td><code>DomainIAMRoleName</code></td><td><code>string</code></td><td>Specify the name of the IAM role to be used when making API calls to the Directory Service.</td></tr>
<tr><td><code>EnableCloudwatchLogsExports</code></td><td><code>array</code></td><td>The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.</td></tr>
<tr><td><code>EnableIAMDatabaseAuthentication</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.</td></tr>
<tr><td><code>EnablePerformanceInsights</code></td><td><code>boolean</code></td><td>A value that indicates whether to enable Performance Insights for the DB instance.</td></tr>
<tr><td><code>Endpoint</code></td><td><code>undefined</code></td><td>Specifies the connection endpoint.</td></tr>
<tr><td><code>Engine</code></td><td><code>string</code></td><td>The name of the database engine that you want to use for this DB instance.</td></tr>
<tr><td><code>EngineVersion</code></td><td><code>string</code></td><td>The version number of the database engine to use.</td></tr>
<tr><td><code>ManageMasterUserPassword</code></td><td><code>boolean</code></td><td>A value that indicates whether to manage the master user password with AWS Secrets Manager.</td></tr>
<tr><td><code>Iops</code></td><td><code>integer</code></td><td>The number of I&#x2F;O operations per second (IOPS) that the database provisions.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) master key that's used to encrypt the DB instance.</td></tr>
<tr><td><code>LicenseModel</code></td><td><code>string</code></td><td>License model information for this DB instance.</td></tr>
<tr><td><code>MasterUsername</code></td><td><code>string</code></td><td>The master user name for the DB instance.</td></tr>
<tr><td><code>MasterUserPassword</code></td><td><code>string</code></td><td>The password for the master user.</td></tr>
<tr><td><code>MasterUserSecret</code></td><td><code>undefined</code></td><td>Contains the secret managed by RDS in AWS Secrets Manager for the master user password.</td></tr>
<tr><td><code>MaxAllocatedStorage</code></td><td><code>integer</code></td><td>The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.</td></tr>
<tr><td><code>MonitoringInterval</code></td><td><code>integer</code></td><td>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.</td></tr>
<tr><td><code>MonitoringRoleArn</code></td><td><code>string</code></td><td>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.</td></tr>
<tr><td><code>MultiAZ</code></td><td><code>boolean</code></td><td>Specifies whether the database instance is a multiple Availability Zone deployment.</td></tr>
<tr><td><code>NcharCharacterSetName</code></td><td><code>string</code></td><td>The name of the NCHAR character set for the Oracle DB instance. This parameter doesn't apply to RDS Custom.</td></tr>
<tr><td><code>NetworkType</code></td><td><code>string</code></td><td>The network type of the DB cluster.</td></tr>
<tr><td><code>OptionGroupName</code></td><td><code>string</code></td><td>Indicates that the DB instance should be associated with the specified option group.</td></tr>
<tr><td><code>PerformanceInsightsKMSKeyId</code></td><td><code>string</code></td><td>The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.</td></tr>
<tr><td><code>PerformanceInsightsRetentionPeriod</code></td><td><code>integer</code></td><td>The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).</td></tr>
<tr><td><code>Port</code></td><td><code>string</code></td><td>The port number on which the database accepts connections.</td></tr>
<tr><td><code>PreferredBackupWindow</code></td><td><code>string</code></td><td>The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.</td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td>he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</td></tr>
<tr><td><code>ProcessorFeatures</code></td><td><code>array</code></td><td>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</td></tr>
<tr><td><code>PromotionTier</code></td><td><code>integer</code></td><td>A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.</td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td>Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.</td></tr>
<tr><td><code>ReplicaMode</code></td><td><code>string</code></td><td>The open mode of an Oracle read replica. The default is open-read-only.</td></tr>
<tr><td><code>RestoreTime</code></td><td><code>string</code></td><td>The date and time to restore from.</td></tr>
<tr><td><code>SourceDBClusterIdentifier</code></td><td><code>string</code></td><td>The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.</td></tr>
<tr><td><code>SourceDbiResourceId</code></td><td><code>string</code></td><td>The resource ID of the source DB instance from which to restore.</td></tr>
<tr><td><code>SourceDBInstanceAutomatedBackupsArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the replicated automated backups from which to restore.</td></tr>
<tr><td><code>SourceDBInstanceIdentifier</code></td><td><code>string</code></td><td>If you want to create a Read Replica DB instance, specify the ID of the source DB instance. Each DB instance can have a limited number of Read Replicas.</td></tr>
<tr><td><code>SourceRegion</code></td><td><code>string</code></td><td>The ID of the region that contains the source DB instance for the Read Replica.</td></tr>
<tr><td><code>StorageEncrypted</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance is encrypted. By default, it isn't encrypted.</td></tr>
<tr><td><code>StorageType</code></td><td><code>string</code></td><td>Specifies the storage type to be associated with the DB instance.</td></tr>
<tr><td><code>StorageThroughput</code></td><td><code>integer</code></td><td>Specifies the storage throughput for the DB instance.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags to assign to the DB instance.</td></tr>
<tr><td><code>TdeCredentialArn</code></td><td><code>string</code></td><td>The ARN from the key store with which to associate the instance for TDE encryption.</td></tr>
<tr><td><code>TdeCredentialPassword</code></td><td><code>string</code></td><td>The password for the given ARN from the key store in order to access the device.</td></tr>
<tr><td><code>Timezone</code></td><td><code>string</code></td><td>The time zone of the DB instance. The time zone parameter is currently supported only by Microsoft SQL Server.</td></tr>
<tr><td><code>UseDefaultProcessorFeatures</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance class of the DB instance uses its default processor features.</td></tr>
<tr><td><code>UseLatestRestorableTime</code></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance is restored from the latest backup time. By default, the DB instance isn't restored from the latest backup time.</td></tr>
<tr><td><code>VPCSecurityGroups</code></td><td><code>array</code></td><td>A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.rds.db_instances
WHERE region = 'us-east-1'
</pre>
