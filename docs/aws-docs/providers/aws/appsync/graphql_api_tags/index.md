---
title: graphql_api_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - graphql_api_tags
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

Expands all tag keys and values for <code>graphql_apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphql_api_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppSync::GraphQLApi</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.graphql_api_tags" /></td></tr>
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
<tr><td><CopyableCode code="user_pool_config" /></td><td><code>object</code></td><td>Optional authorization configuration for using Amazon Cognito user pools with your GraphQL endpoint.<br /></td></tr>
<tr><td><CopyableCode code="visibility" /></td><td><code>string</code></td><td>Sets the scope of the GraphQL API to public (GLOBAL) or private (PRIVATE). By default, the scope is set to Global if no value is provided.</td></tr>
<tr><td><CopyableCode code="xray_enabled" /></td><td><code>boolean</code></td><td>A flag indicating whether to use AWS X-Ray tracing for this GraphqlApi.<br /></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>graphql_apis</code> in a region.
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
user_pool_config,
visibility,
xray_enabled,
tag_key,
tag_value
FROM aws.appsync.graphql_api_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>graphql_api_tags</code> resource, see <a href="/providers/aws/appsync/graphql_apis/#permissions"><code>graphql_apis</code></a>

