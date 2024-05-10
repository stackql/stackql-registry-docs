---
title: assistant_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - assistant_associations
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>assistant_associations</code> in a region or to create or delete a <code>assistant_associations</code> resource, use <code>assistant_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assistant_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AssistantAssociation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.assistant_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="assistant_association_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
assistant_association_id,
assistant_id
FROM aws.wisdom.assistant_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>assistant_association</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- assistant_association.iql (required properties only)
INSERT INTO aws.wisdom.assistant_associations (
 AssistantId,
 Association,
 AssociationType,
 region
)
SELECT 
'{{ AssistantId }}',
 '{{ Association }}',
 '{{ AssociationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- assistant_association.iql (all properties)
INSERT INTO aws.wisdom.assistant_associations (
 AssistantId,
 Association,
 AssociationType,
 Tags,
 region
)
SELECT 
 '{{ AssistantId }}',
 '{{ Association }}',
 '{{ AssociationType }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: assistant_association
    props:
      - name: AssistantId
        value: '{{ AssistantId }}'
      - name: Association
        value:
          KnowledgeBaseId: '{{ KnowledgeBaseId }}'
      - name: AssociationType
        value: '{{ AssociationType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wisdom.assistant_associations
WHERE data__Identifier = '<AssistantAssociationId|AssistantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assistant_associations</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateAssistantAssociation,
wisdom:TagResource
```

### List
```json
wisdom:ListAssistantAssociations
```

### Delete
```json
wisdom:DeleteAssistantAssociation
```

