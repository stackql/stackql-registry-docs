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

Creates, updates, deletes or gets a <code>knowledge_base</code> resource or lists <code>knowledge_bases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.knowledge_bases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="knowledge_base_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rendering_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="KnowledgeBaseType, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>knowledge_bases</code> in a region.
```sql
SELECT
region,
knowledge_base_id
FROM aws.wisdom.knowledge_bases
WHERE region = 'us-east-1';
```
Gets all properties from a <code>knowledge_base</code>.
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
FROM aws.wisdom.knowledge_bases
WHERE region = 'us-east-1' AND data__Identifier = '<KnowledgeBaseId>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
wisdom:ListKnowledgeBases
```

### Read
```json
wisdom:GetKnowledgeBase
```

