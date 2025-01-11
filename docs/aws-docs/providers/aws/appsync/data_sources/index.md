---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - appsync
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppSync::DataSource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>Unique AWS AppSync GraphQL API identifier where this data source will be created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the data source.</td></tr>
<tr><td><CopyableCode code="dynamo_db_config" /></td><td><code>object</code></td><td>AWS Region and TableName for an Amazon DynamoDB table in your account.</td></tr>
<tr><td><CopyableCode code="elasticsearch_config" /></td><td><code>object</code></td><td>AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.<br />As of September 2021, Amazon Elasticsearch Service is Amazon OpenSearch Service. This property is deprecated. For new data sources, use OpenSearchServiceConfig to specify an OpenSearch Service data source.</td></tr>
<tr><td><CopyableCode code="event_bridge_config" /></td><td><code>object</code></td><td>ARN for the EventBridge bus.</td></tr>
<tr><td><CopyableCode code="http_config" /></td><td><code>object</code></td><td>Endpoints for an HTTP data source.</td></tr>
<tr><td><CopyableCode code="lambda_config" /></td><td><code>object</code></td><td>An ARN of a Lambda function in valid ARN format. This can be the ARN of a Lambda function that exists in the current account or in another account.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Friendly name for you to identify your AppSync data source after creation.</td></tr>
<tr><td><CopyableCode code="open_search_service_config" /></td><td><code>object</code></td><td>AWS Region and Endpoints for an Amazon OpenSearch Service domain in your account.</td></tr>
<tr><td><CopyableCode code="relational_database_config" /></td><td><code>object</code></td><td>Relational Database configuration of the relational database data source.</td></tr>
<tr><td><CopyableCode code="service_role_arn" /></td><td><code>string</code></td><td>The AWS Identity and Access Management service role ARN for the data source. The system assumes this role when accessing the data source.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the data source.</td></tr>
<tr><td><CopyableCode code="data_source_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the API key, such as arn:aws:appsync:us-east-1:123456789012:apis/graphqlapiid/datasources/datasourcename.</td></tr>
<tr><td><CopyableCode code="metrics_config" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html"><code>AWS::AppSync::DataSource</code></a>.

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
    <td><CopyableCode code="Type, ApiId, Name, region" /></td>
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
api_id,
description,
dynamo_db_config,
elasticsearch_config,
event_bridge_config,
http_config,
lambda_config,
name,
open_search_service_config,
relational_database_config,
service_role_arn,
type,
data_source_arn,
metrics_config
FROM aws.appsync.data_sources
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_source</code>.
```sql
SELECT
region,
api_id,
description,
dynamo_db_config,
elasticsearch_config,
event_bridge_config,
http_config,
lambda_config,
name,
open_search_service_config,
relational_database_config,
service_role_arn,
type,
data_source_arn,
metrics_config
FROM aws.appsync.data_sources
WHERE region = 'us-east-1' AND data__Identifier = '<DataSourceArn>';
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
INSERT INTO aws.appsync.data_sources (
 ApiId,
 Name,
 Type,
 region
)
SELECT 
'{{ ApiId }}',
 '{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appsync.data_sources (
 ApiId,
 Description,
 DynamoDBConfig,
 ElasticsearchConfig,
 EventBridgeConfig,
 HttpConfig,
 LambdaConfig,
 Name,
 OpenSearchServiceConfig,
 RelationalDatabaseConfig,
 ServiceRoleArn,
 Type,
 MetricsConfig,
 region
)
SELECT 
 '{{ ApiId }}',
 '{{ Description }}',
 '{{ DynamoDBConfig }}',
 '{{ ElasticsearchConfig }}',
 '{{ EventBridgeConfig }}',
 '{{ HttpConfig }}',
 '{{ LambdaConfig }}',
 '{{ Name }}',
 '{{ OpenSearchServiceConfig }}',
 '{{ RelationalDatabaseConfig }}',
 '{{ ServiceRoleArn }}',
 '{{ Type }}',
 '{{ MetricsConfig }}',
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
      - name: ApiId
        value: '{{ ApiId }}'
      - name: Description
        value: '{{ Description }}'
      - name: DynamoDBConfig
        value:
          TableName: '{{ TableName }}'
          DeltaSyncConfig:
            BaseTableTTL: '{{ BaseTableTTL }}'
            DeltaSyncTableTTL: '{{ DeltaSyncTableTTL }}'
            DeltaSyncTableName: '{{ DeltaSyncTableName }}'
          UseCallerCredentials: '{{ UseCallerCredentials }}'
          AwsRegion: '{{ AwsRegion }}'
          Versioned: '{{ Versioned }}'
      - name: ElasticsearchConfig
        value:
          AwsRegion: '{{ AwsRegion }}'
          Endpoint: '{{ Endpoint }}'
      - name: EventBridgeConfig
        value:
          EventBusArn: '{{ EventBusArn }}'
      - name: HttpConfig
        value:
          Endpoint: '{{ Endpoint }}'
          AuthorizationConfig:
            AuthorizationType: '{{ AuthorizationType }}'
            AwsIamConfig:
              SigningRegion: '{{ SigningRegion }}'
              SigningServiceName: '{{ SigningServiceName }}'
      - name: LambdaConfig
        value:
          LambdaFunctionArn: '{{ LambdaFunctionArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: OpenSearchServiceConfig
        value:
          AwsRegion: '{{ AwsRegion }}'
          Endpoint: '{{ Endpoint }}'
      - name: RelationalDatabaseConfig
        value:
          RdsHttpEndpointConfig:
            DatabaseName: '{{ DatabaseName }}'
            AwsRegion: '{{ AwsRegion }}'
            DbClusterIdentifier: '{{ DbClusterIdentifier }}'
            AwsSecretStoreArn: '{{ AwsSecretStoreArn }}'
            Schema: '{{ Schema }}'
          RelationalDatabaseSourceType: '{{ RelationalDatabaseSourceType }}'
      - name: ServiceRoleArn
        value: '{{ ServiceRoleArn }}'
      - name: Type
        value: '{{ Type }}'
      - name: MetricsConfig
        value: '{{ MetricsConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appsync.data_sources
WHERE data__Identifier = '<DataSourceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
appsync:CreateDataSource,
appsync:GetDataSource,
iam:PassRole
```

### Read
```json
appsync:GetDataSource
```

### Update
```json
appsync:UpdateDataSource,
iam:PassRole
```

### Delete
```json
appsync:DeleteDataSource,
appsync:GetDataSource
```

### List
```json
appsync:ListDataSources
```
