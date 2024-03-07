---
title: variable
hide_title: false
hide_table_of_contents: false
keywords:
  - variable
  - frauddetector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>variable</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>variable</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.frauddetector.variable</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the variable.</td></tr>
<tr><td><code>data_source</code></td><td><code>string</code></td><td>The source of the data.</td></tr>
<tr><td><code>data_type</code></td><td><code>string</code></td><td>The data type.</td></tr>
<tr><td><code>default_value</code></td><td><code>string</code></td><td>The default value for the variable when no value is received.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with this variable.</td></tr>
<tr><td><code>variable_type</code></td><td><code>string</code></td><td>The variable type. For more information see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;frauddetector&#x2F;latest&#x2F;ug&#x2F;create-a-variable.html#variable-types</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the variable.</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>The time when the variable was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>The time when the variable was last updated.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
data_source,
data_type,
default_value,
description,
tags,
variable_type,
arn,
created_time,
last_updated_time
FROM awscc.frauddetector.variable
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>variable</code> resource, the following permissions are required:

### Read
```json
frauddetector:GetVariables,
frauddetector:ListTagsForResource
```

### Update
```json
frauddetector:GetVariables,
frauddetector:UpdateVariable,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:GetVariables,
frauddetector:DeleteVariable
```

