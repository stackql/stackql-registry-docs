---
title: db_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters
  - neptune
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
<tr><td><b>Description</b></td><td>The AWS::Neptune::DBCluster resource creates an Amazon Neptune DB cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.neptune.db_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_cluster_identifier" /></td><td><code>string</code></td><td>The DB cluster identifier. Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster stored as a lowercase string.</td></tr>
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
FROM aws.neptune.db_clusters
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
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AvailabilityZones": [
  "{{ AvailabilityZones[0] }}"
 ],
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterParameterGroupName": "{{ DBClusterParameterGroupName }}",
 "DBInstanceParameterGroupName": "{{ DBInstanceParameterGroupName }}",
 "DBPort": "{{ DBPort }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EngineVersion": "{{ EngineVersion }}",
 "IamAuthEnabled": "{{ IamAuthEnabled }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "RestoreToTime": "{{ RestoreToTime }}",
 "RestoreType": "{{ RestoreType }}",
 "ServerlessScalingConfiguration": {
  "MinCapacity": null,
  "MaxCapacity": null
 },
 "SnapshotIdentifier": "{{ SnapshotIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
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
INSERT INTO aws.neptune.db_clusters (
 AssociatedRoles,
 AvailabilityZones,
 BackupRetentionPeriod,
 CopyTagsToSnapshot,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBInstanceParameterGroupName,
 DBPort,
 DBSubnetGroupName,
 DeletionProtection,
 EnableCloudwatchLogsExports,
 EngineVersion,
 IamAuthEnabled,
 KmsKeyId,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 RestoreToTime,
 RestoreType,
 ServerlessScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
{{ .AssociatedRoles }},
 {{ .AvailabilityZones }},
 {{ .BackupRetentionPeriod }},
 {{ .CopyTagsToSnapshot }},
 {{ .DBClusterIdentifier }},
 {{ .DBClusterParameterGroupName }},
 {{ .DBInstanceParameterGroupName }},
 {{ .DBPort }},
 {{ .DBSubnetGroupName }},
 {{ .DeletionProtection }},
 {{ .EnableCloudwatchLogsExports }},
 {{ .EngineVersion }},
 {{ .IamAuthEnabled }},
 {{ .KmsKeyId }},
 {{ .PreferredBackupWindow }},
 {{ .PreferredMaintenanceWindow }},
 {{ .RestoreToTime }},
 {{ .RestoreType }},
 {{ .ServerlessScalingConfiguration }},
 {{ .SnapshotIdentifier }},
 {{ .SourceDBClusterIdentifier }},
 {{ .StorageEncrypted }},
 {{ .Tags }},
 {{ .UseLatestRestorableTime }},
 {{ .VpcSecurityGroupIds }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssociatedRoles": [
  {
   "FeatureName": "{{ FeatureName }}",
   "RoleArn": "{{ RoleArn }}"
  }
 ],
 "AvailabilityZones": [
  "{{ AvailabilityZones[0] }}"
 ],
 "BackupRetentionPeriod": "{{ BackupRetentionPeriod }}",
 "CopyTagsToSnapshot": "{{ CopyTagsToSnapshot }}",
 "DBClusterIdentifier": "{{ DBClusterIdentifier }}",
 "DBClusterParameterGroupName": "{{ DBClusterParameterGroupName }}",
 "DBInstanceParameterGroupName": "{{ DBInstanceParameterGroupName }}",
 "DBPort": "{{ DBPort }}",
 "DBSubnetGroupName": "{{ DBSubnetGroupName }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "EnableCloudwatchLogsExports": [
  "{{ EnableCloudwatchLogsExports[0] }}"
 ],
 "EngineVersion": "{{ EngineVersion }}",
 "IamAuthEnabled": "{{ IamAuthEnabled }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "RestoreToTime": "{{ RestoreToTime }}",
 "RestoreType": "{{ RestoreType }}",
 "ServerlessScalingConfiguration": {
  "MinCapacity": null,
  "MaxCapacity": null
 },
 "SnapshotIdentifier": "{{ SnapshotIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "StorageEncrypted": "{{ StorageEncrypted }}",
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
INSERT INTO aws.neptune.db_clusters (
 AssociatedRoles,
 AvailabilityZones,
 BackupRetentionPeriod,
 CopyTagsToSnapshot,
 DBClusterIdentifier,
 DBClusterParameterGroupName,
 DBInstanceParameterGroupName,
 DBPort,
 DBSubnetGroupName,
 DeletionProtection,
 EnableCloudwatchLogsExports,
 EngineVersion,
 IamAuthEnabled,
 KmsKeyId,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 RestoreToTime,
 RestoreType,
 ServerlessScalingConfiguration,
 SnapshotIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 Tags,
 UseLatestRestorableTime,
 VpcSecurityGroupIds,
 region
)
SELECT 
 {{ .AssociatedRoles }},
 {{ .AvailabilityZones }},
 {{ .BackupRetentionPeriod }},
 {{ .CopyTagsToSnapshot }},
 {{ .DBClusterIdentifier }},
 {{ .DBClusterParameterGroupName }},
 {{ .DBInstanceParameterGroupName }},
 {{ .DBPort }},
 {{ .DBSubnetGroupName }},
 {{ .DeletionProtection }},
 {{ .EnableCloudwatchLogsExports }},
 {{ .EngineVersion }},
 {{ .IamAuthEnabled }},
 {{ .KmsKeyId }},
 {{ .PreferredBackupWindow }},
 {{ .PreferredMaintenanceWindow }},
 {{ .RestoreToTime }},
 {{ .RestoreType }},
 {{ .ServerlessScalingConfiguration }},
 {{ .SnapshotIdentifier }},
 {{ .SourceDBClusterIdentifier }},
 {{ .StorageEncrypted }},
 {{ .Tags }},
 {{ .UseLatestRestorableTime }},
 {{ .VpcSecurityGroupIds }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.neptune.db_clusters
WHERE data__Identifier = '<DBClusterIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_clusters</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
rds:AddRoleToDBCluster,
rds:AddTagsToResource,
rds:CreateDBCluster,
rds:CreateDBInstance,
rds:DescribeDBClusters,
rds:ListTagsForResource,
rds:ModifyDBCluster,
rds:RestoreDBClusterFromSnapshot,
rds:RestoreDBClusterToPointInTime,
kms:*
```

### Delete
```json
rds:DeleteDBCluster,
rds:DeleteDBInstance,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters,
rds:ListTagsForResource,
rds:RemoveFromGlobalCluster,
rds:CreateDBClusterSnapshot,
kms:*
```

### List
```json
rds:DescribeDBClusters,
rds:ListTagsForResource,
kms:*
```

