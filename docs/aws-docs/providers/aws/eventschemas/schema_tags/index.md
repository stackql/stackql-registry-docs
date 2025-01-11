---
title: schema_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_tags
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

Expands all tag keys and values for <code>schemata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.schema_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of schema. Valid types include OpenApi3 and JSONSchemaDraft4.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the schema.</td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td>The version number of the schema.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The source of the schema definition.</td></tr>
<tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td>The name of the schema registry.</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema.</td></tr>
<tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the schema.</td></tr>
<tr><td><CopyableCode code="last_modified" /></td><td><code>string</code></td><td>The last modified time of the schema.</td></tr>
<tr><td><CopyableCode code="version_created_date" /></td><td><code>string</code></td><td>The date the schema version was created.</td></tr>
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
Expands tags for all <code>schemata</code> in a region.
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
tag_key,
tag_value
FROM aws.eventschemas.schema_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>schema_tags</code> resource, see <a href="/providers/aws/eventschemas/schemata/#permissions"><code>schemata</code></a>

