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


Used to retrieve a list of <code>user_pool_clients</code> in a region or to create or delete a <code>user_pool_clients</code> resource, use <code>user_pool_client</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolClient</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_clients" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
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
user_pool_id,
client_id
FROM aws.cognito.user_pool_clients
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "UserPoolId": "{{ UserPoolId }}"
}
>>>
--required properties only
INSERT INTO aws.cognito.user_pool_clients (
 UserPoolId,
 region
)
SELECT 
{{ .UserPoolId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClientName": "{{ ClientName }}",
 "ExplicitAuthFlows": [
  "{{ ExplicitAuthFlows[0] }}"
 ],
 "GenerateSecret": "{{ GenerateSecret }}",
 "ReadAttributes": [
  "{{ ReadAttributes[0] }}"
 ],
 "AuthSessionValidity": "{{ AuthSessionValidity }}",
 "RefreshTokenValidity": "{{ RefreshTokenValidity }}",
 "AccessTokenValidity": "{{ AccessTokenValidity }}",
 "IdTokenValidity": "{{ IdTokenValidity }}",
 "TokenValidityUnits": {
  "AccessToken": "{{ AccessToken }}",
  "IdToken": "{{ IdToken }}",
  "RefreshToken": "{{ RefreshToken }}"
 },
 "UserPoolId": "{{ UserPoolId }}",
 "WriteAttributes": [
  "{{ WriteAttributes[0] }}"
 ],
 "AllowedOAuthFlows": [
  "{{ AllowedOAuthFlows[0] }}"
 ],
 "AllowedOAuthFlowsUserPoolClient": "{{ AllowedOAuthFlowsUserPoolClient }}",
 "AllowedOAuthScopes": [
  "{{ AllowedOAuthScopes[0] }}"
 ],
 "CallbackURLs": [
  "{{ CallbackURLs[0] }}"
 ],
 "DefaultRedirectURI": "{{ DefaultRedirectURI }}",
 "LogoutURLs": [
  "{{ LogoutURLs[0] }}"
 ],
 "SupportedIdentityProviders": [
  "{{ SupportedIdentityProviders[0] }}"
 ],
 "AnalyticsConfiguration": {
  "ApplicationArn": "{{ ApplicationArn }}",
  "ApplicationId": "{{ ApplicationId }}",
  "ExternalId": "{{ ExternalId }}",
  "RoleArn": "{{ RoleArn }}",
  "UserDataShared": "{{ UserDataShared }}"
 },
 "PreventUserExistenceErrors": "{{ PreventUserExistenceErrors }}",
 "EnableTokenRevocation": "{{ EnableTokenRevocation }}",
 "EnablePropagateAdditionalUserContextData": "{{ EnablePropagateAdditionalUserContextData }}"
}
>>>
--all properties
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
 {{ .ClientName }},
 {{ .ExplicitAuthFlows }},
 {{ .GenerateSecret }},
 {{ .ReadAttributes }},
 {{ .AuthSessionValidity }},
 {{ .RefreshTokenValidity }},
 {{ .AccessTokenValidity }},
 {{ .IdTokenValidity }},
 {{ .TokenValidityUnits }},
 {{ .UserPoolId }},
 {{ .WriteAttributes }},
 {{ .AllowedOAuthFlows }},
 {{ .AllowedOAuthFlowsUserPoolClient }},
 {{ .AllowedOAuthScopes }},
 {{ .CallbackURLs }},
 {{ .DefaultRedirectURI }},
 {{ .LogoutURLs }},
 {{ .SupportedIdentityProviders }},
 {{ .AnalyticsConfiguration }},
 {{ .PreventUserExistenceErrors }},
 {{ .EnableTokenRevocation }},
 {{ .EnablePropagateAdditionalUserContextData }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

