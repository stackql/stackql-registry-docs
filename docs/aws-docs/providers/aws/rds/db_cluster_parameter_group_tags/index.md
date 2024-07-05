---
title: db_cluster_parameter_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster_parameter_group_tags
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

Expands all tag keys and values for <code>db_cluster_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster_parameter_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_cluster_parameter_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A friendly description for this DB cluster parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.</td></tr>
<tr><td><CopyableCode code="db_cluster_parameter_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>db_cluster_parameter_groups</code> in a region.
```sql
SELECT
region,
description,
family,
parameters,
db_cluster_parameter_group_name,
tag_key,
tag_value
FROM aws.rds.db_cluster_parameter_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>db_cluster_parameter_group_tags</code> resource, see <a href="/providers/aws/rds/db_cluster_parameter_groups/#permissions"><code>db_cluster_parameter_groups</code></a>


