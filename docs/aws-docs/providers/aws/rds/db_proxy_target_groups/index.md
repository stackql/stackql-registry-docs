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


Used to retrieve a list of <code>db_proxy_target_groups</code> in a region or to create or delete a <code>db_proxy_target_groups</code> resource, use <code>db_proxy_target_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyTargetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_target_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="target_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) representing the target group.</td></tr>
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
    <td><CopyableCode code="DBProxyName, TargetGroupName, region" /></td>
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
target_group_arn
FROM aws.rds.db_proxy_target_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
rds:DeregisterDBProxyTargets
```

### List
```json
rds:DescribeDBProxyTargetGroups
```

