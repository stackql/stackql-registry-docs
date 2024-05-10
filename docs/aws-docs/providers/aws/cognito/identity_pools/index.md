---
title: identity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pools
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


Used to retrieve a list of <code>identity_pools</code> in a region or to create or delete a <code>identity_pools</code> resource, use <code>identity_pool</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::IdentityPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.identity_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
id
FROM aws.cognito.identity_pools
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
 "AllowUnauthenticatedIdentities": "{{ AllowUnauthenticatedIdentities }}"
}
>>>
--required properties only
INSERT INTO aws.cognito.identity_pools (
 AllowUnauthenticatedIdentities,
 region
)
SELECT 
{{ AllowUnauthenticatedIdentities }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PushSync": {
  "ApplicationArns": [
   "{{ ApplicationArns[0] }}"
  ],
  "RoleArn": "{{ RoleArn }}"
 },
 "CognitoIdentityProviders": [
  {
   "ServerSideTokenCheck": "{{ ServerSideTokenCheck }}",
   "ProviderName": "{{ ProviderName }}",
   "ClientId": "{{ ClientId }}"
  }
 ],
 "DeveloperProviderName": "{{ DeveloperProviderName }}",
 "CognitoStreams": {
  "StreamingStatus": "{{ StreamingStatus }}",
  "StreamName": "{{ StreamName }}",
  "RoleArn": "{{ RoleArn }}"
 },
 "SupportedLoginProviders": {},
 "CognitoEvents": {},
 "IdentityPoolName": "{{ IdentityPoolName }}",
 "AllowUnauthenticatedIdentities": "{{ AllowUnauthenticatedIdentities }}",
 "SamlProviderARNs": [
  "{{ SamlProviderARNs[0] }}"
 ],
 "OpenIdConnectProviderARNs": [
  "{{ OpenIdConnectProviderARNs[0] }}"
 ],
 "AllowClassicFlow": "{{ AllowClassicFlow }}"
}
>>>
--all properties
INSERT INTO aws.cognito.identity_pools (
 PushSync,
 CognitoIdentityProviders,
 DeveloperProviderName,
 CognitoStreams,
 SupportedLoginProviders,
 CognitoEvents,
 IdentityPoolName,
 AllowUnauthenticatedIdentities,
 SamlProviderARNs,
 OpenIdConnectProviderARNs,
 AllowClassicFlow,
 region
)
SELECT 
 {{ PushSync }},
 {{ CognitoIdentityProviders }},
 {{ DeveloperProviderName }},
 {{ CognitoStreams }},
 {{ SupportedLoginProviders }},
 {{ CognitoEvents }},
 {{ IdentityPoolName }},
 {{ AllowUnauthenticatedIdentities }},
 {{ SamlProviderARNs }},
 {{ OpenIdConnectProviderARNs }},
 {{ AllowClassicFlow }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cognito.identity_pools
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>identity_pools</code> resource, the following permissions are required:

### Create
```json
cognito-identity:CreateIdentityPool,
cognito-sync:SetIdentityPoolConfiguration,
cognito-sync:SetCognitoEvents,
iam:PassRole
```

### Delete
```json
cognito-identity:DeleteIdentityPool
```

### List
```json
cognito-identity:ListIdentityPools
```

