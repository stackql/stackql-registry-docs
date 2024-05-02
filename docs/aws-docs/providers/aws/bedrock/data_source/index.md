---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
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
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bedrock.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>data_source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_source_id</code></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><code>knowledge_base_id</code></td><td><code>string</code></td><td>The unique identifier of the knowledge base to which to add the data source.</td></tr>
<tr><td><code>data_source_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the data source.</td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vector_ingestion_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time at which the data source was created.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
data_source_configuration,
data_source_id,
description,
knowledge_base_id,
data_source_status,
name,
server_side_encryption_configuration,
vector_ingestion_configuration,
created_at,
updated_at
FROM aws.bedrock.data_source
WHERE data__Identifier = '<KnowledgeBaseId>|<DataSourceId>';
```

## Permissions

To operate on the <code>data_source</code> resource, the following permissions are required:

### Read
```json
bedrock:GetDataSource
```

### Update
```json
bedrock:GetDataSource,
bedrock:UpdateDataSource
```

### Delete
```json
bedrock:GetDataSource,
bedrock:DeleteDataSource
```

