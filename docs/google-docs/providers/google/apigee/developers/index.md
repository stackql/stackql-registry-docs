---
title: developers
hide_title: false
hide_table_of_contents: false
keywords:
  - developers
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

Creates, updates, deletes, gets or lists a <code>developers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>developers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.developers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessType" /> | `string` | Access type. |
| <CopyableCode code="appFamily" /> | `string` | Developer app family. |
| <CopyableCode code="apps" /> | `array` | List of apps associated with the developer. |
| <CopyableCode code="attributes" /> | `array` | Optional. Developer attributes (name/value pairs). The custom attribute limit is 18. |
| <CopyableCode code="companies" /> | `array` | List of companies associated with the developer. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time at which the developer was created in milliseconds since epoch. |
| <CopyableCode code="developerId" /> | `string` | ID of the developer. **Note**: IDs are generated internally by Apigee and are not guaranteed to stay the same over time. |
| <CopyableCode code="email" /> | `string` | Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only. |
| <CopyableCode code="firstName" /> | `string` | Required. First name of the developer. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time at which the developer was last modified in milliseconds since epoch. |
| <CopyableCode code="lastName" /> | `string` | Required. Last name of the developer. |
| <CopyableCode code="organizationName" /> | `string` | Output only. Name of the Apigee organization in which the developer resides. |
| <CopyableCode code="status" /> | `string` | Output only. Status of the developer. Valid values are `active` and `inactive`. |
| <CopyableCode code="userName" /> | `string` | Required. User name of the developer. Not used by Apigee hybrid. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_get" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Returns the developer details, including the developer's name, email address, apps, and other information. **Note**: The response includes only the first 100 developer apps. |
| <CopyableCode code="organizations_developers_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all developers in an organization by email address. By default, the response does not include company developers. Set the `includeCompany` query parameter to `true` to include company developers. **Note**: A maximum of 1000 developers are returned in the response. You paginate the list of developers returned using the `startKey` and `count` query parameters. |
| <CopyableCode code="organizations_developers_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a developer. Once created, the developer can register an app and obtain an API key. At creation time, a developer is set as `active`. To change the developer status, use the SetDeveloperStatus API. |
| <CopyableCode code="organizations_developers_delete" /> | `DELETE` | <CopyableCode code="developersId, organizationsId" /> | Deletes a developer. All apps and API keys associated with the developer are also removed. **Warning**: This API will permanently delete the developer and related artifacts. To avoid permanently deleting developers and their artifacts, set the developer status to `inactive` using the SetDeveloperStatus API. **Note**: The delete operation is asynchronous. The developer app is deleted immediately, but its associated resources, such as apps and API keys, may take anywhere from a few seconds to a few minutes to be deleted. |
| <CopyableCode code="organizations_developers_update" /> | `REPLACE` | <CopyableCode code="developersId, organizationsId" /> | Updates a developer. This API replaces the existing developer details with those specified in the request. Include or exclude any existing details that you want to retain or delete, respectively. The custom attribute limit is 18. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| <CopyableCode code="organizations_developers_attributes" /> | `EXEC` | <CopyableCode code="developersId, organizationsId" /> | Updates developer attributes. This API replaces the existing attributes with those specified in the request. Add new attributes, and include or exclude any existing attributes that you want to retain or remove, respectively. The custom attribute limit is 18. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| <CopyableCode code="organizations_developers_set_developer_status" /> | `EXEC` | <CopyableCode code="developersId, organizationsId" /> | Sets the status of a developer. A developer is `active` by default. If you set a developer's status to `inactive`, the API keys assigned to the developer apps are no longer valid even though the API keys are set to `approved`. Inactive developers can still sign in to the developer portal and create apps; however, any new API keys generated during app creation won't work. To set the status of a developer, set the `action` query parameter to `active` or `inactive`, and the `Content-Type` header to `application/octet-stream`. If successful, the API call returns the following HTTP status code: `204 No Content` |

## `SELECT` examples

Lists all developers in an organization by email address. By default, the response does not include company developers. Set the `includeCompany` query parameter to `true` to include company developers. **Note**: A maximum of 1000 developers are returned in the response. You paginate the list of developers returned using the `startKey` and `count` query parameters.

```sql
SELECT
accessType,
appFamily,
apps,
attributes,
companies,
createdAt,
developerId,
email,
firstName,
lastModifiedAt,
lastName,
organizationName,
status,
userName
FROM google.apigee.developers
WHERE organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>developers</code> resource.

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
INSERT INTO google.apigee.developers (
organizationsId,
companies,
developerId,
apps,
email,
appFamily,
firstName,
userName,
attributes,
accessType,
lastName
)
SELECT 
'{{ organizationsId }}',
'{{ companies }}',
'{{ developerId }}',
'{{ apps }}',
'{{ email }}',
'{{ appFamily }}',
'{{ firstName }}',
'{{ userName }}',
'{{ attributes }}',
'{{ accessType }}',
'{{ lastName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: companies
      value:
        - string
    - name: status
      value: string
    - name: developerId
      value: string
    - name: apps
      value:
        - string
    - name: createdAt
      value: string
    - name: email
      value: string
    - name: appFamily
      value: string
    - name: firstName
      value: string
    - name: userName
      value: string
    - name: organizationName
      value: string
    - name: attributes
      value:
        - - name: name
            value: string
          - name: value
            value: string
    - name: lastModifiedAt
      value: string
    - name: accessType
      value: string
    - name: lastName
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>developers</code> resource.

```sql
/*+ update */
REPLACE google.apigee.developers
SET 
companies = '{{ companies }}',
developerId = '{{ developerId }}',
apps = '{{ apps }}',
email = '{{ email }}',
appFamily = '{{ appFamily }}',
firstName = '{{ firstName }}',
userName = '{{ userName }}',
attributes = '{{ attributes }}',
accessType = '{{ accessType }}',
lastName = '{{ lastName }}'
WHERE 
developersId = '{{ developersId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>developers</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.developers
WHERE developersId = '{{ developersId }}'
AND organizationsId = '{{ organizationsId }}';
```
