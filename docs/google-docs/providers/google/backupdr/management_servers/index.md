---
title: management_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - management_servers
  - backupdr
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

Creates, updates, deletes or gets an <code>management_server</code> resource or lists <code>management_servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.management_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name. |
| <CopyableCode code="description" /> | `string` | Optional. The description of the ManagementServer instance (2048 characters or less). |
| <CopyableCode code="baProxyUri" /> | `array` | Output only. The hostname or ip address of the exposed AGM endpoints, used by BAs to connect to BA proxy. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. Labels currently defined: 1. migrate_from_go= If set to true, the MS is created in migration ready mode. |
| <CopyableCode code="managementUri" /> | `object` | ManagementURI for the Management Server resource. |
| <CopyableCode code="networks" /> | `array` | Required. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. |
| <CopyableCode code="oauth2ClientId" /> | `string` | Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the 'aud' field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken). |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The ManagementServer state. |
| <CopyableCode code="type" /> | `string` | Optional. The type of the ManagementServer resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |
| <CopyableCode code="workforceIdentityBasedManagementUri" /> | `object` | ManagementURI depending on the Workforce Identity i.e. either 1p or 3p. |
| <CopyableCode code="workforceIdentityBasedOauth2ClientId" /> | `object` | OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p, |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, managementServersId, projectsId" /> | Gets details of a single ManagementServer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ManagementServers in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ManagementServer in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, managementServersId, projectsId" /> | Deletes a single ManagementServer. |

## `SELECT` examples

Lists ManagementServers in a given project and location.

```sql
SELECT
name,
description,
baProxyUri,
createTime,
etag,
labels,
managementUri,
networks,
oauth2ClientId,
satisfiesPzi,
satisfiesPzs,
state,
type,
updateTime,
workforceIdentityBasedManagementUri,
workforceIdentityBasedOauth2ClientId
FROM google.backupdr.management_servers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_servers</code> resource.

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
INSERT INTO google.backupdr.management_servers (
locationsId,
projectsId,
name,
description,
labels,
createTime,
updateTime,
type,
managementUri,
workforceIdentityBasedManagementUri,
state,
networks,
etag,
oauth2ClientId,
workforceIdentityBasedOauth2ClientId,
baProxyUri,
satisfiesPzs,
satisfiesPzi
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ type }}',
'{{ managementUri }}',
'{{ workforceIdentityBasedManagementUri }}',
'{{ state }}',
'{{ networks }}',
'{{ etag }}',
'{{ oauth2ClientId }}',
'{{ workforceIdentityBasedOauth2ClientId }}',
'{{ baProxyUri }}',
true|false,
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: type
        value: '{{ type }}'
      - name: managementUri
        value: '{{ managementUri }}'
      - name: workforceIdentityBasedManagementUri
        value: '{{ workforceIdentityBasedManagementUri }}'
      - name: state
        value: '{{ state }}'
      - name: networks
        value: '{{ networks }}'
      - name: etag
        value: '{{ etag }}'
      - name: oauth2ClientId
        value: '{{ oauth2ClientId }}'
      - name: workforceIdentityBasedOauth2ClientId
        value: '{{ workforceIdentityBasedOauth2ClientId }}'
      - name: baProxyUri
        value: '{{ baProxyUri }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified management_server resource.

```sql
DELETE FROM google.backupdr.management_servers
WHERE locationsId = '{{ locationsId }}'
AND managementServersId = '{{ managementServersId }}'
AND projectsId = '{{ projectsId }}';
```
