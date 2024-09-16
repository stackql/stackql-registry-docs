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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiProducts" /> | `array` | Output only. List of API products and its status for which the credential can be used. **Note**: Use UpdateAppGroupAppKeyApiProductRequest API to make the association after the consumer key and secret are created. |
| <CopyableCode code="attributes" /> | `array` | List of attributes associated with the credential. |
| <CopyableCode code="consumerKey" /> | `string` | Immutable. Consumer key. |
| <CopyableCode code="consumerSecret" /> | `string` | Secret key. |
| <CopyableCode code="expiresAt" /> | `string` | Output only. Time the AppGroup app expires in milliseconds since epoch. |
| <CopyableCode code="expiresInSeconds" /> | `string` | Immutable. Expiration time, in seconds, for the consumer key. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set. |
| <CopyableCode code="issuedAt" /> | `string` | Output only. Time the AppGroup app was created in milliseconds since epoch. |
| <CopyableCode code="scopes" /> | `array` | Scopes to apply to the app. The specified scope names must already be defined for the API product that you associate with the app. |
| <CopyableCode code="status" /> | `string` | Status of the credential. Valid values include `approved` or `revoked`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_appgroups_apps_keys_get" /> | `SELECT` | <CopyableCode code="appgroupsId, appsId, keysId, organizationsId" /> | Gets details for a consumer key for a AppGroup app, including the key and secret value, associated API products, and other information. |
| <CopyableCode code="organizations_developers_apps_keys_get" /> | `SELECT` | <CopyableCode code="appsId, developersId, keysId, organizationsId" /> | Gets details for a consumer key for a developer app, including the key and secret value, associated API products, and other information. |
| <CopyableCode code="organizations_appgroups_apps_keys_create" /> | `INSERT` | <CopyableCode code="appgroupsId, appsId, organizationsId" /> | Creates a custom consumer key and secret for a AppGroup app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the ProductizeAppGroupAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteAppGroupAppKey API. |
| <CopyableCode code="organizations_developers_apps_keys_create" /> | `INSERT` | <CopyableCode code="appsId, developersId, organizationsId" /> | Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system. Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each. **Note**: When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the UpdateDeveloperAppKey API to make the association after the consumer key and secret are created. If a consumer key and secret already exist, you can keep them or delete them using the DeleteDeveloperAppKey API. **Note**: All keys start out with status=approved, even if status=revoked is passed when the key is created. To revoke a key, use the UpdateDeveloperAppKey API. |
| <CopyableCode code="organizations_appgroups_apps_keys_delete" /> | `DELETE` | <CopyableCode code="appgroupsId, appsId, keysId, organizationsId" /> | Deletes an app's consumer key and removes all API products associated with the app. After the consumer key is deleted, it cannot be used to access any APIs. |
| <CopyableCode code="organizations_developers_apps_keys_delete" /> | `DELETE` | <CopyableCode code="appsId, developersId, keysId, organizationsId" /> | Deletes an app's consumer key and removes all API products associated with the app. After the consumer key is deleted, it cannot be used to access any APIs. **Note**: After you delete a consumer key, you may want to: 1. Create a new consumer key and secret for the developer app using the CreateDeveloperAppKey API, and subsequently add an API product to the key using the UpdateDeveloperAppKey API. 2. Delete the developer app, if it is no longer required. |
| <CopyableCode code="organizations_developers_apps_keys_replace_developer_app_key" /> | `REPLACE` | <CopyableCode code="appsId, developersId, keysId, organizationsId" /> | Updates the scope of an app. This API replaces the existing scopes with those specified in the request. Include or exclude any existing scopes that you want to retain or delete, respectively. The specified scopes must already be defined for the API products associated with the app. This API sets the `scopes` element under the `apiProducts` element in the attributes of the app. |

## `SELECT` examples

Gets details for a consumer key for a AppGroup app, including the key and secret value, associated API products, and other information.

```sql
SELECT
apiProducts,
attributes,
consumerKey,
consumerSecret,
expiresAt,
expiresInSeconds,
issuedAt,
scopes,
status
FROM google.apigee.keys
WHERE appgroupsId = '{{ appgroupsId }}'
AND appsId = '{{ appsId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keys</code> resource.

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
INSERT INTO google.apigee.keys (
appgroupsId,
appsId,
organizationsId,
attributes,
expiresInSeconds,
consumerKey,
consumerSecret,
status,
scopes
)
SELECT 
'{{ appgroupsId }}',
'{{ appsId }}',
'{{ organizationsId }}',
'{{ attributes }}',
'{{ expiresInSeconds }}',
'{{ consumerKey }}',
'{{ consumerSecret }}',
'{{ status }}',
'{{ scopes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: attributes
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: expiresInSeconds
      value: '{{ expiresInSeconds }}'
    - name: consumerKey
      value: '{{ consumerKey }}'
    - name: consumerSecret
      value: '{{ consumerSecret }}'
    - name: status
      value: '{{ status }}'
    - name: scopes
      value:
        - name: type
          value: '{{ type }}'

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>keys</code> resource.

```sql
/*+ update */
REPLACE google.apigee.keys
SET 
consumerKey = '{{ consumerKey }}',
expiresInSeconds = '{{ expiresInSeconds }}',
consumerSecret = '{{ consumerSecret }}',
attributes = '{{ attributes }}',
apiProducts = '{{ apiProducts }}',
status = '{{ status }}',
issuedAt = '{{ issuedAt }}',
scopes = '{{ scopes }}',
expiresAt = '{{ expiresAt }}'
WHERE 
appsId = '{{ appsId }}'
AND developersId = '{{ developersId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.keys
WHERE appgroupsId = '{{ appgroupsId }}'
AND appsId = '{{ appsId }}'
AND keysId = '{{ keysId }}'
AND organizationsId = '{{ organizationsId }}';
```
