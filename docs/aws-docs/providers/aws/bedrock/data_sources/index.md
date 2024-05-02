---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - bedrock
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bedrock.data_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>knowledge_base_id</code></td><td><code>string</code></td><td>The unique identifier of the knowledge base to which to add the data source.</td></tr>
<tr><td><code>data_source_id</code></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
knowledge_base_id,
data_source_id
FROM aws.bedrock.data_sources
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateDataSource,
bedrock:GetDataSource,
bedrock:GetKnowledgeBase
```

### List
```json
bedrock:ListDataSources
```

