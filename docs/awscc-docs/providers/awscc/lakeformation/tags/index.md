---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - lakeformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>tags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tags</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lakeformation.tags</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tag_key</code></td><td><code>undefined</code></td><td>The key-name for the LF-tag.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>tags</code> resource, the following permissions are required:

### Create
```json
lakeformation:CreateLFTag
```

### List
```json
lakeformation:ListLFTags
```


## Example
```sql
SELECT
region,
tag_key
FROM awscc.lakeformation.tags
WHERE region = 'us-east-1'
```
