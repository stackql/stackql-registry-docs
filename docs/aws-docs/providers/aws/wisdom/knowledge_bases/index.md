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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>knowledge_bases</code> in a region or create a <code>knowledge_bases</code> resource, use <code>knowledge_base</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.knowledge_bases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
knowledge_base_id
FROM aws.wisdom.knowledge_bases
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>knowledge_bases</code> resource, the following permissions are required:

### Create
```json
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
wisdom:TagResource
```

### List
```json
wisdom:ListKnowledgeBases
```

