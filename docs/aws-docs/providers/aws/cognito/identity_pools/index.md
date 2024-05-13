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
    <td><CopyableCode code="AllowUnauthenticatedIdentities, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>identity_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.identity_pools (
 AllowUnauthenticatedIdentities,
 region
)
SELECT 
'{{ AllowUnauthenticatedIdentities }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ PushSync }}',
 '{{ CognitoIdentityProviders }}',
 '{{ DeveloperProviderName }}',
 '{{ CognitoStreams }}',
 '{{ SupportedLoginProviders }}',
 '{{ CognitoEvents }}',
 '{{ IdentityPoolName }}',
 '{{ AllowUnauthenticatedIdentities }}',
 '{{ SamlProviderARNs }}',
 '{{ OpenIdConnectProviderARNs }}',
 '{{ AllowClassicFlow }}',
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
  - name: identity_pool
    props:
      - name: PushSync
        value:
          ApplicationArns:
            - '{{ ApplicationArns[0] }}'
          RoleArn: '{{ RoleArn }}'
      - name: CognitoIdentityProviders
        value:
          - ServerSideTokenCheck: '{{ ServerSideTokenCheck }}'
            ProviderName: '{{ ProviderName }}'
            ClientId: '{{ ClientId }}'
      - name: DeveloperProviderName
        value: '{{ DeveloperProviderName }}'
      - name: CognitoStreams
        value:
          StreamingStatus: '{{ StreamingStatus }}'
          StreamName: '{{ StreamName }}'
          RoleArn: '{{ RoleArn }}'
      - name: SupportedLoginProviders
        value: {}
      - name: CognitoEvents
        value: {}
      - name: IdentityPoolName
        value: '{{ IdentityPoolName }}'
      - name: AllowUnauthenticatedIdentities
        value: '{{ AllowUnauthenticatedIdentities }}'
      - name: SamlProviderARNs
        value:
          - '{{ SamlProviderARNs[0] }}'
      - name: OpenIdConnectProviderARNs
        value:
          - '{{ OpenIdConnectProviderARNs[0] }}'
      - name: AllowClassicFlow
        value: '{{ AllowClassicFlow }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

