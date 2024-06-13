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

Creates, updates, deletes or gets a <code>replication_config</code> resource or lists <code>replication_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A replication configuration that you later provide to configure and start a AWS DMS Serverless replication</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.replication_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="replication_config_identifier" /></td><td><code>string</code></td><td>A unique identifier of replication configuration</td></tr>
<tr><td><CopyableCode code="replication_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
<tr><td><CopyableCode code="source_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="target_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="replication_type" /></td><td><code>string</code></td><td>The type of AWS DMS Serverless replication to provision using this replication configuration</td></tr>
<tr><td><CopyableCode code="compute_config" /></td><td><code>object</code></td><td>Configuration parameters for provisioning a AWS DMS Serverless replication</td></tr>
<tr><td><CopyableCode code="replication_settings" /></td><td><code>object</code></td><td>JSON settings for Servereless replications that are provisioned using this replication configuration</td></tr>
<tr><td><CopyableCode code="supplemental_settings" /></td><td><code>object</code></td><td>JSON settings for specifying supplemental data</td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td>A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource</td></tr>
<tr><td><CopyableCode code="table_mappings" /></td><td><code>object</code></td><td>JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td><p>Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.</p></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>replication_configs</code> in a region.
```sql
SELECT
region,
replication_config_arn
FROM aws.dms.replication_configs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>replication_config</code>.
```sql
SELECT
region,
replication_config_identifier,
replication_config_arn,
source_endpoint_arn,
target_endpoint_arn,
replication_type,
compute_config,
replication_settings,
supplemental_settings,
resource_identifier,
table_mappings,
tags
FROM aws.dms.replication_configs
WHERE region = 'us-east-1' AND data__Identifier = '<ReplicationConfigArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
'{{ ReplicationConfigIdentifier }}',
 '{{ ReplicationConfigArn }}',
 '{{ SourceEndpointArn }}',
 '{{ TargetEndpointArn }}',
 '{{ ReplicationType }}',
 '{{ ComputeConfig }}',
 '{{ ReplicationSettings }}',
 '{{ SupplementalSettings }}',
 '{{ ResourceIdentifier }}',
 '{{ TableMappings }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ReplicationConfigIdentifier }}',
 '{{ ReplicationConfigArn }}',
 '{{ SourceEndpointArn }}',
 '{{ TargetEndpointArn }}',
 '{{ ReplicationType }}',
 '{{ ComputeConfig }}',
 '{{ ReplicationSettings }}',
 '{{ SupplementalSettings }}',
 '{{ ResourceIdentifier }}',
 '{{ TableMappings }}',
 '{{ Tags }}',
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
  - name: replication_config
    props:
      - name: ReplicationConfigIdentifier
        value: '{{ ReplicationConfigIdentifier }}'
      - name: ReplicationConfigArn
        value: '{{ ReplicationConfigArn }}'
      - name: SourceEndpointArn
        value: '{{ SourceEndpointArn }}'
      - name: TargetEndpointArn
        value: '{{ TargetEndpointArn }}'
      - name: ReplicationType
        value: '{{ ReplicationType }}'
      - name: ComputeConfig
        value:
          AvailabilityZone: '{{ AvailabilityZone }}'
          DnsNameServers: '{{ DnsNameServers }}'
          KmsKeyId: '{{ KmsKeyId }}'
          MaxCapacityUnits: '{{ MaxCapacityUnits }}'
          MinCapacityUnits: '{{ MinCapacityUnits }}'
          MultiAZ: '{{ MultiAZ }}'
          PreferredMaintenanceWindow: '{{ PreferredMaintenanceWindow }}'
          ReplicationSubnetGroupId: '{{ ReplicationSubnetGroupId }}'
          VpcSecurityGroupIds:
            - '{{ VpcSecurityGroupIds[0] }}'
      - name: ReplicationSettings
        value: {}
      - name: SupplementalSettings
        value: {}
      - name: ResourceIdentifier
        value: '{{ ResourceIdentifier }}'
      - name: TableMappings
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
dms:DescribeReplicationConfigs,
dms:ListTagsForResource
```

### Update
```json
dms:ModifyReplicationConfig,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
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

