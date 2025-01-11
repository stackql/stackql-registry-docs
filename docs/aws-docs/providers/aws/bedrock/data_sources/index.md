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

Creates, updates, deletes or gets a <code>data_source</code> resource or lists <code>data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_source_configuration" /></td><td><code>object</code></td><td>Specifies a raw data source location to ingest.</td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="knowledge_base_id" /></td><td><code>string</code></td><td>The unique identifier of the knowledge base to which to add the data source.</td></tr>
<tr><td><CopyableCode code="data_source_status" /></td><td><code>string</code></td><td>The status of a data source.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data source.</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Contains details about the server-side encryption for the data source.</td></tr>
<tr><td><CopyableCode code="vector_ingestion_configuration" /></td><td><code>object</code></td><td>Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.</td></tr>
<tr><td><CopyableCode code="data_deletion_policy" /></td><td><code>string</code></td><td>The deletion policy for the data source.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time at which the data source was created.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time at which the knowledge base was last updated.</td></tr>
<tr><td><CopyableCode code="failure_reasons" /></td><td><code>array</code></td><td>The details of the failure reasons related to the data source.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-datasource.html"><code>AWS::Bedrock::DataSource</code></a>.

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
Gets all <code>data_sources</code> in a region.
```sql
SELECT
region,
data_source_configuration,
data_source_id,
description,
knowledge_base_id,
data_source_status,
name,
server_side_encryption_configuration,
vector_ingestion_configuration,
data_deletion_policy,
created_at,
updated_at,
failure_reasons
FROM aws.bedrock.data_sources
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_source</code>.
```sql
SELECT
region,
data_source_configuration,
data_source_id,
description,
knowledge_base_id,
data_source_status,
name,
server_side_encryption_configuration,
vector_ingestion_configuration,
data_deletion_policy,
created_at,
updated_at,
failure_reasons
FROM aws.bedrock.data_sources
WHERE region = 'us-east-1' AND data__Identifier = '<KnowledgeBaseId>|<DataSourceId>';
```

## `INSERT` example

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
 DataDeletionPolicy,
 region
)
SELECT 
 '{{ DataSourceConfiguration }}',
 '{{ Description }}',
 '{{ KnowledgeBaseId }}',
 '{{ Name }}',
 '{{ ServerSideEncryptionConfiguration }}',
 '{{ VectorIngestionConfiguration }}',
 '{{ DataDeletionPolicy }}',
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
            BucketOwnerAccountId: '{{ BucketOwnerAccountId }}'
          ConfluenceConfiguration:
            SourceConfiguration:
              HostUrl: '{{ HostUrl }}'
              HostType: '{{ HostType }}'
              AuthType: '{{ AuthType }}'
              CredentialsSecretArn: '{{ CredentialsSecretArn }}'
            CrawlerConfiguration:
              FilterConfiguration:
                Type: '{{ Type }}'
                PatternObjectFilter:
                  Filters:
                    - ObjectType: '{{ ObjectType }}'
                      InclusionFilters:
                        - '{{ InclusionFilters[0] }}'
                      ExclusionFilters: null
          SalesforceConfiguration:
            SourceConfiguration:
              HostUrl: '{{ HostUrl }}'
              AuthType: '{{ AuthType }}'
              CredentialsSecretArn: '{{ CredentialsSecretArn }}'
            CrawlerConfiguration:
              FilterConfiguration: null
          SharePointConfiguration:
            SourceConfiguration:
              SiteUrls:
                - '{{ SiteUrls[0] }}'
              HostType: '{{ HostType }}'
              AuthType: '{{ AuthType }}'
              CredentialsSecretArn: '{{ CredentialsSecretArn }}'
              TenantId: '{{ TenantId }}'
              Domain: '{{ Domain }}'
            CrawlerConfiguration:
              FilterConfiguration: null
          WebConfiguration:
            SourceConfiguration:
              UrlConfiguration:
                SeedUrls:
                  - Url: '{{ Url }}'
            CrawlerConfiguration:
              CrawlerLimits:
                RateLimit: '{{ RateLimit }}'
              InclusionFilters: null
              ExclusionFilters: null
              Scope: '{{ Scope }}'
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
            HierarchicalChunkingConfiguration:
              LevelConfigurations:
                - MaxTokens: '{{ MaxTokens }}'
              OverlapTokens: '{{ OverlapTokens }}'
            SemanticChunkingConfiguration:
              BreakpointPercentileThreshold: '{{ BreakpointPercentileThreshold }}'
              BufferSize: '{{ BufferSize }}'
              MaxTokens: '{{ MaxTokens }}'
          CustomTransformationConfiguration:
            IntermediateStorage:
              S3Location:
                URI: '{{ URI }}'
            Transformations:
              - StepToApply: '{{ StepToApply }}'
                TransformationFunction:
                  TransformationLambdaConfiguration:
                    LambdaArn: '{{ LambdaArn }}'
          ParsingConfiguration:
            ParsingStrategy: '{{ ParsingStrategy }}'
            BedrockFoundationModelConfiguration:
              ModelArn: '{{ ModelArn }}'
              ParsingPrompt:
                ParsingPromptText: '{{ ParsingPromptText }}'
              ParsingModality: '{{ ParsingModality }}'
            BedrockDataAutomationConfiguration:
              ParsingModality: null
      - name: DataDeletionPolicy
        value: '{{ DataDeletionPolicy }}'

```
</TabItem>
</Tabs>

## `DELETE` example

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

### Read
```json
bedrock:GetDataSource
```

### Update
```json
bedrock:GetDataSource,
bedrock:UpdateDataSource
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
