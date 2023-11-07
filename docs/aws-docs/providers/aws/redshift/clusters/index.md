---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
Retrieves a list of <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>clusters</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshift.clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterIdentifier</code></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
<tr><td><code>MasterUsername</code></td><td><code>string</code></td><td>The user name associated with the master user account for the cluster that is being created. The user name can't be PUBLIC and first character must be a letter.</td></tr>
<tr><td><code>MasterUserPassword</code></td><td><code>string</code></td><td>The password associated with the master user account for the cluster that is being created. Password must be between 8 and 64 characters in length, should have at least one uppercase letter.Must contain at least one lowercase letter.Must contain one number.Can be any printable ASCII character.</td></tr>
<tr><td><code>NodeType</code></td><td><code>string</code></td><td>The node type to be provisioned for the cluster.Valid Values: ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge | dc2.large | dc2.8xlarge | ra3.4xlarge | ra3.16xlarge</td></tr>
<tr><td><code>AllowVersionUpgrade</code></td><td><code>boolean</code></td><td>Major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default value is True</td></tr>
<tr><td><code>AutomatedSnapshotRetentionPeriod</code></td><td><code>integer</code></td><td>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Default value is 1</td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td>The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint</td></tr>
<tr><td><code>ClusterParameterGroupName</code></td><td><code>string</code></td><td>The name of the parameter group to be associated with this cluster.</td></tr>
<tr><td><code>ClusterType</code></td><td><code>string</code></td><td>The type of the cluster. When cluster type is specified as single-node, the NumberOfNodes parameter is not required and if multi-node, the NumberOfNodes parameter is required</td></tr>
<tr><td><code>ClusterVersion</code></td><td><code>string</code></td><td>The version of the Amazon Redshift engine software that you want to deploy on the cluster.The version selected runs on all the nodes in the cluster.</td></tr>
<tr><td><code>ClusterSubnetGroupName</code></td><td><code>string</code></td><td>The name of a cluster subnet group to be associated with this cluster.</td></tr>
<tr><td><code>DBName</code></td><td><code>string</code></td><td>The name of the first database to be created when the cluster is created. To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database.</td></tr>
<tr><td><code>ElasticIp</code></td><td><code>string</code></td><td>The Elastic IP (EIP) address for the cluster.</td></tr>
<tr><td><code>Encrypted</code></td><td><code>boolean</code></td><td>If true, the data in the cluster is encrypted at rest.</td></tr>
<tr><td><code>HsmClientCertificateIdentifier</code></td><td><code>string</code></td><td>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM</td></tr>
<tr><td><code>HsmConfigurationIdentifier</code></td><td><code>string</code></td><td>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</td></tr>
<tr><td><code>NumberOfNodes</code></td><td><code>integer</code></td><td>The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node.</td></tr>
<tr><td><code>Port</code></td><td><code>integer</code></td><td>The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings</td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td>The weekly time range (in UTC) during which automated cluster maintenance can occur.</td></tr>
<tr><td><code>PubliclyAccessible</code></td><td><code>boolean</code></td><td>If true, the cluster can be accessed from a public network.</td></tr>
<tr><td><code>ClusterSecurityGroups</code></td><td><code>array</code></td><td>A list of security groups to be associated with this cluster.</td></tr>
<tr><td><code>IamRoles</code></td><td><code>array</code></td><td>A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 50 IAM roles in a single request</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The list of tags for the cluster parameter group.</td></tr>
<tr><td><code>VpcSecurityGroupIds</code></td><td><code>array</code></td><td>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</td></tr>
<tr><td><code>SnapshotClusterIdentifier</code></td><td><code>string</code></td><td>The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</td></tr>
<tr><td><code>SnapshotIdentifier</code></td><td><code>string</code></td><td>The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OwnerAccount</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LoggingProperties</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Endpoint</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DestinationRegion</code></td><td><code>string</code></td><td>The destination AWS Region that you want to copy snapshots to. Constraints: Must be the name of a valid AWS Region. For more information, see Regions and Endpoints in the Amazon Web Services &#91;https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;rande.html#redshift_region&#93; General Reference</td></tr>
<tr><td><code>SnapshotCopyRetentionPeriod</code></td><td><code>integer</code></td><td>The number of days to retain automated snapshots in the destination region after they are copied from the source region. &lt;br&#x2F;&gt;&lt;br&#x2F;&gt; Default is 7. &lt;br&#x2F;&gt;&lt;br&#x2F;&gt; Constraints: Must be at least 1 and no more than 35.</td></tr>
<tr><td><code>SnapshotCopyGrantName</code></td><td><code>string</code></td><td>The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.</td></tr>
<tr><td><code>ManualSnapshotRetentionPeriod</code></td><td><code>integer</code></td><td>The number of days to retain newly copied snapshots in the destination AWS Region after they are copied from the source AWS Region. If the value is -1, the manual snapshot is retained indefinitely.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The value must be either -1 or an integer between 1 and 3,653.</td></tr>
<tr><td><code>SnapshotCopyManual</code></td><td><code>boolean</code></td><td>Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.</td></tr>
<tr><td><code>AvailabilityZoneRelocation</code></td><td><code>boolean</code></td><td>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.</td></tr>
<tr><td><code>AvailabilityZoneRelocationStatus</code></td><td><code>string</code></td><td>The availability zone relocation status of the cluster</td></tr>
<tr><td><code>AquaConfigurationStatus</code></td><td><code>string</code></td><td>The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) after the cluster is restored. Possible values include the following.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;enabled - Use AQUA if it is available for the current Region and Amazon Redshift node type.&lt;br&#x2F;&gt;disabled - Don't use AQUA.&lt;br&#x2F;&gt;auto - Amazon Redshift determines whether to use AQUA.&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>Classic</code></td><td><code>boolean</code></td><td>A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to false , the resize type is elastic.</td></tr>
<tr><td><code>EnhancedVpcRouting</code></td><td><code>boolean</code></td><td>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If this option is true , enhanced VPC routing is enabled.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Default: false</td></tr>
<tr><td><code>MaintenanceTrackName</code></td><td><code>string</code></td><td>The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the PendingModifiedValues for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.</td></tr>
<tr><td><code>DeferMaintenance</code></td><td><code>boolean</code></td><td>A boolean indicating whether to enable the deferred maintenance window.</td></tr>
<tr><td><code>DeferMaintenanceIdentifier</code></td><td><code>string</code></td><td>A unique identifier for the deferred maintenance window.</td></tr>
<tr><td><code>DeferMaintenanceStartTime</code></td><td><code>string</code></td><td>A timestamp indicating the start time for the deferred maintenance window.</td></tr>
<tr><td><code>DeferMaintenanceEndTime</code></td><td><code>string</code></td><td>A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can't specify a duration.</td></tr>
<tr><td><code>DeferMaintenanceDuration</code></td><td><code>integer</code></td><td>An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 45 days or less.</td></tr>
<tr><td><code>RevisionTarget</code></td><td><code>string</code></td><td>The identifier of the database revision. You can retrieve this value from the response to the DescribeClusterDbRevisions request.</td></tr>
<tr><td><code>ResourceAction</code></td><td><code>string</code></td><td>The Redshift operation to be performed. Resource Action supports pause-cluster, resume-cluster APIs</td></tr>
<tr><td><code>RotateEncryptionKey</code></td><td><code>boolean</code></td><td>A boolean indicating if we want to rotate Encryption Keys.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.redshift.clusters<br/>WHERE region = 'us-east-1'
</pre>
