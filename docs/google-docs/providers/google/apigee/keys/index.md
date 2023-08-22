---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `consumerKey` | `string` | Immutable. Consumer key. |
| `scopes` | `array` | Scopes to apply to the app. The specified scope names must already be defined for the API product that you associate with the app. |
| `attributes` | `array` | List of attributes associated with the credential. |
| `issuedAt` | `string` | Output only. Time the AppGroup app was created in milliseconds since epoch. |
| `status` | `string` | Status of the credential. Valid values include `approved` or `revoked`. |
| `consumerSecret` | `string` | Secret key. |
| `expiresAt` | `string` | Output only. Time the AppGroup app expires in milliseconds since epoch. |
| `apiProducts` | `array` | Output only. List of API products and its status for which the credential can be used. **Note**: Use UpdateAppGroupAppKeyApiProductRequest API to make the association after the consumer key and secret are created. |
| `expiresInSeconds` | `string` | Immutable. Expiration time, in seconds, for the consumer key. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_appgroups_apps_keys_get` | `SELECT` | `appgroupsId, appsId, keysId, organizationsId` | Gets details for a consumer key for a AppGroup app, including the key and secret value, associated API products, and other information. |
| `organizations_developers_apps_keys_get` | `SELECT` | `appsId, developersId, keysId, organizationsId` | Gets details for a consumer key for a developer app, including the key and secret value, associated API products, and other information. |
| `organizations_appgroups_apps_keys_create` | `INSERT` | `appgroupsId, appsId, organizationsId` | Creates a custom consumer key and secret for a AppGroup app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the ProductizeAppGroupAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteAppGroupAppKey API. |
| `organizations_developers_apps_keys_create` | `INSERT` | `appsId, developersId, organizationsId` | Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteDeveloperAppKey API. **Note**: All keys start out with status=approved, even if status=revoked is passed when the key is created. To revoke a key, use the UpdateDeveloperAppKey API. |
| `organizations_appgroups_apps_keys_delete` | `DELETE` | `appgroupsId, appsId, keysId, organizationsId` | Deletes an app's consumer key and removes all API products associated with the app. After the consumer key is deleted, it cannot be used to access any APIs. |
| `organizations_developers_apps_keys_delete` | `DELETE` | `appsId, developersId, keysId, organizationsId` | Deletes an app's consumer key and removes all API products associated with the app. After the consumer key is deleted, it cannot be used to access any APIs. **Note**: After you delete a consumer key, you may want to: 1. Create a new consumer key and secret for the developer app using the CreateDeveloperAppKey API, and subsequently add an API product to the key using the UpdateDeveloperAppKey API. 2. Delete the developer app, if it is no longer required. |
| `organizations_developers_apps_keys_replace_developer_app_key` | `EXEC` | `appsId, developersId, keysId, organizationsId` | Updates the scope of an app. This API replaces the existing scopes with those specified in the request. Include or exclude any existing scopes that you want to retain or delete, respectively. The specified scopes must already be defined for the API products associated with the app. This API sets the `scopes` element under the `apiProducts` element in the attributes of the app. |
