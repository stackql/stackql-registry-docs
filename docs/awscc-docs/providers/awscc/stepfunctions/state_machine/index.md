---
title: state_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine
  - stepfunctions
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>state_machine</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>state_machine</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.stepfunctions.state_machine</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition_string</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_machine_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_machine_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_machine_revision_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logging_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tracing_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>definition_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>definition_substitutions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
definition_string,
role_arn,
state_machine_name,
state_machine_type,
state_machine_revision_id,
logging_configuration,
tracing_configuration,
definition_s3_location,
definition_substitutions,
definition,
tags
FROM awscc.stepfunctions.state_machine
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>state_machine</code> resource, the following permissions are required:

### Read
```json
states:DescribeStateMachine,
states:ListTagsForResource
```

### Update
```json
states:UpdateStateMachine,
states:TagResource,
states:UntagResource,
states:ListTagsForResource,
iam:PassRole
```

### Delete
```json
states:DeleteStateMachine,
states:DescribeStateMachine
```

