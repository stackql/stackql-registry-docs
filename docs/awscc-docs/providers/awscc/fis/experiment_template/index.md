---
title: experiment_template
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_template
  - fis
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>experiment_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>experiment_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.fis.experiment_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>actions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>stop_conditions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>log_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>experiment_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
description,
targets,
actions,
stop_conditions,
log_configuration,
role_arn,
tags,
experiment_options
FROM awscc.fis.experiment_template
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>experiment_template</code> resource, the following permissions are required:

### Read
```json
fis:GetExperimentTemplate,
fis:ListTagsForResource
```

### Update
```json
fis:UpdateExperimentTemplate,
fis:TagResource,
fis:UntagResource,
iam:PassRole
```

### Delete
```json
fis:DeleteExperimentTemplate
```

