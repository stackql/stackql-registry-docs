---
title: db_proxy_target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_target_groups
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

Creates, updates, deletes or gets a <code>db_proxy_target_group</code> resource or lists <code>db_proxy_target_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyTargetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_target_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_proxy_name" /></td><td><code>string</code></td><td>The identifier for the proxy.</td></tr>
<tr><td><CopyableCode code="target_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) representing the target group.</td></tr>
<tr><td><CopyableCode code="target_group_name" /></td><td><code>string</code></td><td>The identifier for the DBProxyTargetGroup</td></tr>
<tr><td><CopyableCode code="connection_pool_configuration_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="db_instance_identifiers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="db_cluster_identifiers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxytargetgroup.html"><code>AWS::RDS::DBProxyTargetGroup</code></a>.

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
    <td><CopyableCode code="DBProxyName, TargetGroupName, region" /></td>
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
Gets all <code>db_proxy_target_groups</code> in a region.
```sql
SELECT
region,
db_proxy_name,
target_group_arn,
target_group_name,
connection_pool_configuration_info,
db_instance_identifiers,
db_cluster_identifiers
FROM aws.rds.db_proxy_target_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_proxy_target_group</code>.
```sql
SELECT
region,
db_proxy_name,
target_group_arn,
target_group_name,
connection_pool_configuration_info,
db_instance_identifiers,
db_cluster_identifiers
FROM aws.rds.db_proxy_target_groups
WHERE region = 'us-east-1' AND data__Identifier = '<TargetGroupArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_proxy_target_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_proxy_target_groups (
 DBProxyName,
 TargetGroupName,
 region
)
SELECT 
'{{ DBProxyName }}',
 '{{ TargetGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_proxy_target_groups (
 DBProxyName,
 TargetGroupName,
 ConnectionPoolConfigurationInfo,
 DBInstanceIdentifiers,
 DBClusterIdentifiers,
 region
)
SELECT 
 '{{ DBProxyName }}',
 '{{ TargetGroupName }}',
 '{{ ConnectionPoolConfigurationInfo }}',
 '{{ DBInstanceIdentifiers }}',
 '{{ DBClusterIdentifiers }}',
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
  - name: db_proxy_target_group
    props:
      - name: DBProxyName
        value: '{{ DBProxyName }}'
      - name: TargetGroupName
        value: '{{ TargetGroupName }}'
      - name: ConnectionPoolConfigurationInfo
        value:
          MaxConnectionsPercent: '{{ MaxConnectionsPercent }}'
          MaxIdleConnectionsPercent: '{{ MaxIdleConnectionsPercent }}'
          ConnectionBorrowTimeout: '{{ ConnectionBorrowTimeout }}'
          SessionPinningFilters:
            - '{{ SessionPinningFilters[0] }}'
          InitQuery: '{{ InitQuery }}'
      - name: DBInstanceIdentifiers
        value:
          - '{{ DBInstanceIdentifiers[0] }}'
      - name: DBClusterIdentifiers
        value:
          - '{{ DBClusterIdentifiers[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rds.db_proxy_target_groups
WHERE data__Identifier = '<TargetGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_proxy_target_groups</code> resource, the following permissions are required:

### Create
```json
rds:DescribeDBProxies,
rds:DescribeDBProxyTargetGroups,
rds:ModifyDBProxyTargetGroup,
rds:RegisterDBProxyTargets
```

### Read
```json
rds:DescribeDBProxyTargetGroups,
rds:DescribeDBProxyTargets
```

### Update
```json
rds:DescribeDBProxyTargetGroups,
rds:ModifyDBProxyTargetGroup,
rds:RegisterDBProxyTargets,
rds:DeregisterDBProxyTargets
```

### Delete
```json
rds:DeregisterDBProxyTargets
```

### List
```json
rds:DescribeDBProxyTargetGroups
```
