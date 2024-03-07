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
Gets an individual <code>configured_table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configured_table</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.configured_table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><code>allowed_columns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>analysis_method</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configured_table_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>analysis_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>table_reference</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### Delete
```json
cleanrooms:DeleteConfiguredTable,
cleanrooms:GetConfiguredTable,
cleanrooms:ListConfiguredTables,
cleanrooms:GetConfiguredTableAnalysisRule,
cleanrooms:DeleteConfiguredTableAnalysisRule,
cleanrooms:ListTagsForResource,
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


## Example
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
FROM awscc.cleanrooms.configured_table
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConfiguredTableIdentifier&gt;'
```
