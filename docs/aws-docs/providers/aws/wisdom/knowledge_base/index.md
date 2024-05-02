---
title: knowledge_base
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_base
  - wisdom
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>knowledge_base</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_base</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wisdom.knowledge_base</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>knowledge_base_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>knowledge_base_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>knowledge_base_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rendering_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
description,
knowledge_base_arn,
knowledge_base_id,
knowledge_base_type,
name,
rendering_configuration,
server_side_encryption_configuration,
source_configuration,
tags
FROM aws.wisdom.knowledge_base
WHERE data__Identifier = '<KnowledgeBaseId>';
```

## Permissions

To operate on the <code>knowledge_base</code> resource, the following permissions are required:

### Update
```json
wisdom:GetKnowledgeBase
```

### Delete
```json
appflow:DeleteFlow,
appflow:StopFlow,
app-integrations:DeleteDataIntegrationAssociation,
wisdom:DeleteKnowledgeBase
```

### Read
```json
wisdom:GetKnowledgeBase
```

