---
title: db_proxy_target_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_target_group
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
Gets an individual <code>db_proxy_target_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_target_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_proxy_target_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_proxy_target_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>d_bproxy_name</code></td><td><code>string</code></td><td>The identifier for the proxy.</td></tr>
<tr><td><code>target_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) representing the target group.</td></tr>
<tr><td><code>target_group_name</code></td><td><code>string</code></td><td>The identifier for the DBProxyTargetGroup</td></tr>
<tr><td><code>connection_pool_configuration_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>d_binstance_identifiers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>d_bcluster_identifiers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
d_bproxy_name,
target_group_arn,
target_group_name,
connection_pool_configuration_info,
d_binstance_identifiers,
d_bcluster_identifiers
FROM awscc.rds.db_proxy_target_group
WHERE region = 'us-east-1'
AND data__Identifier = '{TargetGroupArn}';
```

## Permissions

To operate on the <code>db_proxy_target_group</code> resource, the following permissions are required:

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

