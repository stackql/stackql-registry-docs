---
title: schema_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_mapping
  - entityresolution
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

Gets or operates on an individual <code>schema_mapping</code> resource, use <code>schema_mappings</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>SchemaMapping defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.schema_mapping" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="mapped_input_fields" /></td><td><code>array</code></td><td>The SchemaMapping attributes input</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="has_workflows" /></td><td><code>boolean</code></td><td></td></tr>
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
schema_name,
description,
mapped_input_fields,
tags,
schema_arn,
created_at,
updated_at,
has_workflows
FROM aws.entityresolution.schema_mapping
WHERE data__Identifier = '<SchemaName>';
```

## Permissions

To operate on the <code>schema_mapping</code> resource, the following permissions are required:

### Read
```json
entityresolution:GetSchemaMapping,
entityresolution:ListTagsForResource
```

### Delete
```json
entityresolution:DeleteSchemaMapping,
entityresolution:GetSchemaMapping
```

### Update
```json
entityresolution:GetSchemaMapping,
entityresolution:UpdateSchemaMapping,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource
```

