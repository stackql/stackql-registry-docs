---
title: authorizers
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizers
  - apigateway
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

Creates, updates, deletes or gets an <code>authorizer</code> resource or lists <code>authorizers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Authorizer</code> resource creates an authorization layer that API Gateway activates for methods that have authorization enabled. API Gateway activates the authorizer when a client calls those methods.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.authorizers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_credentials" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_result_ttl_in_seconds" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_source" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_validation_expression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provider_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html"><code>AWS::ApiGateway::Authorizer</code></a>.

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
    <td><CopyableCode code="RestApiId, Type, Name, region" /></td>
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
Gets all <code>authorizers</code> in a region.
```sql
SELECT
region,
rest_api_id,
authorizer_id,
auth_type,
authorizer_credentials,
authorizer_result_ttl_in_seconds,
authorizer_uri,
identity_source,
identity_validation_expression,
name,
provider_arns,
type
FROM aws.apigateway.authorizers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>authorizer</code>.
```sql
SELECT
region,
rest_api_id,
authorizer_id,
auth_type,
authorizer_credentials,
authorizer_result_ttl_in_seconds,
authorizer_uri,
identity_source,
identity_validation_expression,
name,
provider_arns,
type
FROM aws.apigateway.authorizers
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>|<AuthorizerId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorizer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 Name,
 Type,
 region
)
SELECT 
'{{ RestApiId }}',
 '{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigateway.authorizers (
 RestApiId,
 AuthType,
 AuthorizerCredentials,
 AuthorizerResultTtlInSeconds,
 AuthorizerUri,
 IdentitySource,
 IdentityValidationExpression,
 Name,
 ProviderARNs,
 Type,
 region
)
SELECT 
 '{{ RestApiId }}',
 '{{ AuthType }}',
 '{{ AuthorizerCredentials }}',
 '{{ AuthorizerResultTtlInSeconds }}',
 '{{ AuthorizerUri }}',
 '{{ IdentitySource }}',
 '{{ IdentityValidationExpression }}',
 '{{ Name }}',
 '{{ ProviderARNs }}',
 '{{ Type }}',
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
  - name: authorizer
    props:
      - name: RestApiId
        value: '{{ RestApiId }}'
      - name: AuthType
        value: '{{ AuthType }}'
      - name: AuthorizerCredentials
        value: '{{ AuthorizerCredentials }}'
      - name: AuthorizerResultTtlInSeconds
        value: '{{ AuthorizerResultTtlInSeconds }}'
      - name: AuthorizerUri
        value: '{{ AuthorizerUri }}'
      - name: IdentitySource
        value: '{{ IdentitySource }}'
      - name: IdentityValidationExpression
        value: '{{ IdentityValidationExpression }}'
      - name: Name
        value: '{{ Name }}'
      - name: ProviderARNs
        value:
          - '{{ ProviderARNs[0] }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigateway.authorizers
WHERE data__Identifier = '<RestApiId|AuthorizerId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>authorizers</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
iam:PassRole
```

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
iam:PassRole
```

### Delete
```json
apigateway:DELETE
```

### List
```json
apigateway:GET
```
