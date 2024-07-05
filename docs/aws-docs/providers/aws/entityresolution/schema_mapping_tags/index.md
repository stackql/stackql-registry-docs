---
title: schema_mapping_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_mapping_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>schema_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_mapping_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>SchemaMapping defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.schema_mapping_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="schema_name" /></td><td><code>string</code></td><td>The name of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the SchemaMapping</td></tr>
<tr><td><CopyableCode code="mapped_input_fields" /></td><td><code>array</code></td><td>The SchemaMapping attributes input</td></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The SchemaMapping arn associated with the Schema</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got created</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got last updated at</td></tr>
<tr><td><CopyableCode code="has_workflows" /></td><td><code>boolean</code></td><td>The boolean value that indicates whether or not a SchemaMapping has MatchingWorkflows that are associated with</td></tr>
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
Expands tags for all <code>schema_mappings</code> in a region.
```sql
SELECT
region,
schema_name,
description,
mapped_input_fields,
schema_arn,
created_at,
updated_at,
has_workflows,
tag_key,
tag_value
FROM aws.entityresolution.schema_mapping_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>schema_mapping_tags</code> resource, see <a href="/providers/aws/entityresolution/schema_mappings/#permissions"><code>schema_mappings</code></a>


