---
title: replication_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_configs
  - dms
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


Used to retrieve a list of <code>replication_configs</code> in a region or to create or delete a <code>replication_configs</code> resource, use <code>replication_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A replication configuration that you later provide to configure and start a AWS DMS Serverless replication</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.replication_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="replication_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
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
replication_config_arn
FROM aws.dms.replication_configs
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
 "ReplicationConfigIdentifier": "{{ ReplicationConfigIdentifier }}",
 "ReplicationConfigArn": "{{ ReplicationConfigArn }}",
 "SourceEndpointArn": "{{ SourceEndpointArn }}",
 "TargetEndpointArn": "{{ TargetEndpointArn }}",
 "ReplicationType": "{{ ReplicationType }}",
 "ComputeConfig": {
  "AvailabilityZone": "{{ AvailabilityZone }}",
  "DnsNameServers": "{{ DnsNameServers }}",
  "KmsKeyId": "{{ KmsKeyId }}",
  "MaxCapacityUnits": "{{ MaxCapacityUnits }}",
  "MinCapacityUnits": "{{ MinCapacityUnits }}",
  "MultiAZ": "{{ MultiAZ }}",
  "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
  "ReplicationSubnetGroupId": "{{ ReplicationSubnetGroupId }}",
  "VpcSecurityGroupIds": [
   "{{ VpcSecurityGroupIds[0] }}"
  ]
 },
 "ReplicationSettings": {},
 "SupplementalSettings": {},
 "ResourceIdentifier": "{{ ResourceIdentifier }}",
 "TableMappings": {},
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.dms.replication_configs (
 ReplicationConfigIdentifier,
 ReplicationConfigArn,
 SourceEndpointArn,
 TargetEndpointArn,
 ReplicationType,
 ComputeConfig,
 ReplicationSettings,
 SupplementalSettings,
 ResourceIdentifier,
 TableMappings,
 Tags,
 region
)
SELECT 
{{ ReplicationConfigIdentifier }},
 {{ ReplicationConfigArn }},
 {{ SourceEndpointArn }},
 {{ TargetEndpointArn }},
 {{ ReplicationType }},
 {{ ComputeConfig }},
 {{ ReplicationSettings }},
 {{ SupplementalSettings }},
 {{ ResourceIdentifier }},
 {{ TableMappings }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ReplicationConfigIdentifier": "{{ ReplicationConfigIdentifier }}",
 "ReplicationConfigArn": "{{ ReplicationConfigArn }}",
 "SourceEndpointArn": "{{ SourceEndpointArn }}",
 "TargetEndpointArn": "{{ TargetEndpointArn }}",
 "ReplicationType": "{{ ReplicationType }}",
 "ComputeConfig": {
  "AvailabilityZone": "{{ AvailabilityZone }}",
  "DnsNameServers": "{{ DnsNameServers }}",
  "KmsKeyId": "{{ KmsKeyId }}",
  "MaxCapacityUnits": "{{ MaxCapacityUnits }}",
  "MinCapacityUnits": "{{ MinCapacityUnits }}",
  "MultiAZ": "{{ MultiAZ }}",
  "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
  "ReplicationSubnetGroupId": "{{ ReplicationSubnetGroupId }}",
  "VpcSecurityGroupIds": [
   "{{ VpcSecurityGroupIds[0] }}"
  ]
 },
 "ReplicationSettings": {},
 "SupplementalSettings": {},
 "ResourceIdentifier": "{{ ResourceIdentifier }}",
 "TableMappings": {},
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.dms.replication_configs (
 ReplicationConfigIdentifier,
 ReplicationConfigArn,
 SourceEndpointArn,
 TargetEndpointArn,
 ReplicationType,
 ComputeConfig,
 ReplicationSettings,
 SupplementalSettings,
 ResourceIdentifier,
 TableMappings,
 Tags,
 region
)
SELECT 
 {{ ReplicationConfigIdentifier }},
 {{ ReplicationConfigArn }},
 {{ SourceEndpointArn }},
 {{ TargetEndpointArn }},
 {{ ReplicationType }},
 {{ ComputeConfig }},
 {{ ReplicationSettings }},
 {{ SupplementalSettings }},
 {{ ResourceIdentifier }},
 {{ TableMappings }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.dms.replication_configs
WHERE data__Identifier = '<ReplicationConfigArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>replication_configs</code> resource, the following permissions are required:

### Create
```json
dms:CreateReplicationConfig,
dms:AddTagsToResource,
dms:ListTagsForResource,
iam:CreateServiceLinkedRole,
iam:AttachRolePolicy,
iam:PutRolePolicy,
iam:UpdateRoleDescription
```

### List
```json
dms:DescribeReplicationConfigs,
dms:ListTagsForResource
```

### Delete
```json
dms:DescribeReplicationConfigs,
dms:DeleteReplicationConfig,
dms:ListTagsForResource,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

