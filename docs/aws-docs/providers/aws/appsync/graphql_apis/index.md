---
title: graphql_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - graphql_apis
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

Creates, updates, deletes or gets a <code>graphql_api</code> resource or lists <code>graphql_apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphql_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppSync::GraphQLApi</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.graphql_apis" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_authentication_providers" /></td><td><code>array</code></td><td>A list of additional authentication providers for the GraphqlApi API.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>Unique AWS AppSync GraphQL API identifier.</td></tr>
<tr><td><CopyableCode code="api_type" /></td><td><code>string</code></td><td>The value that indicates whether the GraphQL API is a standard API (GRAPHQL) or merged API (MERGED).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the API key</td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>string</code></td><td>Security configuration for your GraphQL API</td></tr>
<tr><td><CopyableCode code="enhanced_metrics_config" /></td><td><code>object</code></td><td>Enables and controls the enhanced metrics feature. Enhanced metrics emit granular data on API usage and performance such as AppSync request and error counts, latency, and cache hits/misses. All enhanced metric data is sent to your CloudWatch account, and you can configure the types of data that will be sent.</td></tr>
<tr><td><CopyableCode code="environment_variables" /></td><td><code>object</code></td><td>A map containing the list of resources with their properties and environment variables.</td></tr>
<tr><td><CopyableCode code="graph_ql_dns" /></td><td><code>string</code></td><td>The fully qualified domain name (FQDN) of the endpoint URL of your GraphQL API.</td></tr>
<tr><td><CopyableCode code="graph_ql_endpoint_arn" /></td><td><code>string</code></td><td>The GraphQL endpoint ARN.</td></tr>
<tr><td><CopyableCode code="graph_ql_url" /></td><td><code>string</code></td><td>The Endpoint URL of your GraphQL API.</td></tr>
<tr><td><CopyableCode code="introspection_config" /></td><td><code>string</code></td><td>Sets the value of the GraphQL API to enable (ENABLED) or disable (DISABLED) introspection. If no value is provided, the introspection configuration will be set to ENABLED by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.</td></tr>
<tr><td><CopyableCode code="lambda_authorizer_config" /></td><td><code>object</code></td><td>A LambdaAuthorizerConfig holds configuration on how to authorize AWS AppSync API access when using the AWS_LAMBDA authorizer mode. Be aware that an AWS AppSync API may have only one Lambda authorizer configured at a time.</td></tr>
<tr><td><CopyableCode code="log_config" /></td><td><code>object</code></td><td>The Amazon CloudWatch Logs configuration.</td></tr>
<tr><td><CopyableCode code="merged_api_execution_role_arn" /></td><td><code>string</code></td><td>The AWS Identity and Access Management service role ARN for a merged API.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The API name</td></tr>
<tr><td><CopyableCode code="open_id_connect_config" /></td><td><code>object</code></td><td>The OpenID Connect configuration.</td></tr>
<tr><td><CopyableCode code="owner_contact" /></td><td><code>string</code></td><td>The owner contact information for an API resource.</td></tr>
<tr><td><CopyableCode code="query_depth_limit" /></td><td><code>integer</code></td><td>The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query.</td></tr>
<tr><td><CopyableCode code="realtime_dns" /></td><td><code>string</code></td><td>The fully qualified domain name (FQDN) of the real-time endpoint URL of your GraphQL API.</td></tr>
<tr><td><CopyableCode code="realtime_url" /></td><td><code>string</code></td><td>The GraphQL API real-time endpoint URL.</td></tr>
<tr><td><CopyableCode code="resolver_count_limit" /></td><td><code>integer</code></td><td>The maximum number of resolvers that can be invoked in a single request.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this GraphQL API.<br /></td></tr>
<tr><td><CopyableCode code="user_pool_config" /></td><td><code>object</code></td><td>Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.<br /></td></tr>
<tr><td><CopyableCode code="visibility" /></td><td><code>string</code></td><td>Sets the scope of the GraphQL API to public (GLOBAL) or private (PRIVATE). By default, the scope is set to Global if no value is provided.</td></tr>
<tr><td><CopyableCode code="xray_enabled" /></td><td><code>boolean</code></td><td>A flag indicating whether to use AWS X-Ray tracing for this GraphqlApi.<br /></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html"><code>AWS::AppSync::GraphQLApi</code></a>.

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
    <td><CopyableCode code="Name, AuthenticationType, region" /></td>
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
Gets all <code>graphql_apis</code> in a region.
```sql
SELECT
region,
additional_authentication_providers,
api_id,
api_type,
arn,
authentication_type,
enhanced_metrics_config,
environment_variables,
graph_ql_dns,
graph_ql_endpoint_arn,
graph_ql_url,
introspection_config,
lambda_authorizer_config,
log_config,
merged_api_execution_role_arn,
name,
open_id_connect_config,
owner_contact,
query_depth_limit,
realtime_dns,
realtime_url,
resolver_count_limit,
tags,
user_pool_config,
visibility,
xray_enabled
FROM aws.appsync.graphql_apis
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>graphql_api</code>.
```sql
SELECT
region,
additional_authentication_providers,
api_id,
api_type,
arn,
authentication_type,
enhanced_metrics_config,
environment_variables,
graph_ql_dns,
graph_ql_endpoint_arn,
graph_ql_url,
introspection_config,
lambda_authorizer_config,
log_config,
merged_api_execution_role_arn,
name,
open_id_connect_config,
owner_contact,
query_depth_limit,
realtime_dns,
realtime_url,
resolver_count_limit,
tags,
user_pool_config,
visibility,
xray_enabled
FROM aws.appsync.graphql_apis
WHERE region = 'us-east-1' AND data__Identifier = '<ApiId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>graphql_api</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appsync.graphql_apis (
 AuthenticationType,
 Name,
 region
)
SELECT 
'{{ AuthenticationType }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appsync.graphql_apis (
 AdditionalAuthenticationProviders,
 ApiType,
 AuthenticationType,
 EnhancedMetricsConfig,
 EnvironmentVariables,
 IntrospectionConfig,
 LambdaAuthorizerConfig,
 LogConfig,
 MergedApiExecutionRoleArn,
 Name,
 OpenIDConnectConfig,
 OwnerContact,
 QueryDepthLimit,
 ResolverCountLimit,
 Tags,
 UserPoolConfig,
 Visibility,
 XrayEnabled,
 region
)
SELECT 
 '{{ AdditionalAuthenticationProviders }}',
 '{{ ApiType }}',
 '{{ AuthenticationType }}',
 '{{ EnhancedMetricsConfig }}',
 '{{ EnvironmentVariables }}',
 '{{ IntrospectionConfig }}',
 '{{ LambdaAuthorizerConfig }}',
 '{{ LogConfig }}',
 '{{ MergedApiExecutionRoleArn }}',
 '{{ Name }}',
 '{{ OpenIDConnectConfig }}',
 '{{ OwnerContact }}',
 '{{ QueryDepthLimit }}',
 '{{ ResolverCountLimit }}',
 '{{ Tags }}',
 '{{ UserPoolConfig }}',
 '{{ Visibility }}',
 '{{ XrayEnabled }}',
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
  - name: graphql_api
    props:
      - name: AdditionalAuthenticationProviders
        value:
          - LambdaAuthorizerConfig:
              IdentityValidationExpression: '{{ IdentityValidationExpression }}'
              AuthorizerUri: '{{ AuthorizerUri }}'
              AuthorizerResultTtlInSeconds: '{{ AuthorizerResultTtlInSeconds }}'
            OpenIDConnectConfig:
              ClientId: '{{ ClientId }}'
              AuthTTL: null
              Issuer: '{{ Issuer }}'
              IatTTL: null
            UserPoolConfig:
              AppIdClientRegex: '{{ AppIdClientRegex }}'
              UserPoolId: '{{ UserPoolId }}'
              AwsRegion: '{{ AwsRegion }}'
            AuthenticationType: '{{ AuthenticationType }}'
      - name: ApiType
        value: '{{ ApiType }}'
      - name: AuthenticationType
        value: '{{ AuthenticationType }}'
      - name: EnhancedMetricsConfig
        value:
          OperationLevelMetricsConfig: '{{ OperationLevelMetricsConfig }}'
          ResolverLevelMetricsBehavior: '{{ ResolverLevelMetricsBehavior }}'
          DataSourceLevelMetricsBehavior: '{{ DataSourceLevelMetricsBehavior }}'
      - name: EnvironmentVariables
        value: {}
      - name: IntrospectionConfig
        value: '{{ IntrospectionConfig }}'
      - name: LambdaAuthorizerConfig
        value: null
      - name: LogConfig
        value:
          ExcludeVerboseContent: '{{ ExcludeVerboseContent }}'
          FieldLogLevel: '{{ FieldLogLevel }}'
          CloudWatchLogsRoleArn: '{{ CloudWatchLogsRoleArn }}'
      - name: MergedApiExecutionRoleArn
        value: '{{ MergedApiExecutionRoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: OpenIDConnectConfig
        value: null
      - name: OwnerContact
        value: '{{ OwnerContact }}'
      - name: QueryDepthLimit
        value: '{{ QueryDepthLimit }}'
      - name: ResolverCountLimit
        value: '{{ ResolverCountLimit }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: UserPoolConfig
        value:
          AppIdClientRegex: '{{ AppIdClientRegex }}'
          UserPoolId: '{{ UserPoolId }}'
          AwsRegion: '{{ AwsRegion }}'
          DefaultAction: '{{ DefaultAction }}'
      - name: Visibility
        value: '{{ Visibility }}'
      - name: XrayEnabled
        value: '{{ XrayEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appsync.graphql_apis
WHERE data__Identifier = '<ApiId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>graphql_apis</code> resource, the following permissions are required:

### Create
```json
appsync:CreateGraphqlApi,
appsync:TagResource
```

### Read
```json
appsync:GetGraphqlApi,
appsync:GetGraphqlApiEnvironmentVariables,
appsync:ListTagsForResource
```

### Update
```json
appsync:GetGraphqlApi,
appsync:UpdateGraphqlApi,
appsync:TagResource,
appsync:UntagResource
```

### Delete
```json
appsync:DeleteGraphqlApi
```

### List
```json
appsync:ListGraphqlApis
```
