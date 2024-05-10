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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>knowledge_bases</code> in a region or to create or delete a <code>knowledge_bases</code> resource, use <code>knowledge_base</code> to read or update an individual resource.

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
knowledge_base_id
FROM aws.wisdom.knowledge_bases
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>knowledge_base</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- knowledge_base.iql (required properties only)
INSERT INTO aws.wisdom.knowledge_bases (
 KnowledgeBaseType,
 Name,
 region
)
SELECT 
'{{ KnowledgeBaseType }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- knowledge_base.iql (all properties)
INSERT INTO aws.wisdom.knowledge_bases (
 Description,
 KnowledgeBaseType,
 Name,
 RenderingConfiguration,
 ServerSideEncryptionConfiguration,
 SourceConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ KnowledgeBaseType }}',
 '{{ Name }}',
 '{{ RenderingConfiguration }}',
 '{{ ServerSideEncryptionConfiguration }}',
 '{{ SourceConfiguration }}',
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
  - name: knowledge_base
    props:
      - name: Description
        value: '{{ Description }}'
      - name: KnowledgeBaseType
        value: '{{ KnowledgeBaseType }}'
      - name: Name
        value: '{{ Name }}'
      - name: RenderingConfiguration
        value:
          TemplateUri: '{{ TemplateUri }}'
      - name: ServerSideEncryptionConfiguration
        value:
          KmsKeyId: '{{ KmsKeyId }}'
      - name: SourceConfiguration
        value:
          AppIntegrations:
            ObjectFields:
              - '{{ ObjectFields[0] }}'
            AppIntegrationArn: '{{ AppIntegrationArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wisdom.knowledge_bases
WHERE data__Identifier = '<KnowledgeBaseId>'
AND region = 'us-east-1';
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

### Delete
```json
appflow:DeleteFlow,
appflow:StopFlow,
app-integrations:DeleteDataIntegrationAssociation,
wisdom:DeleteKnowledgeBase
```

### List
```json
wisdom:ListKnowledgeBases
```

