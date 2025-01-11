---
title: knowledge_bases
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_bases
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

Creates, updates, deletes or gets a <code>knowledge_base</code> resource or lists <code>knowledge_bases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>knowledge_bases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::KnowledgeBase Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.knowledge_bases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="knowledge_base_configuration" /></td><td><code>object</code></td><td>Contains details about the embeddings model used for the knowledge base.</td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td>The unique identifier of the knowledge base.</td></tr>
<tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td>The ARN of the knowledge base.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the knowledge base.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of a knowledge base.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role with permissions to invoke API operations on the knowledge base. The ARN must begin with AmazonBedrockExecutionRoleForKnowledgeBase_</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was created.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>A list of reasons that the API operation on the knowledge base failed.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
<tr><td><CopyableCode code="storage_configuration" /></td><td><code>object</code></td><td>The vector store service in which the knowledge base is stored.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-knowledgebase.html"><code>AWS::Bedrock::KnowledgeBase</code></a>.

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
    <td><CopyableCode code="KnowledgeBaseConfiguration, Name, RoleArn, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>knowledge_bases</code> in a region.
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
FROM aws.bedrock.knowledge_bases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>knowledge_base</code>.
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
FROM aws.bedrock.knowledge_bases
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
INSERT INTO aws.bedrock.knowledge_bases (
 KnowledgeBaseConfiguration,
 Name,
 RoleArn,
 region
)
SELECT 
'{{ KnowledgeBaseConfiguration }}',
 '{{ Name }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.knowledge_bases (
 Description,
 KnowledgeBaseConfiguration,
 Name,
 RoleArn,
 StorageConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ KnowledgeBaseConfiguration }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ StorageConfiguration }}',
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
      - name: KnowledgeBaseConfiguration
        value:
          Type: '{{ Type }}'
          VectorKnowledgeBaseConfiguration:
            EmbeddingModelArn: '{{ EmbeddingModelArn }}'
            EmbeddingModelConfiguration:
              BedrockEmbeddingModelConfiguration:
                Dimensions: '{{ Dimensions }}'
            SupplementalDataStorageConfiguration:
              SupplementalDataStorageLocations:
                - SupplementalDataStorageLocationType: '{{ SupplementalDataStorageLocationType }}'
                  S3Location:
                    URI: '{{ URI }}'
          KendraKnowledgeBaseConfiguration:
            KendraIndexArn: '{{ KendraIndexArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: StorageConfiguration
        value:
          Type: '{{ Type }}'
          OpensearchServerlessConfiguration:
            CollectionArn: '{{ CollectionArn }}'
            VectorIndexName: '{{ VectorIndexName }}'
            FieldMapping:
              VectorField: '{{ VectorField }}'
              TextField: '{{ TextField }}'
              MetadataField: '{{ MetadataField }}'
          PineconeConfiguration:
            ConnectionString: '{{ ConnectionString }}'
            CredentialsSecretArn: '{{ CredentialsSecretArn }}'
            Namespace: '{{ Namespace }}'
            FieldMapping:
              TextField: '{{ TextField }}'
              MetadataField: '{{ MetadataField }}'
          RdsConfiguration:
            ResourceArn: '{{ ResourceArn }}'
            CredentialsSecretArn: '{{ CredentialsSecretArn }}'
            DatabaseName: '{{ DatabaseName }}'
            TableName: '{{ TableName }}'
            FieldMapping:
              PrimaryKeyField: '{{ PrimaryKeyField }}'
              VectorField: '{{ VectorField }}'
              TextField: '{{ TextField }}'
              MetadataField: '{{ MetadataField }}'
          MongoDbAtlasConfiguration:
            Endpoint: '{{ Endpoint }}'
            CredentialsSecretArn: '{{ CredentialsSecretArn }}'
            DatabaseName: '{{ DatabaseName }}'
            CollectionName: '{{ CollectionName }}'
            VectorIndexName: '{{ VectorIndexName }}'
            EndpointServiceName: '{{ EndpointServiceName }}'
            FieldMapping:
              VectorField: '{{ VectorField }}'
              TextField: '{{ TextField }}'
              MetadataField: '{{ MetadataField }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.knowledge_bases
WHERE data__Identifier = '<KnowledgeBaseId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>knowledge_bases</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateKnowledgeBase,
bedrock:GetKnowledgeBase,
bedrock:TagResource,
bedrock:ListTagsForResource,
bedrock:AssociateThirdPartyKnowledgeBase,
iam:PassRole
```

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

### List
```json
bedrock:ListKnowledgeBases
```
