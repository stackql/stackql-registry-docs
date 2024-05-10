---
title: schema
hide_title: false
hide_table_of_contents: false
keywords:
  - schema
  - eventschemas
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


Gets or updates an individual <code>schema</code> resource, use <code>schemata</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.schema" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of schema. Valid types include OpenApi3 and JSONSchemaDraft4.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the schema.</td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td>The version number of the schema.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The source of the schema definition.</td></tr>
<tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td>The name of the schema registry.</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema.</td></tr>
<tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the schema.</td></tr>
<tr><td><CopyableCode code="last_modified" /></td><td><code>string</code></td><td>The last modified time of the schema.</td></tr>
<tr><td><CopyableCode code="version_created_date" /></td><td><code>string</code></td><td>The date the schema version was created.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
type,
description,
schema_version,
content,
registry_name,
schema_arn,
schema_name,
last_modified,
version_created_date,
tags
FROM aws.eventschemas.schema
WHERE region = 'us-east-1' AND data__Identifier = '<SchemaArn>';
```


## Permissions

To operate on the <code>schema</code> resource, the following permissions are required:

### Read
```json
schemas:DescribeSchema
```

### Update
```json
schemas:DescribeSchema,
schemas:UpdateSchema,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource
```

