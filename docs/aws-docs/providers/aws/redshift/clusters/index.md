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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>clusters</code> in a region or to create or delete a <code>clusters</code> resource, use <code>cluster</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_identifier" /></td><td><code>string</code></td><td>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account</td></tr>
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
    <td><CopyableCode code="NodeType, MasterUsername, DBName, ClusterType, region" /></td>
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
cluster_identifier
FROM aws.redshift.clusters
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshift.clusters (
 MasterUsername,
 NodeType,
 ClusterType,
 DBName,
 region
)
SELECT 
'{{ MasterUsername }}',
 '{{ NodeType }}',
 '{{ ClusterType }}',
 '{{ DBName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.clusters (
 ClusterIdentifier,
 MasterUsername,
 MasterUserPassword,
 NodeType,
 AllowVersionUpgrade,
 AutomatedSnapshotRetentionPeriod,
 AvailabilityZone,
 ClusterParameterGroupName,
 ClusterType,
 ClusterVersion,
 ClusterSubnetGroupName,
 DBName,
 ElasticIp,
 Encrypted,
 HsmClientCertificateIdentifier,
 HsmConfigurationIdentifier,
 KmsKeyId,
 NumberOfNodes,
 Port,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 ClusterSecurityGroups,
 IamRoles,
 Tags,
 VpcSecurityGroupIds,
 SnapshotClusterIdentifier,
 SnapshotIdentifier,
 OwnerAccount,
 LoggingProperties,
 Endpoint,
 DestinationRegion,
 SnapshotCopyRetentionPeriod,
 SnapshotCopyGrantName,
 ManualSnapshotRetentionPeriod,
 SnapshotCopyManual,
 AvailabilityZoneRelocation,
 AvailabilityZoneRelocationStatus,
 AquaConfigurationStatus,
 Classic,
 EnhancedVpcRouting,
 MaintenanceTrackName,
 DeferMaintenance,
 DeferMaintenanceStartTime,
 DeferMaintenanceEndTime,
 DeferMaintenanceDuration,
 RevisionTarget,
 ResourceAction,
 RotateEncryptionKey,
 MultiAZ,
 NamespaceResourcePolicy,
 ManageMasterPassword,
 MasterPasswordSecretKmsKeyId,
 region
)
SELECT 
 '{{ ClusterIdentifier }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ NodeType }}',
 '{{ AllowVersionUpgrade }}',
 '{{ AutomatedSnapshotRetentionPeriod }}',
 '{{ AvailabilityZone }}',
 '{{ ClusterParameterGroupName }}',
 '{{ ClusterType }}',
 '{{ ClusterVersion }}',
 '{{ ClusterSubnetGroupName }}',
 '{{ DBName }}',
 '{{ ElasticIp }}',
 '{{ Encrypted }}',
 '{{ HsmClientCertificateIdentifier }}',
 '{{ HsmConfigurationIdentifier }}',
 '{{ KmsKeyId }}',
 '{{ NumberOfNodes }}',
 '{{ Port }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ ClusterSecurityGroups }}',
 '{{ IamRoles }}',
 '{{ Tags }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ SnapshotClusterIdentifier }}',
 '{{ SnapshotIdentifier }}',
 '{{ OwnerAccount }}',
 '{{ LoggingProperties }}',
 '{{ Endpoint }}',
 '{{ DestinationRegion }}',
 '{{ SnapshotCopyRetentionPeriod }}',
 '{{ SnapshotCopyGrantName }}',
 '{{ ManualSnapshotRetentionPeriod }}',
 '{{ SnapshotCopyManual }}',
 '{{ AvailabilityZoneRelocation }}',
 '{{ AvailabilityZoneRelocationStatus }}',
 '{{ AquaConfigurationStatus }}',
 '{{ Classic }}',
 '{{ EnhancedVpcRouting }}',
 '{{ MaintenanceTrackName }}',
 '{{ DeferMaintenance }}',
 '{{ DeferMaintenanceStartTime }}',
 '{{ DeferMaintenanceEndTime }}',
 '{{ DeferMaintenanceDuration }}',
 '{{ RevisionTarget }}',
 '{{ ResourceAction }}',
 '{{ RotateEncryptionKey }}',
 '{{ MultiAZ }}',
 '{{ NamespaceResourcePolicy }}',
 '{{ ManageMasterPassword }}',
 '{{ MasterPasswordSecretKmsKeyId }}',
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
  - name: cluster
    props:
      - name: ClusterIdentifier
        value: '{{ ClusterIdentifier }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: NodeType
        value: '{{ NodeType }}'
      - name: AllowVersionUpgrade
        value: '{{ AllowVersionUpgrade }}'
      - name: AutomatedSnapshotRetentionPeriod
        value: '{{ AutomatedSnapshotRetentionPeriod }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: ClusterParameterGroupName
        value: '{{ ClusterParameterGroupName }}'
      - name: ClusterType
        value: '{{ ClusterType }}'
      - name: ClusterVersion
        value: '{{ ClusterVersion }}'
      - name: ClusterSubnetGroupName
        value: '{{ ClusterSubnetGroupName }}'
      - name: DBName
        value: '{{ DBName }}'
      - name: ElasticIp
        value: '{{ ElasticIp }}'
      - name: Encrypted
        value: '{{ Encrypted }}'
      - name: HsmClientCertificateIdentifier
        value: '{{ HsmClientCertificateIdentifier }}'
      - name: HsmConfigurationIdentifier
        value: '{{ HsmConfigurationIdentifier }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: NumberOfNodes
        value: '{{ NumberOfNodes }}'
      - name: Port
        value: '{{ Port }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: ClusterSecurityGroups
        value:
          - '{{ ClusterSecurityGroups[0] }}'
      - name: IamRoles
        value:
          - '{{ IamRoles[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: SnapshotClusterIdentifier
        value: '{{ SnapshotClusterIdentifier }}'
      - name: SnapshotIdentifier
        value: '{{ SnapshotIdentifier }}'
      - name: OwnerAccount
        value: '{{ OwnerAccount }}'
      - name: LoggingProperties
        value:
          BucketName: '{{ BucketName }}'
          S3KeyPrefix: '{{ S3KeyPrefix }}'
      - name: Endpoint
        value:
          Port: '{{ Port }}'
          Address: '{{ Address }}'
      - name: DestinationRegion
        value: '{{ DestinationRegion }}'
      - name: SnapshotCopyRetentionPeriod
        value: '{{ SnapshotCopyRetentionPeriod }}'
      - name: SnapshotCopyGrantName
        value: '{{ SnapshotCopyGrantName }}'
      - name: ManualSnapshotRetentionPeriod
        value: '{{ ManualSnapshotRetentionPeriod }}'
      - name: SnapshotCopyManual
        value: '{{ SnapshotCopyManual }}'
      - name: AvailabilityZoneRelocation
        value: '{{ AvailabilityZoneRelocation }}'
      - name: AvailabilityZoneRelocationStatus
        value: '{{ AvailabilityZoneRelocationStatus }}'
      - name: AquaConfigurationStatus
        value: '{{ AquaConfigurationStatus }}'
      - name: Classic
        value: '{{ Classic }}'
      - name: EnhancedVpcRouting
        value: '{{ EnhancedVpcRouting }}'
      - name: MaintenanceTrackName
        value: '{{ MaintenanceTrackName }}'
      - name: DeferMaintenance
        value: '{{ DeferMaintenance }}'
      - name: DeferMaintenanceStartTime
        value: '{{ DeferMaintenanceStartTime }}'
      - name: DeferMaintenanceEndTime
        value: '{{ DeferMaintenanceEndTime }}'
      - name: DeferMaintenanceDuration
        value: '{{ DeferMaintenanceDuration }}'
      - name: RevisionTarget
        value: '{{ RevisionTarget }}'
      - name: ResourceAction
        value: '{{ ResourceAction }}'
      - name: RotateEncryptionKey
        value: '{{ RotateEncryptionKey }}'
      - name: MultiAZ
        value: '{{ MultiAZ }}'
      - name: NamespaceResourcePolicy
        value: {}
      - name: ManageMasterPassword
        value: '{{ ManageMasterPassword }}'
      - name: MasterPasswordSecretKmsKeyId
        value: '{{ MasterPasswordSecretKmsKeyId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.redshift.clusters
WHERE data__Identifier = '<ClusterIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iam:CreateServiceLinkedRole,
redshift:DescribeClusters,
redshift:CreateCluster,
redshift:RestoreFromClusterSnapshot,
redshift:EnableLogging,
redshift:DescribeLoggingStatus,
redshift:CreateTags,
redshift:DescribeTags,
redshift:GetResourcePolicy,
redshift:PutResourcePolicy,
redshift:ModifyClusterMaintenance,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeNetworkInterfaces,
ec2:DescribeAddresses,
ec2:AssociateAddress,
ec2:CreateNetworkInterface,
ec2:ModifyNetworkInterfaceAttribute,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
ec2:ModifyVpcEndpoint,
ec2:AllocateAddress,
ec2:CreateSecurityGroup,
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroupRules,
ec2:DescribeAvailabilityZones,
ec2:DescribeNetworkAcls,
ec2:DescribeRouteTables,
cloudwatch:PutMetricData
```

### Delete
```json
redshift:DescribeTags,
redshift:DescribeClusters,
redshift:DeleteCluster
```

### List
```json
redshift:DescribeTags,
redshift:DescribeClusters
```

