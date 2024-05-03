---
title: task_template
hide_title: false
hide_table_of_contents: false
keywords:
  - task_template
  - connect
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

Gets or operates on an individual <code>task_template</code> resource, use <code>task_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TaskTemplate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.task_template" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier (arn) of the instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the task template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the task template.</td></tr>
<tr><td><CopyableCode code="contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><CopyableCode code="constraints" /></td><td><code>object</code></td><td>The constraints for the task template</td></tr>
<tr><td><CopyableCode code="defaults" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>The list of task template's fields</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
arn,
instance_arn,
name,
description,
contact_flow_arn,
constraints,
defaults,
fields,
status,
client_token,
tags
FROM aws.connect.task_template
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>task_template</code> resource, the following permissions are required:

### Read
```json
connect:GetTaskTemplate
```

### Update
```json
connect:UpdateTaskTemplate,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteTaskTemplate,
connect:UntagResource,
connect:GetTaskTemplate
```

