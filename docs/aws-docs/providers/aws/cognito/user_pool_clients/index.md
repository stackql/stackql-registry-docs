---
title: user_pool_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_clients
  - cognito
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

Creates, updates, deletes or gets an <code>user_pool_client</code> resource or lists <code>user_pool_clients</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolClient</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_clients" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="client_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="explicit_auth_flows" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="generate_secret" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="read_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_session_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="refresh_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="access_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="id_token_validity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="token_validity_units" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="write_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_flows" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_flows_user_pool_client" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="allowed_oauth_scopes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="callback_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_redirect_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logout_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="supported_identity_providers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="analytics_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="prevent_user_existence_errors" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_token_revocation" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_propagate_additional_user_context_data" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_secret" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html"><code>AWS::Cognito::UserPoolClient</code></a>.

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
    <td><CopyableCode code="UserPoolId, region" /></td>
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
Gets all <code>user_pool_clients</code> in a region.
```sql
SELECT
region,
client_name,
explicit_auth_flows,
generate_secret,
read_attributes,
auth_session_validity,
refresh_token_validity,
access_token_validity,
id_token_validity,
token_validity_units,
user_pool_id,
write_attributes,
allowed_oauth_flows,
allowed_oauth_flows_user_pool_client,
allowed_oauth_scopes,
callback_urls,
default_redirect_uri,
logout_urls,
supported_identity_providers,
analytics_configuration,
prevent_user_existence_errors,
enable_token_revocation,
enable_propagate_additional_user_context_data,
name,
client_secret,
client_id
FROM aws.cognito.user_pool_clients
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool_client</code>.
```sql
SELECT
region,
client_name,
explicit_auth_flows,
generate_secret,
read_attributes,
auth_session_validity,
refresh_token_validity,
access_token_validity,
id_token_validity,
token_validity_units,
user_pool_id,
write_attributes,
allowed_oauth_flows,
allowed_oauth_flows_user_pool_client,
allowed_oauth_scopes,
callback_urls,
default_redirect_uri,
logout_urls,
supported_identity_providers,
analytics_configuration,
prevent_user_existence_errors,
enable_token_revocation,
enable_propagate_additional_user_context_data,
name,
client_secret,
client_id
FROM aws.cognito.user_pool_clients
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<ClientId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_client</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_clients (
 UserPoolId,
 region
)
SELECT 
'{{ UserPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_clients (
 ClientName,
 ExplicitAuthFlows,
 GenerateSecret,
 ReadAttributes,
 AuthSessionValidity,
 RefreshTokenValidity,
 AccessTokenValidity,
 IdTokenValidity,
 TokenValidityUnits,
 UserPoolId,
 WriteAttributes,
 AllowedOAuthFlows,
 AllowedOAuthFlowsUserPoolClient,
 AllowedOAuthScopes,
 CallbackURLs,
 DefaultRedirectURI,
 LogoutURLs,
 SupportedIdentityProviders,
 AnalyticsConfiguration,
 PreventUserExistenceErrors,
 EnableTokenRevocation,
 EnablePropagateAdditionalUserContextData,
 region
)
SELECT 
 '{{ ClientName }}',
 '{{ ExplicitAuthFlows }}',
 '{{ GenerateSecret }}',
 '{{ ReadAttributes }}',
 '{{ AuthSessionValidity }}',
 '{{ RefreshTokenValidity }}',
 '{{ AccessTokenValidity }}',
 '{{ IdTokenValidity }}',
 '{{ TokenValidityUnits }}',
 '{{ UserPoolId }}',
 '{{ WriteAttributes }}',
 '{{ AllowedOAuthFlows }}',
 '{{ AllowedOAuthFlowsUserPoolClient }}',
 '{{ AllowedOAuthScopes }}',
 '{{ CallbackURLs }}',
 '{{ DefaultRedirectURI }}',
 '{{ LogoutURLs }}',
 '{{ SupportedIdentityProviders }}',
 '{{ AnalyticsConfiguration }}',
 '{{ PreventUserExistenceErrors }}',
 '{{ EnableTokenRevocation }}',
 '{{ EnablePropagateAdditionalUserContextData }}',
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
  - name: user_pool_client
    props:
      - name: ClientName
        value: '{{ ClientName }}'
      - name: ExplicitAuthFlows
        value:
          - '{{ ExplicitAuthFlows[0] }}'
      - name: GenerateSecret
        value: '{{ GenerateSecret }}'
      - name: ReadAttributes
        value:
          - '{{ ReadAttributes[0] }}'
      - name: AuthSessionValidity
        value: '{{ AuthSessionValidity }}'
      - name: RefreshTokenValidity
        value: '{{ RefreshTokenValidity }}'
      - name: AccessTokenValidity
        value: '{{ AccessTokenValidity }}'
      - name: IdTokenValidity
        value: '{{ IdTokenValidity }}'
      - name: TokenValidityUnits
        value:
          AccessToken: '{{ AccessToken }}'
          IdToken: '{{ IdToken }}'
          RefreshToken: '{{ RefreshToken }}'
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: WriteAttributes
        value:
          - '{{ WriteAttributes[0] }}'
      - name: AllowedOAuthFlows
        value:
          - '{{ AllowedOAuthFlows[0] }}'
      - name: AllowedOAuthFlowsUserPoolClient
        value: '{{ AllowedOAuthFlowsUserPoolClient }}'
      - name: AllowedOAuthScopes
        value:
          - '{{ AllowedOAuthScopes[0] }}'
      - name: CallbackURLs
        value:
          - '{{ CallbackURLs[0] }}'
      - name: DefaultRedirectURI
        value: '{{ DefaultRedirectURI }}'
      - name: LogoutURLs
        value:
          - '{{ LogoutURLs[0] }}'
      - name: SupportedIdentityProviders
        value:
          - '{{ SupportedIdentityProviders[0] }}'
      - name: AnalyticsConfiguration
        value:
          ApplicationArn: '{{ ApplicationArn }}'
          ApplicationId: '{{ ApplicationId }}'
          ExternalId: '{{ ExternalId }}'
          RoleArn: '{{ RoleArn }}'
          UserDataShared: '{{ UserDataShared }}'
      - name: PreventUserExistenceErrors
        value: '{{ PreventUserExistenceErrors }}'
      - name: EnableTokenRevocation
        value: '{{ EnableTokenRevocation }}'
      - name: EnablePropagateAdditionalUserContextData
        value: '{{ EnablePropagateAdditionalUserContextData }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pool_clients
WHERE data__Identifier = '<UserPoolId|ClientId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_clients</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateUserPoolClient,
iam:PassRole,
iam:PutRolePolicy,
iam:CreateServiceLinkedRole
```

### Read
```json
cognito-idp:DescribeUserPoolClient
```

### Update
```json
cognito-idp:UpdateUserPoolClient,
iam:PassRole,
iam:PutRolePolicy
```

### Delete
```json
cognito-idp:DeleteUserPoolClient,
iam:PutRolePolicy,
iam:DeleteRolePolicy
```

### List
```json
cognito-idp:ListUserPoolClients
```
