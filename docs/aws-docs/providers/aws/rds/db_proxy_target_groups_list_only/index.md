---
title: db_proxy_target_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_target_groups_list_only
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

Lists <code>db_proxy_target_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/db_proxy_target_groups/"><code>db_proxy_target_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_target_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyTargetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_target_groups_list_only" /></td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>db_proxy_target_groups</code> in a region.
```sql
SELECT
region,
target_group_arn
FROM aws.rds.db_proxy_target_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_proxy_target_groups_list_only</code> resource, see <a href="/providers/aws/rds/db_proxy_target_groups/#permissions"><code>db_proxy_target_groups</code></a>


