---
title: parameter_group
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter_group
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

Gets or operates on an individual <code>parameter_group</code> resource, use <code>parameter_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.parameter_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="parameter_group_name" /></td><td><code>string</code></td><td>The name of the parameter group.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The name of the parameter group family that this parameter group is compatible with.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this parameter group.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parameter group.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
parameter_group_name,
family,
description,
tags,
parameters,
arn
FROM aws.memorydb.parameter_group
WHERE data__Identifier = '<ParameterGroupName>';
```

## Permissions

To operate on the <code>parameter_group</code> resource, the following permissions are required:

### Read
```json
memorydb:DescribeParameterGroups,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateParameterGroup,
memorydb:DescribeParameterGroups,
memorydb:DescribeParameters,
memorydb:DescribeClusters,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:DeleteParameterGroup
```

