---
title: parameter_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter_group_tags
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

Expands all tag keys and values for <code>parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.parameter_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The name of the parameter group family that this parameter group is compatible with.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parameter group.</td></tr>
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
Expands tags for all <code>parameter_groups</code> in a region.
```sql
SELECT
region,
parameter_group_name,
family,
description,
parameters,
arn,
tag_key,
tag_value
FROM aws.memorydb.parameter_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>parameter_group_tags</code> resource, see <a href="/providers/aws/memorydb/parameter_groups/#permissions"><code>parameter_groups</code></a>

