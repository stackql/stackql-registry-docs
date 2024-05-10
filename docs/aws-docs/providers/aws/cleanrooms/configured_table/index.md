---
title: configured_table
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_table
  - cleanrooms
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


Gets or updates an individual <code>configured_table</code> resource, use <code>configured_tables</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be associated with collaborations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_table" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><CopyableCode code="allowed_columns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="analysis_method" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configured_table_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="analysis_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="table_reference" /></td><td><code>object</code></td><td></td></tr>
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
arn,
tags,
allowed_columns,
analysis_method,
configured_table_identifier,
description,
name,
analysis_rules,
table_reference
FROM aws.cleanrooms.configured_table
WHERE region = 'us-east-1' AND data__Identifier = '<ConfiguredTableIdentifier>';
```


## Permissions

To operate on the <code>configured_table</code> resource, the following permissions are required:

### Read
```json
cleanrooms:GetConfiguredTable,
cleanrooms:GetConfiguredTableAnalysisRule,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdateConfiguredTable,
cleanrooms:GetConfiguredTable,
cleanrooms:CreateConfiguredTableAnalysisRule,
cleanrooms:UpdateConfiguredTableAnalysisRule,
cleanrooms:GetConfiguredTableAnalysisRule,
cleanrooms:DeleteConfiguredTableAnalysisRule,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource,
glue:GetDatabase,
glue:GetDatabases,
glue:GetTable,
glue:GetTables,
glue:GetPartition,
glue:GetPartitions,
glue:BatchGetPartition,
glue:GetSchemaVersion
```

