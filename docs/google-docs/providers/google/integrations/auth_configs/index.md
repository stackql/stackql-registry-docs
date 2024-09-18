---
title: auth_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_configs
  - integrations
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>auth_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.auth_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the auth config. For more information, see Manage authentication profiles. projects/{project}/locations/{location}/authConfigs/{authConfig}. |
| <CopyableCode code="description" /> | `string` | A description of the auth config. |
| <CopyableCode code="certificateId" /> | `string` | Certificate id for client certificate |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the auth config is created. |
| <CopyableCode code="creatorEmail" /> | `string` | The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| <CopyableCode code="credentialType" /> | `string` | Credential type of the encrypted credential. |
| <CopyableCode code="decryptedCredential" /> | `object` | Defines parameters for a single, canonical credential. |
| <CopyableCode code="displayName" /> | `string` | Required. The name of the auth config. |
| <CopyableCode code="encryptedCredential" /> | `string` | Auth credential encrypted by Cloud KMS. Can be decrypted as Credential with proper KMS key. |
| <CopyableCode code="expiryNotificationDuration" /> | `array` | User can define the time to receive notification after which the auth config becomes invalid. Support up to 30 days. Support granularity in hours. |
| <CopyableCode code="lastModifierEmail" /> | `string` | The last modifier's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| <CopyableCode code="overrideValidTime" /> | `string` | User provided expiry time to override. For the example of Salesforce, username/password credentials can be valid for 6 months depending on the instance settings. |
| <CopyableCode code="reason" /> | `string` | The reason / details of the current status. |
| <CopyableCode code="state" /> | `string` | The status of the auth config. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the auth config is modified. |
| <CopyableCode code="validTime" /> | `string` | The time until the auth config is valid. Empty or max value is considered the auth config won't expire. |
| <CopyableCode code="visibility" /> | `string` | The visibility of the auth config. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_auth_configs_get" /> | `SELECT` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| <CopyableCode code="projects_locations_auth_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="projects_locations_products_auth_configs_get" /> | `SELECT` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Gets a complete auth config. If the auth config doesn't exist, Code.NOT_FOUND exception will be thrown. Returns the decrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only. |
| <CopyableCode code="projects_locations_auth_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates an auth config record. Fetch corresponding credentials for specific auth types, e.g. access token for OAuth 2.0, JWT token for JWT. Encrypt the auth config with Cloud KMS and store the encrypted credentials in Spanner. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_auth_configs_delete" /> | `DELETE` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Deletes an auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_delete" /> | `DELETE` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Deletes an auth config. |
| <CopyableCode code="projects_locations_auth_configs_patch" /> | `UPDATE` | <CopyableCode code="authConfigsId, locationsId, projectsId" /> | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |
| <CopyableCode code="projects_locations_products_auth_configs_patch" /> | `UPDATE` | <CopyableCode code="authConfigsId, locationsId, productsId, projectsId" /> | Updates an auth config. If credential is updated, fetch the encrypted auth config from Spanner, decrypt with Cloud KMS key, update the credential fields, re-encrypt with Cloud KMS key and update the Spanner record. For other fields, directly update the Spanner record. Returns the encrypted auth config. |

## `SELECT` examples

Lists all auth configs that match the filter. Restrict to auth configs belong to the current client only.

```sql
SELECT
name,
description,
certificateId,
createTime,
creatorEmail,
credentialType,
decryptedCredential,
displayName,
encryptedCredential,
expiryNotificationDuration,
lastModifierEmail,
overrideValidTime,
reason,
state,
updateTime,
validTime,
visibility
FROM google.integrations.auth_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>auth_configs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.integrations.auth_configs (
locationsId,
projectsId,
reason,
visibility,
displayName,
encryptedCredential,
name,
description,
creatorEmail,
credentialType,
validTime,
state,
lastModifierEmail,
overrideValidTime,
expiryNotificationDuration,
certificateId,
decryptedCredential
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ reason }}',
'{{ visibility }}',
'{{ displayName }}',
'{{ encryptedCredential }}',
'{{ name }}',
'{{ description }}',
'{{ creatorEmail }}',
'{{ credentialType }}',
'{{ validTime }}',
'{{ state }}',
'{{ lastModifierEmail }}',
'{{ overrideValidTime }}',
'{{ expiryNotificationDuration }}',
'{{ certificateId }}',
'{{ decryptedCredential }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
reason: string
visibility: string
displayName: string
encryptedCredential: string
name: string
description: string
creatorEmail: string
credentialType: string
validTime: string
state: string
lastModifierEmail: string
overrideValidTime: string
expiryNotificationDuration:
  - type: string
    format: string
createTime: string
updateTime: string
certificateId: string
decryptedCredential:
  credentialType: string
  serviceAccountCredentials:
    serviceAccount: string
    scope: string
  authToken:
    token: string
    type: string
  oauth2ClientCredentials:
    accessToken:
      accessToken: string
      refreshTokenExpireTime: string
      tokenType: string
      refreshToken: string
      accessTokenExpireTime: string
    tokenEndpoint: string
    clientId: string
    clientSecret: string
    tokenParams:
      entries:
        - value:
            literalValue:
              stringValue: string
              doubleValue: number
              jsonValue: string
              booleanArray:
                booleanValues:
                  - type: string
              booleanValue: boolean
              intValue: string
              stringArray:
                stringValues:
                  - type: string
              intArray:
                intValues:
                  - type: string
                    format: string
              doubleArray:
                doubleValues:
                  - format: string
                    type: string
            referenceKey: string
      keyType: string
      valueType: string
    requestType: string
    scope: string
  oauth2AuthorizationCode:
    authCode: string
    clientId: string
    scope: string
    clientSecret: string
    applyReauthPolicy: boolean
    authEndpoint: string
    tokenEndpoint: string
    requestType: string
  jwt:
    jwtHeader: string
    secret: string
    jwt: string
    jwtPayload: string
  oidcToken:
    tokenExpireTime: string
    audience: string
    serviceAccountEmail: string
    token: string
  oauth2ResourceOwnerCredentials:
    scope: string
    requestType: string
    clientId: string
    username: string
    password: string
    clientSecret: string
    tokenEndpoint: string
  usernameAndPassword:
    username: string
    password: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>auth_configs</code> resource.

```sql
/*+ update */
UPDATE google.integrations.auth_configs
SET 
reason = '{{ reason }}',
visibility = '{{ visibility }}',
displayName = '{{ displayName }}',
encryptedCredential = '{{ encryptedCredential }}',
name = '{{ name }}',
description = '{{ description }}',
creatorEmail = '{{ creatorEmail }}',
credentialType = '{{ credentialType }}',
validTime = '{{ validTime }}',
state = '{{ state }}',
lastModifierEmail = '{{ lastModifierEmail }}',
overrideValidTime = '{{ overrideValidTime }}',
expiryNotificationDuration = '{{ expiryNotificationDuration }}',
certificateId = '{{ certificateId }}',
decryptedCredential = '{{ decryptedCredential }}'
WHERE 
authConfigsId = '{{ authConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>auth_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.integrations.auth_configs
WHERE authConfigsId = '{{ authConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
