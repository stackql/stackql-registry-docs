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

Creates, updates, deletes or gets a <code>db_instance</code> resource or lists <code>db_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::DBInstance</code> resource creates an Amazon DB instance. The new DB instance can be an RDS DB instance, or it can be a DB instance in an Aurora DB cluster.<br />For more information about creating an RDS DB instance, see &#91;Creating an Amazon RDS DB instance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) in the *Amazon RDS User Guide*.<br />For more information about creating a DB instance in an Aurora DB cluster, see &#91;Creating an Amazon Aurora DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the *Amazon Aurora User Guide*.<br />If you import an existing DB instance, and the template configuration doesn't match the actual configuration of the DB instance, AWS CloudFormation applies the changes in the template during the import operation.<br />If a DB instance is deleted or replaced during an update, AWS CloudFormation deletes all automated snapshots. However, it retains manual DB snapshots. During an update that requires replacement, you can apply a stack policy to prevent DB instances from being replaced. For more information, see &#91;Prevent Updates to Stack Resources&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html).<br />*Updating DB instances* <br />When properties labeled "*Update requires:* &#91;Replacement&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)" are updated, AWS CloudFormation first creates a replacement DB instance, then changes references from other dependent resources to point to the replacement DB instance, and finally deletes the old DB instance.<br />We highly recommend that you take a snapshot of the database before updating the stack. If you don't, you lose the data when AWS CloudFormation replaces your DB instance. To preserve your data, perform the following procedure:<br />1. Deactivate any applications that are using the DB instance so that there's no activity on the DB instance.<br />1. Create a snapshot of the DB instance. For more information, see &#91;Creating a DB Snapshot&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html).<br />1. If you want to restore your instance using a DB snapshot, modify the updated template with your DB instance changes and add the <code>DBSnapshotIdentifier</code> property with the ID of the DB snapshot that you want to use.<br />After you restore a DB instance with a <code>DBSnapshotIdentifier</code> property, you can delete the <code>DBSnapshotIdentifier</code> property. When you specify this property for an update, the DB instance is not restored from the DB snapshot again, and the data in the database is not changed. However, if you don't specify the <code>DBSnapshotIdentifier</code> property, an empty DB instance is created, and the original DB instance is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB instance is restored from the specified <code>DBSnapshotIdentifier</code> property, and the original DB instance is deleted.<br />1. Update the stack.<br /><br />For more information about updating other properties of this resource, see <code>ModifyDBInstance</code>. For more information about updating stacks, see &#91;CloudFormation Stacks Updates&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html).<br />*Deleting DB instances* <br />For DB instances that are part of an Aurora DB cluster, you can set a deletion policy for your DB instance to control how AWS CloudFormation handles the DB instance when the stack is deleted. For Amazon RDS DB instances, you can choose to *retain* the DB instance, to *delete* the DB instance, or to *create a snapshot* of the DB instance. The default AWS CloudFormation behavior depends on the <code>DBClusterIdentifier</code> property:<br />1. For <code>AWS::RDS::DBInstance</code> resources that don't specify the <code>DBClusterIdentifier</code> property, AWS CloudFormation saves a snapshot of the DB instance.<br />1. For <code>AWS::RDS::DBInstance</code> resources that do specify the <code>DBClusterIdentifier</code> property, AWS CloudFormation deletes the DB instance.<br /><br />For more information, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance is encrypted. By default, it isn't encrypted.<br />If you specify the <code>KmsKeyId</code> property, then you must enable encryption.<br />If you specify the <code>SourceDBInstanceIdentifier</code> property, don't specify this property. The value is inherited from the source DB instance, and if the DB instance is encrypted, the specified <code>KmsKeyId</code> property is used.<br />If you specify <code>DBSnapshotIdentifier</code> property, don't specify this property. The value is inherited from the snapshot.<br />*Amazon Aurora* <br />Not applicable. The encryption for DB instances is managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="timezone" /></td><td><code>string</code></td><td>The time zone of the DB instance. The time zone parameter is currently supported only by &#91;RDS for Db2&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone) and &#91;RDS for SQL Server&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.TimeZone).</td></tr>
<tr><td><CopyableCode code="db_system_id" /></td><td><code>string</code></td><td>The Oracle system identifier (SID), which is the name of the Oracle database instance that manages your database files. In this context, the term "Oracle database instance" refers exclusively to the system global area (SGA) and Oracle background processes. If you don't specify a SID, the value defaults to <code>RDSCDB</code>. The Oracle SID is also the name of your CDB.</td></tr>
<tr><td><CopyableCode code="certificate_details" /></td><td><code>object</code></td><td>The details of the DB instance's server certificate.</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>string</code></td><td>The port number on which the database accepts connections.<br />*Amazon Aurora* <br />Not applicable. The port number is managed by the DB cluster.<br />*Db2* <br />Default value: <code>50000</code></td></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The identifier of the DB cluster that the instance will belong to.</td></tr>
<tr><td><CopyableCode code="storage_throughput" /></td><td><code>integer</code></td><td>Specifies the storage throughput value for the DB instance. This setting applies only to the <code>gp3</code> storage type. <br />This setting doesn't apply to RDS Custom or Amazon Aurora.</td></tr>
<tr><td><CopyableCode code="dbi_resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitoring_interval" /></td><td><code>integer</code></td><td>The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collection of Enhanced Monitoring metrics, specify 0. The default is 0.<br />If <code>MonitoringRoleArn</code> is specified, then you must set <code>MonitoringInterval</code> to a value other than 0.<br />This setting doesn't apply to RDS Custom.<br />Valid Values: <code>0, 1, 5, 10, 15, 30, 60</code></td></tr>
<tr><td><CopyableCode code="db_parameter_group_name" /></td><td><code>string</code></td><td>The name of an existing DB parameter group or a reference to an &#91;AWS::RDS::DBParameterGroup&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html) resource created in the template.<br />To list all of the available DB parameter group names, use the following command:<br /><code>aws rds describe-db-parameter-groups --query "DBParameterGroups&#91;&#93;.DBParameterGroupName" --output text</code> <br />If any of the data members of the referenced parameter group are changed during an update, the DB instance might need to be restarted, which causes some interruption. If the parameter group contains static parameters, whether they were changed or not, an update triggers a reboot.<br />If you don't specify a value for <code>DBParameterGroupName</code> property, the default DB parameter group for the specified engine and engine version is used.</td></tr>
<tr><td><CopyableCode code="db_instance_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>object</code></td><td>The connection endpoint for the DB instance.<br />The endpoint might not be shown for instances with the status of <code>creating</code>.</td></tr>
<tr><td><CopyableCode code="tde_credential_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="automatic_backup_replication_kms_key_id" /></td><td><code>string</code></td><td>The AWS KMS key identifier for encryption of the replicated automated backups. The KMS key ID is the Amazon Resource Name (ARN) for the KMS encryption key in the destination AWS-Region, for example, <code>arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE</code>.</td></tr>
<tr><td><CopyableCode code="multi_az" /></td><td><code>boolean</code></td><td>Specifies whether the database instance is a Multi-AZ DB instance deployment. You can't set the <code>AvailabilityZone</code> parameter if the <code>MultiAZ</code> parameter is set to true. <br />For more information, see &#91;Multi-AZ deployments for high availability&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) in the *Amazon RDS User Guide*.<br />*Amazon Aurora* <br />Not applicable. Amazon Aurora storage is replicated across all of the Availability Zones and doesn't require the <code>MultiAZ</code> option to be set.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The name of the database engine to use for this DB instance. Not every database engine is available in every AWS Region.<br />This property is required when creating a DB instance.<br />You can convert an Oracle database from the non-CDB architecture to the container database (CDB) architecture by updating the <code>Engine</code> value in your templates from <code>oracle-ee</code> to <code>oracle-ee-cdb</code> or from <code>oracle-se2</code> to <code>oracle-se2-cdb</code>. Converting to the CDB architecture requires an interruption.<br />Valid Values:<br />+ <code>aurora-mysql</code> (for Aurora MySQL DB instances)<br />+ <code>aurora-postgresql</code> (for Aurora PostgreSQL DB instances)<br />+ <code>custom-oracle-ee</code> (for RDS Custom for Oracle DB instances)<br />+ <code>custom-oracle-ee-cdb</code> (for RDS Custom for Oracle DB instances)<br />+ <code>custom-sqlserver-ee</code> (for RDS Custom for SQL Server DB instances)<br />+ <code>custom-sqlserver-se</code> (for RDS Custom for SQL Server DB instances)<br />+ <code>custom-sqlserver-web</code> (for RDS Custom for SQL Server DB instances)<br />+ <code>db2-ae</code> <br />+ <code>db2-se</code> <br />+ <code>mariadb</code> <br />+ <code>mysql</code> <br />+ <code>oracle-ee</code> <br />+ <code>oracle-ee-cdb</code> <br />+ <code>oracle-se2</code> <br />+ <code>oracle-se2-cdb</code> <br />+ <code>postgres</code> <br />+ <code>sqlserver-ee</code> <br />+ <code>sqlserver-se</code> <br />+ <code>sqlserver-ex</code> <br />+ <code>sqlserver-web</code></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional array of key-value pairs to apply to this DB instance.</td></tr>
<tr><td><CopyableCode code="performance_insights_kms_key_id" /></td><td><code>string</code></td><td>The AWS KMS key identifier for encryption of Performance Insights data.<br />The KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.<br />If you do not specify a value for <code>PerformanceInsightsKMSKeyId</code>, then Amazon RDS uses your default KMS key. There is a default KMS key for your AWS account. Your AWS account has a different default KMS key for each AWS Region.<br />For information about enabling Performance Insights, see &#91;EnablePerformanceInsights&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-enableperformanceinsights).</td></tr>
<tr><td><CopyableCode code="tde_credential_password" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_db_instance_identifier" /></td><td><code>string</code></td><td>If you want to create a read replica DB instance, specify the ID of the source DB instance. Each DB instance can have a limited number of read replicas. For more information, see &#91;Working with Read Replicas&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/DeveloperGuide/USER_ReadRepl.html) in the *Amazon RDS User Guide*.<br />For information about constraints that apply to DB instance identifiers, see &#91;Naming constraints in Amazon RDS&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.<br />The <code>SourceDBInstanceIdentifier</code> property determines whether a DB instance is a read replica. If you remove the <code>SourceDBInstanceIdentifier</code> property from your template and then update your stack, AWS CloudFormation promotes the Read Replica to a standalone DB instance.<br />+ If you specify a source DB instance that uses VPC security groups, we recommend that you specify the <code>VPCSecurityGroups</code> property. If you don't specify the property, the read replica inherits the value of the <code>VPCSecurityGroups</code> property from the source DB when you create the replica. However, if you update the stack, AWS CloudFormation reverts the replica's <code>VPCSecurityGroups</code> property to the default value because it's not defined in the stack's template. This change might cause unexpected issues.<br />+ Read replicas don't support deletion policies. AWS CloudFormation ignores any deletion policy that's associated with a read replica.<br />+ If you specify <code>SourceDBInstanceIdentifier</code>, don't specify the <code>DBSnapshotIdentifier</code> property. You can't create a read replica from a snapshot.<br />+ Don't set the <code>BackupRetentionPeriod</code>, <code>DBName</code>, <code>MasterUsername</code>, <code>MasterUserPassword</code>, and <code>PreferredBackupWindow</code> properties. The database attributes are inherited from the source DB instance, and backups are disabled for read replicas.<br />+ If the source DB instance is in a different region than the read replica, specify the source region in <code>SourceRegion</code>, and specify an ARN for a valid DB instance in <code>SourceDBInstanceIdentifier</code>. For more information, see &#91;Constructing a Amazon RDS Amazon Resource Name (ARN)&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html#USER_Tagging.ARN) in the *Amazon RDS User Guide*.<br />+ For DB instances in Amazon Aurora clusters, don't specify this property. Amazon RDS automatically assigns writer and reader DB instances.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version number of the database engine to use.<br />For a list of valid engine versions, use the <code>DescribeDBEngineVersions</code> action.<br />The following are the database engines and links to information about the major and minor versions that are available with Amazon RDS. Not every database engine is available for every AWS Region.<br />*Amazon Aurora* <br />Not applicable. The version number of the database engine to be used by the DB instance is managed by the DB cluster.<br />*Db2* <br />See &#91;Amazon RDS for Db2&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html#Db2.Concepts.VersionMgmt) in the *Amazon RDS User Guide.* <br />*MariaDB* <br />See &#91;MariaDB on Amazon RDS Versions&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html#MariaDB.Concepts.VersionMgmt) in the *Amazon RDS User Guide.* <br />*Microsoft SQL Server* <br />See &#91;Microsoft SQL Server Versions on Amazon RDS&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.VersionSupport) in the *Amazon RDS User Guide.* <br />*MySQL* <br />See &#91;MySQL on Amazon RDS Versions&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt) in the *Amazon RDS User Guide.* <br />*Oracle* <br />See &#91;Oracle Database Engine Release Notes&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.PatchComposition.html) in the *Amazon RDS User Guide.* <br />*PostgreSQL* <br />See &#91;Supported PostgreSQL Database Versions&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts.General.DBVersions) in the *Amazon RDS User Guide.*</td></tr>
<tr><td><CopyableCode code="storage_type" /></td><td><code>string</code></td><td>The storage type to associate with the DB instance.<br />If you specify <code>io1</code>, <code>io2</code>, or <code>gp3</code>, you must also include a value for the <code>Iops</code> parameter.<br />This setting doesn't apply to Amazon Aurora DB instances. Storage is managed by the DB cluster.<br />Valid Values: <code>gp2 | gp3 | io1 | io2 | standard</code> <br />Default: <code>io1</code>, if the <code>Iops</code> parameter is specified. Otherwise, <code>gp2</code>.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ARN of the AWS KMS key that's used to encrypt the DB instance, such as <code>arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef</code>. If you enable the StorageEncrypted property but don't specify this property, AWS CloudFormation uses the default KMS key. If you specify this property, you must set the StorageEncrypted property to true. <br />If you specify the <code>SourceDBInstanceIdentifier</code> property, the value is inherited from the source DB instance if the read replica is created in the same region.<br />If you create an encrypted read replica in a different AWS Region, then you must specify a KMS key for the destination AWS Region. KMS encryption keys are specific to the region that they're created in, and you can't use encryption keys from one region in another region.<br />If you specify the <code>DBSnapshotIdentifier</code> property, don't specify this property. The <code>StorageEncrypted</code> property value is inherited from the snapshot. If the DB instance is encrypted, the specified <code>KmsKeyId</code> property is also inherited from the snapshot.<br />If you specify <code>DBSecurityGroups</code>, AWS CloudFormation ignores this property. To specify both a security group and this property, you must use a VPC security group. For more information about Amazon RDS and VPC, see &#91;Using Amazon RDS with Amazon VPC&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html) in the *Amazon RDS User Guide*.<br />*Amazon Aurora* <br />Not applicable. The KMS key identifier is managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="db_instance_class" /></td><td><code>string</code></td><td>The compute and memory capacity of the DB instance, for example <code>db.m5.large</code>. Not all DB instance classes are available in all AWS-Regions, or for all database engines. For the full list of DB instance classes, and availability for your engine, see &#91;DB instance classes&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) in the *Amazon RDS User Guide* or &#91;Aurora DB instance classes&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html) in the *Amazon Aurora User Guide*.</td></tr>
<tr><td><CopyableCode code="delete_automated_backups" /></td><td><code>boolean</code></td><td>A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.<br />*Amazon Aurora* <br />Not applicable. When you delete a DB cluster, all automated backups for that DB cluster are deleted and can't be recovered. Manual DB cluster snapshots of the DB cluster are not deleted.</td></tr>
<tr><td><CopyableCode code="performance_insights_retention_period" /></td><td><code>integer</code></td><td>The number of days to retain Performance Insights data.<br />This setting doesn't apply to RDS Custom DB instances.<br />Valid Values:<br />+ <code>7</code> <br />+ *month* * 31, where *month* is a number of months from 1-23. Examples: <code>93</code> (3 months * 31), <code>341</code> (11 months * 31), <code>589</code> (19 months * 31)<br />+ <code>731</code> <br /><br />Default: <code>7</code> days<br />If you specify a retention period that isn't valid, such as <code>94</code>, Amazon RDS returns an error.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone (AZ) where the database will be created. For information on AWS-Regions and Availability Zones, see &#91;Regions and Availability Zones&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).<br />For Amazon Aurora, each Aurora DB cluster hosts copies of its storage in three separate Availability Zones. Specify one of these Availability Zones. Aurora automatically chooses an appropriate Availability Zone if you don't specify one.<br />Default: A random, system-chosen Availability Zone in the endpoint's AWS-Region.<br />Constraints:<br />+ The <code>AvailabilityZone</code> parameter can't be specified if the DB instance is a Multi-AZ deployment.<br />+ The specified Availability Zone must be in the same AWS-Region as the current endpoint.<br /><br />Example: <code>us-east-1d</code></td></tr>
<tr><td><CopyableCode code="option_group_name" /></td><td><code>string</code></td><td>Indicates that the DB instance should be associated with the specified option group.<br />Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group. Also, that option group can't be removed from a DB instance once it is associated with a DB instance.</td></tr>
<tr><td><CopyableCode code="enable_performance_insights" /></td><td><code>boolean</code></td><td>Specifies whether to enable Performance Insights for the DB instance. For more information, see &#91;Using Amazon Performance Insights&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) in the *Amazon RDS User Guide*.<br />This setting doesn't apply to RDS Custom DB instances.</td></tr>
<tr><td><CopyableCode code="auto_minor_version_upgrade" /></td><td><code>boolean</code></td><td>A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.</td></tr>
<tr><td><CopyableCode code="db_subnet_group_name" /></td><td><code>string</code></td><td>A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new VPC. <br />If there's no DB subnet group, then the DB instance isn't a VPC DB instance.<br />For more information about using Amazon RDS in a VPC, see &#91;Using Amazon RDS with Amazon Virtual Private Cloud (VPC)&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html) in the *Amazon RDS User Guide*. <br />*Amazon Aurora* <br />Not applicable. The DB subnet group is managed by the DB cluster. If specified, the setting must match the DB cluster setting.</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled. For more information, see &#91;Deleting a DB Instance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html). <br />*Amazon Aurora* <br />Not applicable. You can enable or disable deletion protection for the DB cluster. For more information, see <code>CreateDBCluster</code>. DB instances in a DB cluster can be deleted even when deletion protection is enabled for the DB cluster.</td></tr>
<tr><td><CopyableCode code="db_instance_identifier" /></td><td><code>string</code></td><td>A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance. For more information, see &#91;Name Type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />For information about constraints that apply to DB instance identifiers, see &#91;Naming constraints in Amazon RDS&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.<br />If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="allocated_storage" /></td><td><code>string</code></td><td>The amount of storage in gibibytes (GiB) to be initially allocated for the database instance.<br />If any value is set in the <code>Iops</code> parameter, <code>AllocatedStorage</code> must be at least 100 GiB, which corresponds to the minimum Iops value of 1,000. If you increase the <code>Iops</code> value (in 1,000 IOPS increments), then you must also increase the <code>AllocatedStorage</code> value (in 100-GiB increments). <br />*Amazon Aurora* <br />Not applicable. Aurora cluster volumes automatically grow as the amount of data in your database increases, though you are only charged for the space that you use in an Aurora cluster volume.<br />*Db2* <br />Constraints to the amount of storage for each storage type are the following:<br />+ General Purpose (SSD) storage (gp3): Must be an integer from 20 to 64000.<br />+ Provisioned IOPS storage (io1): Must be an integer from 100 to 64000.<br /><br />*MySQL* <br />Constraints to the amount of storage for each storage type are the following: <br />+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.<br />+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.<br />+ Magnetic storage (standard): Must be an integer from 5 to 3072.<br /><br />*MariaDB* <br />Constraints to the amount of storage for each storage type are the following: <br />+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.<br />+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.<br />+ Magnetic storage (standard): Must be an integer from 5 to 3072.<br /><br />*PostgreSQL* <br />Constraints to the amount of storage for each storage type are the following: <br />+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.<br />+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.<br />+ Magnetic storage (standard): Must be an integer from 5 to 3072.<br /><br />*Oracle* <br />Constraints to the amount of storage for each storage type are the following: <br />+ General Purpose (SSD) storage (gp2): Must be an integer from 20 to 65536.<br />+ Provisioned IOPS storage (io1): Must be an integer from 100 to 65536.<br />+ Magnetic storage (standard): Must be an integer from 10 to 3072.<br /><br />*SQL Server* <br />Constraints to the amount of storage for each storage type are the following: <br />+ General Purpose (SSD) storage (gp2):<br />+ Enterprise and Standard editions: Must be an integer from 20 to 16384.<br />+ Web and Express editions: Must be an integer from 20 to 16384.<br /><br />+ Provisioned IOPS storage (io1):<br />+ Enterprise and Standard editions: Must be an integer from 20 to 16384.<br />+ Web and Express editions: Must be an integer from 20 to 16384.<br /><br />+ Magnetic storage (standard):<br />+ Enterprise and Standard editions: Must be an integer from 20 to 1024.<br />+ Web and Express editions: Must be an integer from 20 to 1024.</td></tr>
<tr><td><CopyableCode code="master_user_password" /></td><td><code>string</code></td><td>The password for the master user. The password can include any printable ASCII character except "/", """, or "@".<br />*Amazon Aurora* <br />Not applicable. The password for the master user is managed by the DB cluster.<br />*RDS for Db2* <br />Must contain from 8 to 255 characters.<br />*RDS for MariaDB* <br />Constraints: Must contain from 8 to 41 characters.<br />*RDS for Microsoft SQL Server* <br />Constraints: Must contain from 8 to 128 characters.<br />*RDS for MySQL* <br />Constraints: Must contain from 8 to 41 characters.<br />*RDS for Oracle* <br />Constraints: Must contain from 8 to 30 characters.<br />*RDS for PostgreSQL* <br />Constraints: Must contain from 8 to 128 characters.</td></tr>
<tr><td><CopyableCode code="master_user_secret" /></td><td><code>object</code></td><td>The secret managed by RDS in AWS Secrets Manager for the master user password.<br />For more information, see &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.*</td></tr>
<tr><td><CopyableCode code="nchar_character_set_name" /></td><td><code>string</code></td><td>The name of the NCHAR character set for the Oracle DB instance.<br />This setting doesn't apply to RDS Custom DB instances.</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.<br />Constraints:<br />+ Must be the identifier of an existing Multi-AZ DB cluster.<br />+ Can't be specified if the <code>SourceDBInstanceIdentifier</code> parameter is also specified.<br />+ The specified DB cluster must have automatic backups enabled, that is, its backup retention period must be greater than 0.<br />+ The source DB cluster must be in the same AWS-Region as the read replica. Cross-Region replication isn't supported.</td></tr>
<tr><td><CopyableCode code="db_security_groups" /></td><td><code>array</code></td><td>A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.<br />If you set DBSecurityGroups, you must not set VPCSecurityGroups, and vice versa. Also, note that the DBSecurityGroups property exists only for backwards compatibility with older regions and is no longer recommended for providing security information to an RDS DB instance. Instead, use VPCSecurityGroups.<br />If you specify this property, AWS CloudFormation sends only the following properties (if specified) to Amazon RDS during create operations:<br />+ <code>AllocatedStorage</code> <br />+ <code>AutoMinorVersionUpgrade</code> <br />+ <code>AvailabilityZone</code> <br />+ <code>BackupRetentionPeriod</code> <br />+ <code>CharacterSetName</code> <br />+ <code>DBInstanceClass</code> <br />+ <code>DBName</code> <br />+ <code>DBParameterGroupName</code> <br />+ <code>DBSecurityGroups</code> <br />+ <code>DBSubnetGroupName</code> <br />+ <code>Engine</code> <br />+ <code>EngineVersion</code> <br />+ <code>Iops</code> <br />+ <code>LicenseModel</code> <br />+ <code>MasterUsername</code> <br />+ <code>MasterUserPassword</code> <br />+ <code>MultiAZ</code> <br />+ <code>OptionGroupName</code> <br />+ <code>PreferredBackupWindow</code> <br />+ <code>PreferredMaintenanceWindow</code> <br /><br />All other properties are ignored. Specify a virtual private cloud (VPC) security group if you want to submit other properties, such as <code>StorageType</code>, <code>StorageEncrypted</code>, or <code>KmsKeyId</code>. If you're already using the <code>DBSecurityGroups</code> property, you can't use these other properties by updating your DB instance to use a VPC security group. You must recreate the DB instance.</td></tr>
<tr><td><CopyableCode code="master_username" /></td><td><code>string</code></td><td>The master user name for the DB instance.<br />If you specify the <code>SourceDBInstanceIdentifier</code> or <code>DBSnapshotIdentifier</code> property, don't specify this property. The value is inherited from the source DB instance or snapshot.<br />When migrating a self-managed Db2 database, we recommend that you use the same master username as your self-managed Db2 instance name.<br />*Amazon Aurora* <br />Not applicable. The name for the master user is managed by the DB cluster. <br />*RDS for Db2* <br />Constraints:<br />+ Must be 1 to 16 letters or numbers.<br />+ First character must be a letter.<br />+ Can't be a reserved word for the chosen database engine.<br /><br />*RDS for MariaDB* <br />Constraints:<br />+ Must be 1 to 16 letters or numbers.<br />+ Can't be a reserved word for the chosen database engine.<br /><br />*RDS for Microsoft SQL Server* <br />Constraints:<br />+ Must be 1 to 128 letters or numbers.<br />+ First character must be a letter.<br />+ Can't be a reserved word for the chosen database engine.<br /><br />*RDS for MySQL* <br />Constraints:<br />+ Must be 1 to 16 letters or numbers.<br />+ First character must be a letter.<br />+ Can't be a reserved word for the chosen database engine.<br /><br />*RDS for Oracle* <br />Constraints:<br />+ Must be 1 to 30 letters or numbers.<br />+ First character must be a letter.<br />+ Can't be a reserved word for the chosen database engine.<br /><br />*RDS for PostgreSQL* <br />Constraints:<br />+ Must be 1 to 63 letters or numbers.<br />+ First character must be a letter.<br />+ Can't be a reserved word for the chosen database engine.</td></tr>
<tr><td><CopyableCode code="max_allocated_storage" /></td><td><code>integer</code></td><td>The upper limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance.<br />For more information about this setting, including limitations that apply to it, see &#91;Managing capacity automatically with Amazon RDS storage autoscaling&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling) in the *Amazon RDS User Guide*.<br />This setting doesn't apply to the following DB instances:<br />+ Amazon Aurora (Storage is managed by the DB cluster.)<br />+ RDS Custom</td></tr>
<tr><td><CopyableCode code="promotion_tier" /></td><td><code>integer</code></td><td>The order of priority in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. For more information, see &#91;Fault Tolerance for an Aurora DB Cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance) in the *Amazon Aurora User Guide*.<br />This setting doesn't apply to RDS Custom DB instances.<br />Default: <code>1</code> <br />Valid Values: <code>0 - 15</code></td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address. <br />The default behavior value depends on your VPC setup and the database subnet group. For more information, see the <code>PubliclyAccessible</code> parameter in the &#91;CreateDBInstance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) in the *Amazon RDS API Reference*.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The Active Directory directory ID to create the DB instance in. Currently, only Db2, MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.<br />For more information, see &#91;Kerberos Authentication&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/kerberos-authentication.html) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><CopyableCode code="domain_fqdn" /></td><td><code>string</code></td><td>The fully qualified domain name (FQDN) of an Active Directory domain.<br />Constraints:<br />+ Can't be longer than 64 characters.<br /><br />Example: <code>mymanagedADtest.mymanagedAD.mydomain</code></td></tr>
<tr><td><CopyableCode code="character_set_name" /></td><td><code>string</code></td><td>For supported engines, indicates that the DB instance should be associated with the specified character set.<br />*Amazon Aurora* <br />Not applicable. The character set is managed by the DB cluster. For more information, see &#91;AWS::RDS::DBCluster&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html).</td></tr>
<tr><td><CopyableCode code="monitoring_role_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. For example, <code>arn:aws:iam:123456789012:role/emaccess</code>. For information on creating a monitoring role, see &#91;Setting Up and Enabling Enhanced Monitoring&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.Enabling) in the *Amazon RDS User Guide*.<br />If <code>MonitoringInterval</code> is set to a value other than <code>0</code>, then you must supply a <code>MonitoringRoleArn</code> value.<br />This setting doesn't apply to RDS Custom DB instances.</td></tr>
<tr><td><CopyableCode code="associated_roles" /></td><td><code>array</code></td><td>The IAMlong (IAM) roles associated with the DB instance. <br />*Amazon Aurora* <br />Not applicable. The associated roles are managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="domain_ou" /></td><td><code>string</code></td><td>The Active Directory organizational unit for your DB instance to join.<br />Constraints:<br />+ Must be in the distinguished name format.<br />+ Can't be longer than 64 characters.<br /><br />Example: <code>OU=mymanagedADtestOU,DC=mymanagedADtest,DC=mymanagedAD,DC=mydomain</code></td></tr>
<tr><td><CopyableCode code="db_cluster_snapshot_identifier" /></td><td><code>string</code></td><td>The identifier for the Multi-AZ DB cluster snapshot to restore from.<br />For more information on Multi-AZ DB clusters, see &#91;Multi-AZ DB cluster deployments&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.<br />Constraints:<br />+ Must match the identifier of an existing Multi-AZ DB cluster snapshot.<br />+ Can't be specified when <code>DBSnapshotIdentifier</code> is specified.<br />+ Must be specified when <code>DBSnapshotIdentifier</code> isn't specified.<br />+ If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the <code>DBClusterSnapshotIdentifier</code> must be the ARN of the shared snapshot.<br />+ Can't be the identifier of an Aurora DB cluster snapshot.</td></tr>
<tr><td><CopyableCode code="source_db_instance_automated_backups_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the replicated automated backups from which to restore, for example, <code>arn:aws:rds:us-east-1:123456789012:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE</code>.<br />This setting doesn't apply to RDS Custom.</td></tr>
<tr><td><CopyableCode code="processor_features" /></td><td><code>array</code></td><td>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.<br />This setting doesn't apply to Amazon Aurora or RDS Custom DB instances.</td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td>The daily time range during which automated backups are created if automated backups are enabled, using the <code>BackupRetentionPeriod</code> parameter. For more information, see &#91;Backup Window&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow) in the *Amazon RDS User Guide.* <br />Constraints:<br />+ Must be in the format <code>hh24:mi-hh24:mi</code>.<br />+ Must be in Universal Coordinated Time (UTC).<br />+ Must not conflict with the preferred maintenance window.<br />+ Must be at least 30 minutes.<br /><br />*Amazon Aurora* <br />Not applicable. The daily time range for creating automated backups is managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="restore_time" /></td><td><code>string</code></td><td>The date and time to restore from.<br />Constraints:<br />+ Must be a time in Universal Coordinated Time (UTC) format.<br />+ Must be before the latest restorable time for the DB instance.<br />+ Can't be specified if the <code>UseLatestRestorableTime</code> parameter is enabled.<br /><br />Example: <code>2009-09-07T23:45:00Z</code></td></tr>
<tr><td><CopyableCode code="certificate_rotation_restart" /></td><td><code>boolean</code></td><td>Specifies whether the DB instance is restarted when you rotate your SSL/TLS certificate.<br />By default, the DB instance is restarted when you rotate your SSL/TLS certificate. The certificate is not updated until the DB instance is restarted.<br />Set this parameter only if you are *not* using SSL/TLS to connect to the DB instance.<br />If you are using SSL/TLS to connect to the DB instance, follow the appropriate instructions for your DB engine to rotate your SSL/TLS certificate:<br />+ For more information about rotating your SSL/TLS certificate for RDS DB engines, see &#91;Rotating Your SSL/TLS Certificate.&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon RDS User Guide.* <br />+ For more information about rotating your SSL/TLS certificate for Aurora DB engines, see &#91;Rotating Your SSL/TLS Certificate&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html) in the *Amazon Aurora User Guide*.<br /><br />This setting doesn't apply to RDS Custom DB instances.</td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td>The network type of the DB instance.<br />Valid values:<br />+ <code>IPV4</code> <br />+ <code>DUAL</code> <br /><br />The network type is determined by the <code>DBSubnetGroup</code> specified for the DB instance. A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and IPv6 protocols (<code>DUAL</code>).<br />For more information, see &#91;Working with a DB instance in a VPC&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*</td></tr>
<tr><td><CopyableCode code="dedicated_log_volume" /></td><td><code>boolean</code></td><td>Indicates whether the DB instance has a dedicated log volume (DLV) enabled.</td></tr>
<tr><td><CopyableCode code="copy_tags_to_snapshot" /></td><td><code>boolean</code></td><td>Specifies whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.<br />This setting doesn't apply to Amazon Aurora DB instances. Copying tags to snapshots is managed by the DB cluster. Setting this value for an Aurora DB instance has no effect on the DB cluster setting.</td></tr>
<tr><td><CopyableCode code="domain_iam_role_name" /></td><td><code>string</code></td><td>The name of the IAM role to use when making API calls to the Directory Service.<br />This setting doesn't apply to the following DB instances:<br />+ Amazon Aurora (The domain is managed by the DB cluster.)<br />+ RDS Custom</td></tr>
<tr><td><CopyableCode code="replica_mode" /></td><td><code>string</code></td><td>The open mode of an Oracle read replica. For more information, see &#91;Working with Oracle Read Replicas for Amazon RDS&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the *Amazon RDS User Guide*.<br />This setting is only supported in RDS for Oracle.<br />Default: <code>open-read-only</code> <br />Valid Values: <code>open-read-only</code> or <code>mounted</code></td></tr>
<tr><td><CopyableCode code="license_model" /></td><td><code>string</code></td><td>License model information for this DB instance.<br />Valid Values:<br />+ Aurora MySQL - <code>general-public-license</code> <br />+ Aurora PostgreSQL - <code>postgresql-license</code> <br />+ RDS for Db2 - <code>bring-your-own-license</code>. For more information about RDS for Db2 licensing, see &#91;&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html) in the *Amazon RDS User Guide.* <br />+ RDS for MariaDB - <code>general-public-license</code> <br />+ RDS for Microsoft SQL Server - <code>license-included</code> <br />+ RDS for MySQL - <code>general-public-license</code> <br />+ RDS for Oracle - <code>bring-your-own-license</code> or <code>license-included</code> <br />+ RDS for PostgreSQL - <code>postgresql-license</code> <br /><br />If you've specified <code>DBSecurityGroups</code> and then you update the license model, AWS CloudFormation replaces the underlying DB instance. This will incur some interruptions to database availability.</td></tr>
<tr><td><CopyableCode code="domain_dns_ips" /></td><td><code>array</code></td><td>The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.<br />Constraints:<br />+ Two IP addresses must be provided. If there isn't a secondary domain controller, use the IP address of the primary domain controller for both entries in the list.<br /><br />Example: <code>123.124.125.126,234.235.236.237</code></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).<br />Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> <br />The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see &#91;Adjusting the Preferred DB Instance Maintenance Window&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#AdjustingTheMaintenanceWindow) in the *Amazon RDS User Guide.* <br />This property applies when AWS CloudFormation initially creates the DB instance. If you use AWS CloudFormation to update the DB instance, those updates are applied immediately.<br />Constraints: Minimum 30-minute window.</td></tr>
<tr><td><CopyableCode code="iops" /></td><td><code>integer</code></td><td>The number of I/O operations per second (IOPS) that the database provisions. The value must be equal to or greater than 1000. <br />If you specify this property, you must follow the range of allowed ratios of your requested IOPS rate to the amount of storage that you allocate (IOPS to allocated storage). For example, you can provision an Oracle database instance with 1000 IOPS and 200 GiB of storage (a ratio of 5:1), or specify 2000 IOPS with 200 GiB of storage (a ratio of 10:1). For more information, see &#91;Amazon RDS Provisioned IOPS Storage to Improve Performance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/DeveloperGuide/CHAP_Storage.html#USER_PIOPS) in the *Amazon RDS User Guide*.<br />If you specify <code>io1</code> for the <code>StorageType</code> property, then you must also specify the <code>Iops</code> property.<br />Constraints:<br />+ For RDS for Db2, MariaDB, MySQL, Oracle, and PostgreSQL - Must be a multiple between .5 and 50 of the storage amount for the DB instance.<br />+ For RDS for SQL Server - Must be a multiple between 1 and 50 of the storage amount for the DB instance.</td></tr>
<tr><td><CopyableCode code="source_region" /></td><td><code>string</code></td><td>The ID of the region that contains the source DB instance for the read replica.</td></tr>
<tr><td><CopyableCode code="use_latest_restorable_time" /></td><td><code>boolean</code></td><td>Specifies whether the DB instance is restored from the latest backup time. By default, the DB instance isn't restored from the latest backup time.<br />Constraints:<br />+ Can't be specified if the <code>RestoreTime</code> parameter is provided.</td></tr>
<tr><td><CopyableCode code="ca_certificate_identifier" /></td><td><code>string</code></td><td>The identifier of the CA certificate for this DB instance.<br />For more information, see &#91;Using SSL/TLS to encrypt a connection to a DB instance&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and &#91;Using SSL/TLS to encrypt a connection to a DB cluster&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.</td></tr>
<tr><td><CopyableCode code="manage_master_user_password" /></td><td><code>boolean</code></td><td>Specifies whether to manage the master user password with AWS Secrets Manager.<br />For more information, see &#91;Password management with Secrets Manager&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide.* <br />Constraints:<br />+ Can't manage the master user password with AWS Secrets Manager if <code>MasterUserPassword</code> is specified.</td></tr>
<tr><td><CopyableCode code="source_dbi_resource_id" /></td><td><code>string</code></td><td>The resource ID of the source DB instance from which to restore.</td></tr>
<tr><td><CopyableCode code="domain_auth_secret_arn" /></td><td><code>string</code></td><td>The ARN for the Secrets Manager secret with the credentials for the user joining the domain.<br />Example: <code>arn:aws:secretsmanager:region:account-number:secret:myselfmanagedADtestsecret-123456</code></td></tr>
<tr><td><CopyableCode code="automatic_backup_replication_region" /></td><td><code>string</code></td><td>The destination region for the backup replication of the DB instance. For more info, see &#91;Replicating automated backups to another Region&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><CopyableCode code="vpc_security_groups" /></td><td><code>array</code></td><td>A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to &#91;AWS::EC2::SecurityGroup&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html) resources created in the template.<br />If you plan to update the resource, don't specify VPC security groups in a shared VPC.<br />If you set <code>VPCSecurityGroups</code>, you must not set &#91;DBSecurityGroups&#93;(https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups), and vice versa.<br />You can migrate a DB instance in your stack from an RDS DB security group to a VPC security group, but keep the following in mind:<br />+ You can't revert to using an RDS security group after you establish a VPC security group membership.<br />+ When you migrate your DB instance to VPC security groups, if your stack update rolls back because the DB instance update fails or because an update fails in another AWS CloudFormation resource, the rollback fails because it can't revert to an RDS security group.<br />+ To use the properties that are available when you use a VPC security group, you must recreate the DB instance. If you don't, AWS CloudFormation submits only the property values that are listed in the &#91;DBSecurityGroups&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups) property.<br /><br />To avoid this situation, migrate your DB instance to using VPC security groups only when that is the only change in your stack template. <br />*Amazon Aurora* <br />Not applicable. The associated list of EC2 VPC security groups is managed by the DB cluster. If specified, the setting must match the DB cluster setting.</td></tr>
<tr><td><CopyableCode code="allow_major_version_upgrade" /></td><td><code>boolean</code></td><td>A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.<br />Constraints: Major version upgrades must be allowed when specifying a value for the <code>EngineVersion</code> parameter that is a different major version than the DB instance's current version.</td></tr>
<tr><td><CopyableCode code="db_name" /></td><td><code>string</code></td><td>The meaning of this parameter differs according to the database engine you use.<br />If you specify the <code>DBSnapshotIdentifier</code> property, this property only applies to RDS for Oracle.<br />*Amazon Aurora* <br />Not applicable. The database name is managed by the DB cluster.<br />*Db2* <br />The name of the database to create when the DB instance is created. If this parameter isn't specified, no database is created in the DB instance.<br />Constraints:<br />+ Must contain 1 to 64 letters or numbers.<br />+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).<br />+ Can't be a word reserved by the specified database engine.<br /><br />*MySQL* <br />The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.<br />Constraints:<br />+ Must contain 1 to 64 letters or numbers.<br />+ Can't be a word reserved by the specified database engine<br /><br />*MariaDB* <br />The name of the database to create when the DB instance is created. If this parameter is not specified, no database is created in the DB instance.<br />Constraints:<br />+ Must contain 1 to 64 letters or numbers.<br />+ Can't be a word reserved by the specified database engine<br /><br />*PostgreSQL* <br />The name of the database to create when the DB instance is created. If this parameter is not specified, the default <code>postgres</code> database is created in the DB instance.<br />Constraints:<br />+ Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0-9).<br />+ Must contain 1 to 63 characters.<br />+ Can't be a word reserved by the specified database engine<br /><br />*Oracle* <br />The Oracle System ID (SID) of the created DB instance. If you specify <code>null</code>, the default value <code>ORCL</code> is used. You can't specify the string NULL, or any other reserved word, for <code>DBName</code>. <br />Default: <code>ORCL</code> <br />Constraints:<br />+ Can't be longer than 8 characters<br /><br />*SQL Server* <br />Not applicable. Must be null.</td></tr>
<tr><td><CopyableCode code="enable_iam_database_authentication" /></td><td><code>boolean</code></td><td>A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.<br />This property is supported for RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL. For more information, see &#91;IAM Database Authentication for MariaDB, MySQL, and PostgreSQL&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) in the *Amazon RDS User Guide.* <br />*Amazon Aurora* <br />Not applicable. Mapping AWS IAM accounts to database accounts is managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="backup_retention_period" /></td><td><code>integer</code></td><td>The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.<br />*Amazon Aurora* <br />Not applicable. The retention period for automated backups is managed by the DB cluster.<br />Default: 1<br />Constraints:<br />+ Must be a value from 0 to 35<br />+ Can't be set to 0 if the DB instance is a source to read replicas</td></tr>
<tr><td><CopyableCode code="custom_iam_instance_profile" /></td><td><code>string</code></td><td>The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance.<br />This setting is required for RDS Custom.<br />Constraints:<br />+ The profile must exist in your account.<br />+ The profile must have an IAM role that Amazon EC2 has permissions to assume.<br />+ The instance profile name and the associated IAM role name must start with the prefix <code>AWSRDSCustom</code>.<br /><br />For the list of permissions required for the IAM role, see &#91;Configure IAM and your VPC&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html#custom-setup-orcl.iam-vpc) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><CopyableCode code="db_snapshot_identifier" /></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the DB snapshot that's used to restore the DB instance. If you're restoring from a shared manual DB snapshot, you must specify the ARN of the snapshot.<br />By specifying this property, you can create a DB instance from the specified DB snapshot. If the <code>DBSnapshotIdentifier</code> property is an empty string or the <code>AWS::RDS::DBInstance</code> declaration has no <code>DBSnapshotIdentifier</code> property, AWS CloudFormation creates a new database. If the property contains a value (other than an empty string), AWS CloudFormation creates a database from the specified snapshot. If a snapshot with the specified name doesn't exist, AWS CloudFormation can't create the database and it rolls back the stack.<br />Some DB instance properties aren't valid when you restore from a snapshot, such as the <code>MasterUsername</code> and <code>MasterUserPassword</code> properties. For information about the properties that you can specify, see the <code>RestoreDBInstanceFromDBSnapshot</code> action in the *Amazon RDS API Reference*.<br />After you restore a DB instance with a <code>DBSnapshotIdentifier</code> property, you must specify the same <code>DBSnapshotIdentifier</code> property for any future updates to the DB instance. When you specify this property for an update, the DB instance is not restored from the DB snapshot again, and the data in the database is not changed. However, if you don't specify the <code>DBSnapshotIdentifier</code> property, an empty DB instance is created, and the original DB instance is deleted. If you specify a property that is different from the previous snapshot restore property, a new DB instance is restored from the specified <code>DBSnapshotIdentifier</code> property, and the original DB instance is deleted.<br />If you specify the <code>DBSnapshotIdentifier</code> property to restore a DB instance (as opposed to specifying it for DB instance updates), then don't specify the following properties:<br />+ <code>CharacterSetName</code> <br />+ <code>DBClusterIdentifier</code> <br />+ <code>DBName</code> <br />+ <code>DeleteAutomatedBackups</code> <br />+ <code>EnablePerformanceInsights</code> <br />+ <code>KmsKeyId</code> <br />+ <code>MasterUsername</code> <br />+ <code>MasterUserPassword</code> <br />+ <code>PerformanceInsightsKMSKeyId</code> <br />+ <code>PerformanceInsightsRetentionPeriod</code> <br />+ <code>PromotionTier</code> <br />+ <code>SourceDBInstanceIdentifier</code> <br />+ <code>SourceRegion</code> <br />+ <code>StorageEncrypted</code> (for an encrypted snapshot)<br />+ <code>Timezone</code> <br /><br />*Amazon Aurora* <br />Not applicable. Snapshot restore is managed by the DB cluster.</td></tr>
<tr><td><CopyableCode code="enable_cloudwatch_logs_exports" /></td><td><code>array</code></td><td>The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see &#91;Publishing Database Logs to Amazon CloudWatch Logs&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch) in the *Amazon Relational Database Service User Guide*.<br />*Amazon Aurora* <br />Not applicable. CloudWatch Logs exports are managed by the DB cluster. <br />*Db2* <br />Valid values: <code>diag.log</code>, <code>notify.log</code> <br />*MariaDB* <br />Valid values: <code>audit</code>, <code>error</code>, <code>general</code>, <code>slowquery</code> <br />*Microsoft SQL Server* <br />Valid values: <code>agent</code>, <code>error</code> <br />*MySQL* <br />Valid values: <code>audit</code>, <code>error</code>, <code>general</code>, <code>slowquery</code> <br />*Oracle* <br />Valid values: <code>alert</code>, <code>audit</code>, <code>listener</code>, <code>trace</code>, <code>oemagent</code> <br />*PostgreSQL* <br />Valid values: <code>postgresql</code>, <code>upgrade</code></td></tr>
<tr><td><CopyableCode code="use_default_processor_features" /></td><td><code>boolean</code></td><td>Specifies whether the DB instance class of the DB instance uses its default processor features.<br />This setting doesn't apply to RDS Custom DB instances.</td></tr>
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
Gets all <code>db_instances</code> in a region.
```sql
SELECT
region,
storage_encrypted,
timezone,
db_system_id,
certificate_details,
port,
db_cluster_identifier,
storage_throughput,
dbi_resource_id,
monitoring_interval,
db_parameter_group_name,
db_instance_arn,
endpoint,
tde_credential_arn,
automatic_backup_replication_kms_key_id,
multi_az,
engine,
tags,
performance_insights_kms_key_id,
tde_credential_password,
source_db_instance_identifier,
engine_version,
storage_type,
kms_key_id,
db_instance_class,
delete_automated_backups,
performance_insights_retention_period,
availability_zone,
option_group_name,
enable_performance_insights,
auto_minor_version_upgrade,
db_subnet_group_name,
deletion_protection,
db_instance_identifier,
allocated_storage,
master_user_password,
master_user_secret,
nchar_character_set_name,
source_db_cluster_identifier,
db_security_groups,
master_username,
max_allocated_storage,
promotion_tier,
publicly_accessible,
domain,
domain_fqdn,
character_set_name,
monitoring_role_arn,
associated_roles,
domain_ou,
db_cluster_snapshot_identifier,
source_db_instance_automated_backups_arn,
processor_features,
preferred_backup_window,
restore_time,
certificate_rotation_restart,
network_type,
dedicated_log_volume,
copy_tags_to_snapshot,
domain_iam_role_name,
replica_mode,
license_model,
domain_dns_ips,
preferred_maintenance_window,
iops,
source_region,
use_latest_restorable_time,
ca_certificate_identifier,
manage_master_user_password,
source_dbi_resource_id,
domain_auth_secret_arn,
automatic_backup_replication_region,
vpc_security_groups,
allow_major_version_upgrade,
db_name,
enable_iam_database_authentication,
backup_retention_period,
custom_iam_instance_profile,
db_snapshot_identifier,
enable_cloudwatch_logs_exports,
use_default_processor_features
FROM aws.rds.db_instances
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_instance</code>.
```sql
SELECT
region,
storage_encrypted,
timezone,
db_system_id,
certificate_details,
port,
db_cluster_identifier,
storage_throughput,
dbi_resource_id,
monitoring_interval,
db_parameter_group_name,
db_instance_arn,
endpoint,
tde_credential_arn,
automatic_backup_replication_kms_key_id,
multi_az,
engine,
tags,
performance_insights_kms_key_id,
tde_credential_password,
source_db_instance_identifier,
engine_version,
storage_type,
kms_key_id,
db_instance_class,
delete_automated_backups,
performance_insights_retention_period,
availability_zone,
option_group_name,
enable_performance_insights,
auto_minor_version_upgrade,
db_subnet_group_name,
deletion_protection,
db_instance_identifier,
allocated_storage,
master_user_password,
master_user_secret,
nchar_character_set_name,
source_db_cluster_identifier,
db_security_groups,
master_username,
max_allocated_storage,
promotion_tier,
publicly_accessible,
domain,
domain_fqdn,
character_set_name,
monitoring_role_arn,
associated_roles,
domain_ou,
db_cluster_snapshot_identifier,
source_db_instance_automated_backups_arn,
processor_features,
preferred_backup_window,
restore_time,
certificate_rotation_restart,
network_type,
dedicated_log_volume,
copy_tags_to_snapshot,
domain_iam_role_name,
replica_mode,
license_model,
domain_dns_ips,
preferred_maintenance_window,
iops,
source_region,
use_latest_restorable_time,
ca_certificate_identifier,
manage_master_user_password,
source_dbi_resource_id,
domain_auth_secret_arn,
automatic_backup_replication_region,
vpc_security_groups,
allow_major_version_upgrade,
db_name,
enable_iam_database_authentication,
backup_retention_period,
custom_iam_instance_profile,
db_snapshot_identifier,
enable_cloudwatch_logs_exports,
use_default_processor_features
FROM aws.rds.db_instances
WHERE region = 'us-east-1' AND data__Identifier = '<DBInstanceIdentifier>';
```

## `INSERT` example

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
 StorageEncrypted,
 Timezone,
 CertificateDetails,
 Port,
 DBClusterIdentifier,
 StorageThroughput,
 MonitoringInterval,
 DBParameterGroupName,
 Endpoint,
 TdeCredentialArn,
 AutomaticBackupReplicationKmsKeyId,
 MultiAZ,
 Engine,
 Tags,
 PerformanceInsightsKMSKeyId,
 TdeCredentialPassword,
 SourceDBInstanceIdentifier,
 EngineVersion,
 StorageType,
 KmsKeyId,
 DBInstanceClass,
 DeleteAutomatedBackups,
 PerformanceInsightsRetentionPeriod,
 AvailabilityZone,
 OptionGroupName,
 EnablePerformanceInsights,
 AutoMinorVersionUpgrade,
 DBSubnetGroupName,
 DeletionProtection,
 DBInstanceIdentifier,
 AllocatedStorage,
 MasterUserPassword,
 MasterUserSecret,
 NcharCharacterSetName,
 SourceDBClusterIdentifier,
 DBSecurityGroups,
 MasterUsername,
 MaxAllocatedStorage,
 PromotionTier,
 PubliclyAccessible,
 Domain,
 DomainFqdn,
 CharacterSetName,
 MonitoringRoleArn,
 AssociatedRoles,
 DomainOu,
 DBClusterSnapshotIdentifier,
 SourceDBInstanceAutomatedBackupsArn,
 ProcessorFeatures,
 PreferredBackupWindow,
 RestoreTime,
 CertificateRotationRestart,
 NetworkType,
 DedicatedLogVolume,
 CopyTagsToSnapshot,
 DomainIAMRoleName,
 ReplicaMode,
 LicenseModel,
 DomainDnsIps,
 PreferredMaintenanceWindow,
 Iops,
 SourceRegion,
 UseLatestRestorableTime,
 CACertificateIdentifier,
 ManageMasterUserPassword,
 SourceDbiResourceId,
 DomainAuthSecretArn,
 AutomaticBackupReplicationRegion,
 VPCSecurityGroups,
 AllowMajorVersionUpgrade,
 DBName,
 EnableIAMDatabaseAuthentication,
 BackupRetentionPeriod,
 CustomIAMInstanceProfile,
 DBSnapshotIdentifier,
 EnableCloudwatchLogsExports,
 UseDefaultProcessorFeatures,
 region
)
SELECT 
'{{ StorageEncrypted }}',
 '{{ Timezone }}',
 '{{ CertificateDetails }}',
 '{{ Port }}',
 '{{ DBClusterIdentifier }}',
 '{{ StorageThroughput }}',
 '{{ MonitoringInterval }}',
 '{{ DBParameterGroupName }}',
 '{{ Endpoint }}',
 '{{ TdeCredentialArn }}',
 '{{ AutomaticBackupReplicationKmsKeyId }}',
 '{{ MultiAZ }}',
 '{{ Engine }}',
 '{{ Tags }}',
 '{{ PerformanceInsightsKMSKeyId }}',
 '{{ TdeCredentialPassword }}',
 '{{ SourceDBInstanceIdentifier }}',
 '{{ EngineVersion }}',
 '{{ StorageType }}',
 '{{ KmsKeyId }}',
 '{{ DBInstanceClass }}',
 '{{ DeleteAutomatedBackups }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ AvailabilityZone }}',
 '{{ OptionGroupName }}',
 '{{ EnablePerformanceInsights }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ DBInstanceIdentifier }}',
 '{{ AllocatedStorage }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ NcharCharacterSetName }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ DBSecurityGroups }}',
 '{{ MasterUsername }}',
 '{{ MaxAllocatedStorage }}',
 '{{ PromotionTier }}',
 '{{ PubliclyAccessible }}',
 '{{ Domain }}',
 '{{ DomainFqdn }}',
 '{{ CharacterSetName }}',
 '{{ MonitoringRoleArn }}',
 '{{ AssociatedRoles }}',
 '{{ DomainOu }}',
 '{{ DBClusterSnapshotIdentifier }}',
 '{{ SourceDBInstanceAutomatedBackupsArn }}',
 '{{ ProcessorFeatures }}',
 '{{ PreferredBackupWindow }}',
 '{{ RestoreTime }}',
 '{{ CertificateRotationRestart }}',
 '{{ NetworkType }}',
 '{{ DedicatedLogVolume }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DomainIAMRoleName }}',
 '{{ ReplicaMode }}',
 '{{ LicenseModel }}',
 '{{ DomainDnsIps }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ Iops }}',
 '{{ SourceRegion }}',
 '{{ UseLatestRestorableTime }}',
 '{{ CACertificateIdentifier }}',
 '{{ ManageMasterUserPassword }}',
 '{{ SourceDbiResourceId }}',
 '{{ DomainAuthSecretArn }}',
 '{{ AutomaticBackupReplicationRegion }}',
 '{{ VPCSecurityGroups }}',
 '{{ AllowMajorVersionUpgrade }}',
 '{{ DBName }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CustomIAMInstanceProfile }}',
 '{{ DBSnapshotIdentifier }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ UseDefaultProcessorFeatures }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_instances (
 StorageEncrypted,
 Timezone,
 CertificateDetails,
 Port,
 DBClusterIdentifier,
 StorageThroughput,
 MonitoringInterval,
 DBParameterGroupName,
 Endpoint,
 TdeCredentialArn,
 AutomaticBackupReplicationKmsKeyId,
 MultiAZ,
 Engine,
 Tags,
 PerformanceInsightsKMSKeyId,
 TdeCredentialPassword,
 SourceDBInstanceIdentifier,
 EngineVersion,
 StorageType,
 KmsKeyId,
 DBInstanceClass,
 DeleteAutomatedBackups,
 PerformanceInsightsRetentionPeriod,
 AvailabilityZone,
 OptionGroupName,
 EnablePerformanceInsights,
 AutoMinorVersionUpgrade,
 DBSubnetGroupName,
 DeletionProtection,
 DBInstanceIdentifier,
 AllocatedStorage,
 MasterUserPassword,
 MasterUserSecret,
 NcharCharacterSetName,
 SourceDBClusterIdentifier,
 DBSecurityGroups,
 MasterUsername,
 MaxAllocatedStorage,
 PromotionTier,
 PubliclyAccessible,
 Domain,
 DomainFqdn,
 CharacterSetName,
 MonitoringRoleArn,
 AssociatedRoles,
 DomainOu,
 DBClusterSnapshotIdentifier,
 SourceDBInstanceAutomatedBackupsArn,
 ProcessorFeatures,
 PreferredBackupWindow,
 RestoreTime,
 CertificateRotationRestart,
 NetworkType,
 DedicatedLogVolume,
 CopyTagsToSnapshot,
 DomainIAMRoleName,
 ReplicaMode,
 LicenseModel,
 DomainDnsIps,
 PreferredMaintenanceWindow,
 Iops,
 SourceRegion,
 UseLatestRestorableTime,
 CACertificateIdentifier,
 ManageMasterUserPassword,
 SourceDbiResourceId,
 DomainAuthSecretArn,
 AutomaticBackupReplicationRegion,
 VPCSecurityGroups,
 AllowMajorVersionUpgrade,
 DBName,
 EnableIAMDatabaseAuthentication,
 BackupRetentionPeriod,
 CustomIAMInstanceProfile,
 DBSnapshotIdentifier,
 EnableCloudwatchLogsExports,
 UseDefaultProcessorFeatures,
 region
)
SELECT 
 '{{ StorageEncrypted }}',
 '{{ Timezone }}',
 '{{ CertificateDetails }}',
 '{{ Port }}',
 '{{ DBClusterIdentifier }}',
 '{{ StorageThroughput }}',
 '{{ MonitoringInterval }}',
 '{{ DBParameterGroupName }}',
 '{{ Endpoint }}',
 '{{ TdeCredentialArn }}',
 '{{ AutomaticBackupReplicationKmsKeyId }}',
 '{{ MultiAZ }}',
 '{{ Engine }}',
 '{{ Tags }}',
 '{{ PerformanceInsightsKMSKeyId }}',
 '{{ TdeCredentialPassword }}',
 '{{ SourceDBInstanceIdentifier }}',
 '{{ EngineVersion }}',
 '{{ StorageType }}',
 '{{ KmsKeyId }}',
 '{{ DBInstanceClass }}',
 '{{ DeleteAutomatedBackups }}',
 '{{ PerformanceInsightsRetentionPeriod }}',
 '{{ AvailabilityZone }}',
 '{{ OptionGroupName }}',
 '{{ EnablePerformanceInsights }}',
 '{{ AutoMinorVersionUpgrade }}',
 '{{ DBSubnetGroupName }}',
 '{{ DeletionProtection }}',
 '{{ DBInstanceIdentifier }}',
 '{{ AllocatedStorage }}',
 '{{ MasterUserPassword }}',
 '{{ MasterUserSecret }}',
 '{{ NcharCharacterSetName }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ DBSecurityGroups }}',
 '{{ MasterUsername }}',
 '{{ MaxAllocatedStorage }}',
 '{{ PromotionTier }}',
 '{{ PubliclyAccessible }}',
 '{{ Domain }}',
 '{{ DomainFqdn }}',
 '{{ CharacterSetName }}',
 '{{ MonitoringRoleArn }}',
 '{{ AssociatedRoles }}',
 '{{ DomainOu }}',
 '{{ DBClusterSnapshotIdentifier }}',
 '{{ SourceDBInstanceAutomatedBackupsArn }}',
 '{{ ProcessorFeatures }}',
 '{{ PreferredBackupWindow }}',
 '{{ RestoreTime }}',
 '{{ CertificateRotationRestart }}',
 '{{ NetworkType }}',
 '{{ DedicatedLogVolume }}',
 '{{ CopyTagsToSnapshot }}',
 '{{ DomainIAMRoleName }}',
 '{{ ReplicaMode }}',
 '{{ LicenseModel }}',
 '{{ DomainDnsIps }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ Iops }}',
 '{{ SourceRegion }}',
 '{{ UseLatestRestorableTime }}',
 '{{ CACertificateIdentifier }}',
 '{{ ManageMasterUserPassword }}',
 '{{ SourceDbiResourceId }}',
 '{{ DomainAuthSecretArn }}',
 '{{ AutomaticBackupReplicationRegion }}',
 '{{ VPCSecurityGroups }}',
 '{{ AllowMajorVersionUpgrade }}',
 '{{ DBName }}',
 '{{ EnableIAMDatabaseAuthentication }}',
 '{{ BackupRetentionPeriod }}',
 '{{ CustomIAMInstanceProfile }}',
 '{{ DBSnapshotIdentifier }}',
 '{{ EnableCloudwatchLogsExports }}',
 '{{ UseDefaultProcessorFeatures }}',
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
      - name: StorageEncrypted
        value: '{{ StorageEncrypted }}'
      - name: Timezone
        value: '{{ Timezone }}'
      - name: CertificateDetails
        value:
          ValidTill: '{{ ValidTill }}'
          CAIdentifier: '{{ CAIdentifier }}'
      - name: Port
        value: '{{ Port }}'
      - name: DBClusterIdentifier
        value: '{{ DBClusterIdentifier }}'
      - name: StorageThroughput
        value: '{{ StorageThroughput }}'
      - name: MonitoringInterval
        value: '{{ MonitoringInterval }}'
      - name: DBParameterGroupName
        value: '{{ DBParameterGroupName }}'
      - name: Endpoint
        value:
          Address: '{{ Address }}'
          Port: '{{ Port }}'
          HostedZoneId: '{{ HostedZoneId }}'
      - name: TdeCredentialArn
        value: '{{ TdeCredentialArn }}'
      - name: AutomaticBackupReplicationKmsKeyId
        value: '{{ AutomaticBackupReplicationKmsKeyId }}'
      - name: MultiAZ
        value: '{{ MultiAZ }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: PerformanceInsightsKMSKeyId
        value: '{{ PerformanceInsightsKMSKeyId }}'
      - name: TdeCredentialPassword
        value: '{{ TdeCredentialPassword }}'
      - name: SourceDBInstanceIdentifier
        value: '{{ SourceDBInstanceIdentifier }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: StorageType
        value: '{{ StorageType }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: DBInstanceClass
        value: '{{ DBInstanceClass }}'
      - name: DeleteAutomatedBackups
        value: '{{ DeleteAutomatedBackups }}'
      - name: PerformanceInsightsRetentionPeriod
        value: '{{ PerformanceInsightsRetentionPeriod }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: OptionGroupName
        value: '{{ OptionGroupName }}'
      - name: EnablePerformanceInsights
        value: '{{ EnablePerformanceInsights }}'
      - name: AutoMinorVersionUpgrade
        value: '{{ AutoMinorVersionUpgrade }}'
      - name: DBSubnetGroupName
        value: '{{ DBSubnetGroupName }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: DBInstanceIdentifier
        value: '{{ DBInstanceIdentifier }}'
      - name: AllocatedStorage
        value: '{{ AllocatedStorage }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: MasterUserSecret
        value:
          SecretArn: '{{ SecretArn }}'
          KmsKeyId: '{{ KmsKeyId }}'
      - name: NcharCharacterSetName
        value: '{{ NcharCharacterSetName }}'
      - name: SourceDBClusterIdentifier
        value: '{{ SourceDBClusterIdentifier }}'
      - name: DBSecurityGroups
        value:
          - '{{ DBSecurityGroups[0] }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MaxAllocatedStorage
        value: '{{ MaxAllocatedStorage }}'
      - name: PromotionTier
        value: '{{ PromotionTier }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: DomainFqdn
        value: '{{ DomainFqdn }}'
      - name: CharacterSetName
        value: '{{ CharacterSetName }}'
      - name: MonitoringRoleArn
        value: '{{ MonitoringRoleArn }}'
      - name: AssociatedRoles
        value:
          - RoleArn: '{{ RoleArn }}'
            FeatureName: '{{ FeatureName }}'
      - name: DomainOu
        value: '{{ DomainOu }}'
      - name: DBClusterSnapshotIdentifier
        value: '{{ DBClusterSnapshotIdentifier }}'
      - name: SourceDBInstanceAutomatedBackupsArn
        value: '{{ SourceDBInstanceAutomatedBackupsArn }}'
      - name: ProcessorFeatures
        value:
          - Value: '{{ Value }}'
            Name: '{{ Name }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: RestoreTime
        value: '{{ RestoreTime }}'
      - name: CertificateRotationRestart
        value: '{{ CertificateRotationRestart }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
      - name: DedicatedLogVolume
        value: '{{ DedicatedLogVolume }}'
      - name: CopyTagsToSnapshot
        value: '{{ CopyTagsToSnapshot }}'
      - name: DomainIAMRoleName
        value: '{{ DomainIAMRoleName }}'
      - name: ReplicaMode
        value: '{{ ReplicaMode }}'
      - name: LicenseModel
        value: '{{ LicenseModel }}'
      - name: DomainDnsIps
        value:
          - '{{ DomainDnsIps[0] }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: Iops
        value: '{{ Iops }}'
      - name: SourceRegion
        value: '{{ SourceRegion }}'
      - name: UseLatestRestorableTime
        value: '{{ UseLatestRestorableTime }}'
      - name: CACertificateIdentifier
        value: '{{ CACertificateIdentifier }}'
      - name: ManageMasterUserPassword
        value: '{{ ManageMasterUserPassword }}'
      - name: SourceDbiResourceId
        value: '{{ SourceDbiResourceId }}'
      - name: DomainAuthSecretArn
        value: '{{ DomainAuthSecretArn }}'
      - name: AutomaticBackupReplicationRegion
        value: '{{ AutomaticBackupReplicationRegion }}'
      - name: VPCSecurityGroups
        value:
          - '{{ VPCSecurityGroups[0] }}'
      - name: AllowMajorVersionUpgrade
        value: '{{ AllowMajorVersionUpgrade }}'
      - name: DBName
        value: '{{ DBName }}'
      - name: EnableIAMDatabaseAuthentication
        value: '{{ EnableIAMDatabaseAuthentication }}'
      - name: BackupRetentionPeriod
        value: '{{ BackupRetentionPeriod }}'
      - name: CustomIAMInstanceProfile
        value: '{{ CustomIAMInstanceProfile }}'
      - name: DBSnapshotIdentifier
        value: '{{ DBSnapshotIdentifier }}'
      - name: EnableCloudwatchLogsExports
        value:
          - '{{ EnableCloudwatchLogsExports[0] }}'
      - name: UseDefaultProcessorFeatures
        value: '{{ UseDefaultProcessorFeatures }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rds.db_instances
WHERE data__Identifier = '<DBInstanceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_instances</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
rds:DescribeDBInstances
```

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

### Update
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
rds:DescribeDBClusters,
rds:DescribeDBEngineVersions,
rds:DescribeDBInstances,
rds:DescribeDBParameterGroups,
rds:DescribeEvents,
rds:ModifyDBInstance,
rds:PromoteReadReplica,
rds:RebootDBInstance,
rds:RemoveRoleFromDBInstance,
rds:RemoveTagsFromResource,
rds:StartDBInstanceAutomatedBackupsReplication,
rds:StopDBInstanceAutomatedBackupsReplication,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### List
```json
rds:DescribeDBInstances
```

### Delete
```json
rds:CreateDBSnapshot,
rds:DeleteDBInstance,
rds:DescribeDBInstances
```

