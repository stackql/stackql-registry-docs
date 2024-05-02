---
title: knowledge_base
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_base
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
Gets or operates on an individual <code>knowledge_base</code> resource, use <code>knowledge_bases</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_base</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bedrock.knowledge_base</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><code>knowledge_base_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>knowledge_base_id</code></td><td><code>string</code></td><td>The unique identifier of the knowledge base.</td></tr>
<tr><td><code>knowledge_base_arn</code></td><td><code>string</code></td><td>The ARN of the knowledge base.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the knowledge base.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the IAM role with permissions to invoke API operations on the knowledge base. The ARN must begin with AmazonBedrockExecutionRoleForKnowledgeBase_</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time at which the knowledge base was created.</td></tr>
<tr><td><code>failure_reasons</code></td><td><code>array</code></td><td>A list of reasons that the API operation on the knowledge base failed.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
<tr><td><code>storage_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
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
knowledge_base_configuration,
knowledge_base_id,
knowledge_base_arn,
name,
status,
role_arn,
created_at,
failure_reasons,
updated_at,
storage_configuration,
tags
FROM aws.bedrock.knowledge_base
WHERE data__Identifier = '<KnowledgeBaseId>';
```

## Permissions

To operate on the <code>knowledge_base</code> resource, the following permissions are required:

### Read
```json
bedrock:GetKnowledgeBase,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:GetKnowledgeBase,
bedrock:UpdateKnowledgeBase,
bedrock:TagResource,
bedrock:UntagResource,
bedrock:ListTagsForResource,
bedrock:AssociateThirdPartyKnowledgeBase,
iam:PassRole
```

### Delete
```json
bedrock:GetKnowledgeBase,
bedrock:DeleteKnowledgeBase,
bedrock:ListDataSources
```

