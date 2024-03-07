---
title: knowledge_bases
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases
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
Retrieves a list of <code>knowledge_bases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>knowledge_bases</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wisdom.knowledge_bases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>knowledge_base_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>knowledge_bases</code> resource, the following permissions are required:

### Create
<pre>
appflow:CreateFlow,
appflow:DeleteFlow,
appflow:StartFlow,
appflow:TagResource,
appflow:UseConnectorProfile,
app-integrations:CreateDataIntegrationAssociation,
app-integrations:GetDataIntegration,
kms:DescribeKey,
kms:CreateGrant,
kms:ListGrants,
wisdom:CreateKnowledgeBase,
wisdom:TagResource</pre>

### List
<pre>
wisdom:ListKnowledgeBases</pre>


## Example
```sql
SELECT
region,
knowledge_base_id
FROM awscc.wisdom.knowledge_bases
WHERE region = 'us-east-1'
```
