---
title: assistant_association
hide_title: false
hide_table_of_contents: false
keywords:
  - assistant_association
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
Gets an individual <code>assistant_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assistant_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AssistantAssociation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wisdom.assistant_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>assistant_association_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assistant_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assistant_association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assistant_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>association</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>association_type</code></td><td><code>string</code></td><td></td></tr>
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
assistant_association_arn,
assistant_arn,
assistant_association_id,
assistant_id,
association,
association_type,
tags
FROM aws.wisdom.assistant_association
WHERE data__Identifier = '<AssistantAssociationId>|<AssistantId>';
```

## Permissions

To operate on the <code>assistant_association</code> resource, the following permissions are required:

### Update
```json
wisdom:GetAssistantAssociation
```

### Read
```json
wisdom:GetAssistantAssociation
```

### Delete
```json
wisdom:DeleteAssistantAssociation
```

