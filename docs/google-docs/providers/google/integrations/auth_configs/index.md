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
description,
certificateId,
name,
decryptedCredential,
visibility,
encryptedCredential,
creatorEmail,
lastModifierEmail,
reason,
validTime,
credentialType,
state,
displayName,
expiryNotificationDuration,
overrideValidTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ certificateId }}',
'{{ name }}',
'{{ decryptedCredential }}',
'{{ visibility }}',
'{{ encryptedCredential }}',
'{{ creatorEmail }}',
'{{ lastModifierEmail }}',
'{{ reason }}',
'{{ validTime }}',
'{{ credentialType }}',
'{{ state }}',
'{{ displayName }}',
'{{ expiryNotificationDuration }}',
'{{ overrideValidTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: string
    - name: certificateId
      value: string
    - name: name
      value: string
    - name: decryptedCredential
      value:
        - name: usernameAndPassword
          value:
            - name: password
              value: string
            - name: username
              value: string
        - name: oidcToken
          value:
            - name: tokenExpireTime
              value: string
            - name: token
              value: string
            - name: audience
              value: string
            - name: serviceAccountEmail
              value: string
        - name: oauth2ClientCredentials
          value:
            - name: scope
              value: string
            - name: clientSecret
              value: string
            - name: tokenParams
              value:
                - name: entries
                  value:
                    - - name: key
                        value:
                          - name: referenceKey
                            value: string
                          - name: literalValue
                            value:
                              - name: intArray
                                value:
                                  - name: intValues
                                    value:
                                      - string
                              - name: doubleArray
                                value:
                                  - name: doubleValues
                                    value:
                                      - number
                              - name: intValue
                                value: string
                              - name: stringArray
                                value:
                                  - name: stringValues
                                    value:
                                      - string
                              - name: doubleValue
                                value: number
                              - name: stringValue
                                value: string
                              - name: jsonValue
                                value: string
                              - name: booleanArray
                                value:
                                  - name: booleanValues
                                    value:
                                      - boolean
                              - name: booleanValue
                                value: boolean
                - name: keyType
                  value: string
                - name: valueType
                  value: string
            - name: clientId
              value: string
            - name: tokenEndpoint
              value: string
            - name: accessToken
              value:
                - name: accessTokenExpireTime
                  value: string
                - name: refreshToken
                  value: string
                - name: tokenType
                  value: string
                - name: accessToken
                  value: string
                - name: refreshTokenExpireTime
                  value: string
            - name: requestType
              value: string
        - name: oauth2ResourceOwnerCredentials
          value:
            - name: scope
              value: string
            - name: clientId
              value: string
            - name: username
              value: string
            - name: clientSecret
              value: string
            - name: password
              value: string
            - name: tokenEndpoint
              value: string
            - name: requestType
              value: string
        - name: credentialType
          value: string
        - name: oauth2AuthorizationCode
          value:
            - name: clientSecret
              value: string
            - name: requestType
              value: string
            - name: authCode
              value: string
            - name: scope
              value: string
            - name: authEndpoint
              value: string
            - name: tokenEndpoint
              value: string
            - name: applyReauthPolicy
              value: boolean
            - name: clientId
              value: string
        - name: serviceAccountCredentials
          value:
            - name: scope
              value: string
            - name: serviceAccount
              value: string
        - name: jwt
          value:
            - name: jwt
              value: string
            - name: secret
              value: string
            - name: jwtPayload
              value: string
            - name: jwtHeader
              value: string
        - name: authToken
          value:
            - name: type
              value: string
            - name: token
              value: string
    - name: visibility
      value: string
    - name: encryptedCredential
      value: string
    - name: creatorEmail
      value: string
    - name: lastModifierEmail
      value: string
    - name: reason
      value: string
    - name: validTime
      value: string
    - name: createTime
      value: string
    - name: credentialType
      value: string
    - name: state
      value: string
    - name: displayName
      value: string
    - name: expiryNotificationDuration
      value:
        - string
    - name: overrideValidTime
      value: string
    - name: updateTime
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>auth_configs</code> resource.

```sql
/*+ update */
UPDATE google.integrations.auth_configs
SET 
description = '{{ description }}',
certificateId = '{{ certificateId }}',
name = '{{ name }}',
decryptedCredential = '{{ decryptedCredential }}',
visibility = '{{ visibility }}',
encryptedCredential = '{{ encryptedCredential }}',
creatorEmail = '{{ creatorEmail }}',
lastModifierEmail = '{{ lastModifierEmail }}',
reason = '{{ reason }}',
validTime = '{{ validTime }}',
credentialType = '{{ credentialType }}',
state = '{{ state }}',
displayName = '{{ displayName }}',
expiryNotificationDuration = '{{ expiryNotificationDuration }}',
overrideValidTime = '{{ overrideValidTime }}'
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
