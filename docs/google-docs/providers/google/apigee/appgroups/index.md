---
title: appgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - appgroups
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

Creates, updates, deletes, gets or lists a <code>appgroups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.appgroups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\-$ %. |
| <CopyableCode code="appGroupId" /> | `string` | Output only. Internal identifier that cannot be edited |
| <CopyableCode code="attributes" /> | `array` | A list of attributes |
| <CopyableCode code="channelId" /> | `string` | channel identifier identifies the owner maintaing this grouping. |
| <CopyableCode code="channelUri" /> | `string` | A reference to the associated storefront/marketplace. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Created time as milliseconds since epoch. |
| <CopyableCode code="displayName" /> | `string` | app group name displayed in the UI |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Modified time as milliseconds since epoch. |
| <CopyableCode code="organization" /> | `string` | Immutable. the org the app group is created |
| <CopyableCode code="status" /> | `string` | Valid values are `active` or `inactive`. Note that the status of the AppGroup should be updated via UpdateAppGroupRequest by setting the action as `active` or `inactive`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_appgroups_get" /> | `SELECT` | <CopyableCode code="appgroupsId, organizationsId" /> | Returns the AppGroup details for the provided AppGroup name in the request URI. |
| <CopyableCode code="organizations_appgroups_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000. |
| <CopyableCode code="organizations_appgroups_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an AppGroup. Once created, user can register apps under the AppGroup to obtain secret key and password. At creation time, the AppGroup's state is set as `active`. |
| <CopyableCode code="organizations_appgroups_delete" /> | `DELETE` | <CopyableCode code="appgroupsId, organizationsId" /> | Deletes an AppGroup. All app and API keys associations with the AppGroup are also removed. **Warning**: This API will permanently delete the AppGroup and related artifacts. **Note**: The delete operation is asynchronous. The AppGroup app is deleted immediately, but its associated resources, such as apps and API keys, may take anywhere from a few seconds to a few minutes to be deleted. |
| <CopyableCode code="organizations_appgroups_update" /> | `REPLACE` | <CopyableCode code="appgroupsId, organizationsId" /> | Updates an AppGroup. This API replaces the existing AppGroup details with those specified in the request. Include or exclude any existing details that you want to retain or delete, respectively. Note that the state of the AppGroup should be updated using `action`, and not via AppGroup. |

## `SELECT` examples

Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000.

```sql
SELECT
name,
appGroupId,
attributes,
channelId,
channelUri,
createdAt,
displayName,
lastModifiedAt,
organization,
status
FROM google.apigee.appgroups
WHERE organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>appgroups</code> resource.

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
INSERT INTO google.apigee.appgroups (
organizationsId,
name,
displayName,
status,
channelUri,
channelId,
organization,
attributes
)
SELECT 
'{{ organizationsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ status }}',
'{{ channelUri }}',
'{{ channelId }}',
'{{ organization }}',
'{{ attributes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: status
      value: string
    - name: appGroupId
      value: string
    - name: createdAt
      value: string
    - name: lastModifiedAt
      value: string
    - name: channelUri
      value: string
    - name: channelId
      value: string
    - name: organization
      value: string
    - name: attributes
      value:
        - - name: name
            value: string
          - name: value
            value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>appgroups</code> resource.

```sql
/*+ update */
REPLACE google.apigee.appgroups
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
status = '{{ status }}',
channelUri = '{{ channelUri }}',
channelId = '{{ channelId }}',
organization = '{{ organization }}',
attributes = '{{ attributes }}'
WHERE 
appgroupsId = '{{ appgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>appgroups</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.appgroups
WHERE appgroupsId = '{{ appgroupsId }}'
AND organizationsId = '{{ organizationsId }}';
```
