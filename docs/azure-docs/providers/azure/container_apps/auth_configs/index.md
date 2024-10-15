---
title: auth_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_configs
  - container_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.auth_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | AuthConfig resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authConfigName, containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_container_app" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authConfigName, containerAppName, resourceGroupName, subscriptionId" /> | Create or update the AuthConfig for a Container App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authConfigName, containerAppName, resourceGroupName, subscriptionId" /> | Delete a Container App AuthConfig. |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.auth_configs
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.container_apps.auth_configs (
authConfigName,
containerAppName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ authConfigName }}',
'{{ containerAppName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: platform
          value:
            - name: enabled
              value: boolean
            - name: runtimeVersion
              value: string
        - name: globalValidation
          value:
            - name: unauthenticatedClientAction
              value: string
            - name: redirectToProvider
              value: string
            - name: excludedPaths
              value:
                - string
        - name: identityProviders
          value:
            - name: azureActiveDirectory
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: openIdIssuer
                      value: string
                    - name: clientId
                      value: string
                    - name: clientSecretSettingName
                      value: string
                    - name: clientSecretCertificateThumbprint
                      value: string
                    - name: clientSecretCertificateSubjectAlternativeName
                      value: string
                    - name: clientSecretCertificateIssuer
                      value: string
                - name: login
                  value:
                    - name: loginParameters
                      value:
                        - string
                    - name: disableWWWAuthenticate
                      value: boolean
                - name: validation
                  value:
                    - name: jwtClaimChecks
                      value:
                        - name: allowedGroups
                          value:
                            - string
                        - name: allowedClientApplications
                          value:
                            - string
                    - name: allowedAudiences
                      value:
                        - string
                    - name: defaultAuthorizationPolicy
                      value:
                        - name: allowedPrincipals
                          value:
                            - name: groups
                              value:
                                - string
                            - name: identities
                              value:
                                - string
                        - name: allowedApplications
                          value:
                            - string
                - name: isAutoProvisioned
                  value: boolean
            - name: facebook
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: appId
                      value: string
                    - name: appSecretSettingName
                      value: string
                - name: graphApiVersion
                  value: string
                - name: login
                  value:
                    - name: scopes
                      value:
                        - string
            - name: gitHub
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: clientId
                      value: string
                    - name: clientSecretSettingName
                      value: string
            - name: google
              value:
                - name: enabled
                  value: boolean
                - name: validation
                  value:
                    - name: allowedAudiences
                      value:
                        - string
            - name: twitter
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: consumerKey
                      value: string
                    - name: consumerSecretSettingName
                      value: string
            - name: apple
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: clientId
                      value: string
                    - name: clientSecretSettingName
                      value: string
            - name: azureStaticWebApps
              value:
                - name: enabled
                  value: boolean
                - name: registration
                  value:
                    - name: clientId
                      value: string
            - name: customOpenIdConnectProviders
              value: object
        - name: login
          value:
            - name: routes
              value:
                - name: logoutEndpoint
                  value: string
            - name: tokenStore
              value:
                - name: enabled
                  value: boolean
                - name: tokenRefreshExtensionHours
                  value: number
                - name: azureBlobStorage
                  value:
                    - name: sasUrlSettingName
                      value: string
            - name: preserveUrlFragmentsForLogins
              value: boolean
            - name: allowedExternalRedirectUrls
              value:
                - string
            - name: cookieExpiration
              value:
                - name: convention
                  value: string
                - name: timeToExpiration
                  value: string
            - name: nonce
              value:
                - name: validateNonce
                  value: boolean
                - name: nonceExpirationInterval
                  value: string
        - name: httpSettings
          value:
            - name: requireHttps
              value: boolean
            - name: routes
              value:
                - name: apiPrefix
                  value: string
            - name: forwardProxy
              value:
                - name: convention
                  value: string
                - name: customHostHeaderName
                  value: string
                - name: customProtoHeaderName
                  value: string
        - name: encryptionSettings
          value:
            - name: containerAppAuthEncryptionSecretName
              value: string
            - name: containerAppAuthSigningSecretName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>auth_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.auth_configs
WHERE authConfigName = '{{ authConfigName }}'
AND containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
