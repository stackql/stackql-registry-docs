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
<tr><td><b>Description</b></td><td>assistant_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wisdom.assistant_association</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>assistant_association</code> resource, the following permissions are required:

### Update
<pre>
wisdom:GetAssistantAssociation</pre>

### Read
<pre>
wisdom:GetAssistantAssociation</pre>

### Delete
<pre>
wisdom:DeleteAssistantAssociation</pre>


## Example
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
FROM awscc.wisdom.assistant_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AssistantAssociationId&gt;'
AND data__Identifier = '&lt;AssistantId&gt;'
```
