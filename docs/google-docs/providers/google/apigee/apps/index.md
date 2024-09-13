---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apigee
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

Creates, updates, deletes or gets an <code>app</code> resource or lists <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the AppGroup app whose resource name format is of syntax (organizations/*/appgroups/*/apps/*). |
| <CopyableCode code="apiProducts" /> | `array` | List of API products associated with the AppGroup app. |
| <CopyableCode code="appGroup" /> | `string` | Immutable. Name of the parent AppGroup whose resource name format is of syntax (organizations/*/appgroups/*). |
| <CopyableCode code="appId" /> | `string` | Immutable. ID of the AppGroup app. |
| <CopyableCode code="attributes" /> | `array` | List of attributes for the AppGroup app. |
| <CopyableCode code="callbackUrl" /> | `string` | Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to AppGroup apps. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time the AppGroup app was created in milliseconds since epoch. |
| <CopyableCode code="credentials" /> | `array` | Output only. Set of credentials for the AppGroup app consisting of the consumer key/secret pairs associated with the API products. |
| <CopyableCode code="keyExpiresIn" /> | `string` | Immutable. Expiration time, in seconds, for the consumer key that is generated for the AppGroup app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time the AppGroup app was modified in milliseconds since epoch. |
| <CopyableCode code="scopes" /> | `array` | Scopes to apply to the AppGroup app. The specified scopes must already exist for the API product that you associate with the AppGroup app. |
| <CopyableCode code="status" /> | `string` | Status of the App. Valid values include `approved` or `revoked`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_appgroups_apps_get" /> | `SELECT` | <CopyableCode code="appgroupsId, appsId, organizationsId" /> | Returns the details for an AppGroup app. |
| <CopyableCode code="organizations_appgroups_apps_list" /> | `SELECT` | <CopyableCode code="appgroupsId, organizationsId" /> | Lists all apps created by an AppGroup in an Apigee organization. Optionally, you can request an expanded view of the AppGroup apps. Lists all AppGroupApps in an AppGroup. A maximum of 1000 AppGroup apps are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000. |
| <CopyableCode code="organizations_apps_get" /> | `SELECT` | <CopyableCode code="appsId, organizationsId" /> | Gets the app profile for the specified app ID. |
| <CopyableCode code="organizations_apps_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company). |
| <CopyableCode code="organizations_developers_apps_get" /> | `SELECT` | <CopyableCode code="appsId, developersId, organizationsId" /> | Returns the details for a developer app. |
| <CopyableCode code="organizations_developers_apps_list" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Lists all apps created by a developer in an Apigee organization. Optionally, you can request an expanded view of the developer apps. A maximum of 100 developer apps are returned per API call. You can paginate the list of deveoper apps returned using the `startKey` and `count` query parameters. |
| <CopyableCode code="organizations_appgroups_apps_create" /> | `INSERT` | <CopyableCode code="appgroupsId, organizationsId" /> | Creates an app and associates it with an AppGroup. This API associates the AppGroup app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The `name` is the unique ID of the app that you can use in API calls. |
| <CopyableCode code="organizations_developers_apps_create" /> | `INSERT` | <CopyableCode code="developersId, organizationsId" /> | Creates an app associated with a developer. This API associates the developer app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The `name` is the unique ID of the app that you can use in API calls. The `DisplayName` (set as an attribute) appears in the UI. If you don't set the `DisplayName` attribute, the `name` appears in the UI. |
| <CopyableCode code="organizations_appgroups_apps_delete" /> | `DELETE` | <CopyableCode code="appgroupsId, appsId, organizationsId" /> | Deletes an AppGroup app. **Note**: The delete operation is asynchronous. The AppGroup app is deleted immediately, but its associated resources, such as app keys or access tokens, may take anywhere from a few seconds to a few minutes to be deleted. |
| <CopyableCode code="organizations_developers_apps_delete" /> | `DELETE` | <CopyableCode code="appsId, developersId, organizationsId" /> | Deletes a developer app. **Note**: The delete operation is asynchronous. The developer app is deleted immediately, but its associated resources, such as app keys or access tokens, may take anywhere from a few seconds to a few minutes to be deleted. |
| <CopyableCode code="organizations_appgroups_apps_update" /> | `EXEC` | <CopyableCode code="appgroupsId, appsId, organizationsId" /> | Updates the details for an AppGroup app. In addition, you can add an API product to an AppGroup app and automatically generate an API key for the app to use when calling APIs in the API product. If you want to use an existing API key for the API product, add the API product to the API key using the UpdateAppGroupAppKey API. Using this API, you cannot update the app name, as it is the primary key used to identify the app and cannot be changed. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. |
| <CopyableCode code="organizations_developers_apps_attributes" /> | `EXEC` | <CopyableCode code="appsId, developersId, organizationsId" /> | Updates attributes for a developer app. This API replaces the current attributes with those specified in the request. |
| <CopyableCode code="organizations_developers_apps_generate_key_pair_or_update_developer_app_status" /> | `EXEC` | <CopyableCode code="appsId, developersId, organizationsId" /> | Manages access to a developer app by enabling you to: * Approve or revoke a developer app * Generate a new consumer key and secret for a developer app To approve or revoke a developer app, set the `action` query parameter to `approve` or `revoke`, respectively, and the `Content-Type` header to `application/octet-stream`. If a developer app is revoked, none of its API keys are valid for API calls even though the keys are still approved. If successful, the API call returns the following HTTP status code: `204 No Content` To generate a new consumer key and secret for a developer app, pass the new key/secret details. Rather than replace an existing key, this API generates a new key. In this case, multiple key pairs may be associated with a single developer app. Each key pair has an independent status (`approve` or `revoke`) and expiration time. Any approved, non-expired key can be used in an API call. For example, if you're using API key rotation, you can generate new keys with expiration times that overlap keys that are going to expire. You might also generate a new consumer key/secret if the security of the original key/secret is compromised. The `keyExpiresIn` property defines the expiration time for the API key in milliseconds. If you don't set this property or set it to `-1`, the API key never expires. **Notes**: * When generating a new key/secret, this API replaces the existing attributes, notes, and callback URLs with those specified in the request. Include or exclude any existing information that you want to retain or delete, respectively. * To migrate existing consumer keys and secrets to hybrid from another system, see the CreateDeveloperAppKey API. |
| <CopyableCode code="organizations_developers_apps_update" /> | `EXEC` | <CopyableCode code="appsId, developersId, organizationsId" /> | Updates the details for a developer app. In addition, you can add an API product to a developer app and automatically generate an API key for the app to use when calling APIs in the API product. If you want to use an existing API key for the API product, add the API product to the API key using the UpdateDeveloperAppKey API. Using this API, you cannot update the following: * App name as it is the primary key used to identify the app and cannot be changed. * Scopes associated with the app. Instead, use the ReplaceDeveloperAppKey API. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. |

## `SELECT` examples

Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company).

```sql
SELECT
name,
apiProducts,
appGroup,
appId,
attributes,
callbackUrl,
createdAt,
credentials,
keyExpiresIn,
lastModifiedAt,
scopes,
status
FROM google.apigee.apps
WHERE organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps</code> resource.

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
INSERT INTO google.apigee.apps (
appgroupsId,
organizationsId,
createdAt,
apiProducts,
attributes,
keyExpiresIn,
appGroup,
credentials,
scopes,
status,
name,
lastModifiedAt,
callbackUrl,
appId
)
SELECT 
'{{ appgroupsId }}',
'{{ organizationsId }}',
'{{ createdAt }}',
'{{ apiProducts }}',
'{{ attributes }}',
'{{ keyExpiresIn }}',
'{{ appGroup }}',
'{{ credentials }}',
'{{ scopes }}',
'{{ status }}',
'{{ name }}',
'{{ lastModifiedAt }}',
'{{ callbackUrl }}',
'{{ appId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: createdAt
        value: '{{ createdAt }}'
      - name: apiProducts
        value: '{{ apiProducts }}'
      - name: attributes
        value: '{{ attributes }}'
      - name: keyExpiresIn
        value: '{{ keyExpiresIn }}'
      - name: appGroup
        value: '{{ appGroup }}'
      - name: credentials
        value: '{{ credentials }}'
      - name: scopes
        value: '{{ scopes }}'
      - name: status
        value: '{{ status }}'
      - name: name
        value: '{{ name }}'
      - name: lastModifiedAt
        value: '{{ lastModifiedAt }}'
      - name: callbackUrl
        value: '{{ callbackUrl }}'
      - name: appId
        value: '{{ appId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified app resource.

```sql
DELETE FROM google.apigee.apps
WHERE appgroupsId = '{{ appgroupsId }}'
AND appsId = '{{ appsId }}'
AND organizationsId = '{{ organizationsId }}';
```
