---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>data_sources</code> in a region or to create or delete a <code>data_sources</code> resource, use <code>data_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td>The unique identifier of the knowledge base to which to add the data source.</td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
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
    <td><CopyableCode code="DataSourceConfiguration, Name, KnowledgeBaseId, region" /></td>
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
knowledge_base_id,
data_source_id
FROM aws.bedrock.data_sources
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>data_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.data_sources (
 DataSourceConfiguration,
 KnowledgeBaseId,
 Name,
 region
)
SELECT 
'{{ DataSourceConfiguration }}',
 '{{ KnowledgeBaseId }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.data_sources (
 DataSourceConfiguration,
 Description,
 KnowledgeBaseId,
 Name,
 ServerSideEncryptionConfiguration,
 VectorIngestionConfiguration,
 region
)
SELECT 
 '{{ DataSourceConfiguration }}',
 '{{ Description }}',
 '{{ KnowledgeBaseId }}',
 '{{ Name }}',
 '{{ ServerSideEncryptionConfiguration }}',
 '{{ VectorIngestionConfiguration }}',
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
  - name: data_source
    props:
      - name: DataSourceConfiguration
        value:
          Type: '{{ Type }}'
          S3Configuration:
            BucketArn: '{{ BucketArn }}'
            InclusionPrefixes:
              - '{{ InclusionPrefixes[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: KnowledgeBaseId
        value: '{{ KnowledgeBaseId }}'
      - name: Name
        value: '{{ Name }}'
      - name: ServerSideEncryptionConfiguration
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
      - name: VectorIngestionConfiguration
        value:
          ChunkingConfiguration:
            ChunkingStrategy: '{{ ChunkingStrategy }}'
            FixedSizeChunkingConfiguration:
              MaxTokens: '{{ MaxTokens }}'
              OverlapPercentage: '{{ OverlapPercentage }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.bedrock.data_sources
WHERE data__Identifier = '<KnowledgeBaseId|DataSourceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateDataSource,
bedrock:GetDataSource,
bedrock:GetKnowledgeBase
```

### Delete
```json
bedrock:GetDataSource,
bedrock:DeleteDataSource
```

### List
```json
bedrock:ListDataSources
```

