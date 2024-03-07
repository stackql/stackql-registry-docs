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
Gets an individual <code>parameter_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>parameter_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.memorydb.parameter_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>parameter_group_name</code></td><td><code>string</code></td><td>The name of the parameter group.</td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td>The name of the parameter group family that this parameter group is compatible with.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the parameter group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this parameter group.</td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td>An map of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional.</td></tr>
<tr><td><code>a_rn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parameter group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
parameter_group_name,
family,
description,
tags,
parameters,
a_rn
FROM awscc.memorydb.parameter_group
WHERE region = 'us-east-1'
AND data__Identifier = '{ParameterGroupName}';
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

