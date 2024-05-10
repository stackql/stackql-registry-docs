---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - memorydb
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
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</td></tr>
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
cluster_name
FROM aws.memorydb.clusters
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
 "ClusterName": "{{ ClusterName }}",
 "NodeType": "{{ NodeType }}",
 "ACLName": "{{ ACLName }}"
}
>>>
--required properties only
INSERT INTO aws.memorydb.clusters (
 ClusterName,
 NodeType,
 ACLName,
 region
)
SELECT 
{{ .ClusterName }},
 {{ .NodeType }},
 {{ .ACLName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterName": "{{ ClusterName }}",
 "Description": "{{ Description }}",
 "NodeType": "{{ NodeType }}",
 "NumShards": "{{ NumShards }}",
 "NumReplicasPerShard": "{{ NumReplicasPerShard }}",
 "SubnetGroupName": "{{ SubnetGroupName }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "MaintenanceWindow": "{{ MaintenanceWindow }}",
 "ParameterGroupName": "{{ ParameterGroupName }}",
 "Port": "{{ Port }}",
 "SnapshotRetentionLimit": "{{ SnapshotRetentionLimit }}",
 "SnapshotWindow": "{{ SnapshotWindow }}",
 "ACLName": "{{ ACLName }}",
 "SnsTopicArn": "{{ SnsTopicArn }}",
 "SnsTopicStatus": "{{ SnsTopicStatus }}",
 "TLSEnabled": "{{ TLSEnabled }}",
 "DataTiering": "{{ DataTiering }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "SnapshotArns": [
  "{{ SnapshotArns[0] }}"
 ],
 "SnapshotName": "{{ SnapshotName }}",
 "FinalSnapshotName": "{{ FinalSnapshotName }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ClusterEndpoint": {
  "Address": "{{ Address }}",
  "Port": "{{ Port }}"
 },
 "AutoMinorVersionUpgrade": "{{ AutoMinorVersionUpgrade }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.memorydb.clusters (
 ClusterName,
 Description,
 NodeType,
 NumShards,
 NumReplicasPerShard,
 SubnetGroupName,
 SecurityGroupIds,
 MaintenanceWindow,
 ParameterGroupName,
 Port,
 SnapshotRetentionLimit,
 SnapshotWindow,
 ACLName,
 SnsTopicArn,
 SnsTopicStatus,
 TLSEnabled,
 DataTiering,
 KmsKeyId,
 SnapshotArns,
 SnapshotName,
 FinalSnapshotName,
 EngineVersion,
 ClusterEndpoint,
 AutoMinorVersionUpgrade,
 Tags,
 region
)
SELECT 
 {{ .ClusterName }},
 {{ .Description }},
 {{ .NodeType }},
 {{ .NumShards }},
 {{ .NumReplicasPerShard }},
 {{ .SubnetGroupName }},
 {{ .SecurityGroupIds }},
 {{ .MaintenanceWindow }},
 {{ .ParameterGroupName }},
 {{ .Port }},
 {{ .SnapshotRetentionLimit }},
 {{ .SnapshotWindow }},
 {{ .ACLName }},
 {{ .SnsTopicArn }},
 {{ .SnsTopicStatus }},
 {{ .TLSEnabled }},
 {{ .DataTiering }},
 {{ .KmsKeyId }},
 {{ .SnapshotArns }},
 {{ .SnapshotName }},
 {{ .FinalSnapshotName }},
 {{ .EngineVersion }},
 {{ .ClusterEndpoint }},
 {{ .AutoMinorVersionUpgrade }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.memorydb.clusters
WHERE data__Identifier = '<ClusterName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateCluster,
memorydb:DescribeClusters,
memorydb:ListTags
```

### Delete
```json
memorydb:DeleteCluster,
memorydb:DescribeClusters
```

### List
```json
memorydb:DescribeClusters
```

