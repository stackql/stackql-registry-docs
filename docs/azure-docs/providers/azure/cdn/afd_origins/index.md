---
title: afd_origins
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origins
  - cdn
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

Creates, updates, deletes, gets or lists a <code>afd_origins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>afd_origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origins" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_origins', value: 'view', },
        { label: 'afd_origins', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_origin" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="enforce_certificate_name_check" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="originGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="originName" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_host_header" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_private_link_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="weight" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the origin. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin within an origin group. |
| <CopyableCode code="list_by_origin_group" /> | `SELECT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within an origin group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin within the specified origin group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin within an origin group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin within an origin group. |

## `SELECT` examples

Lists all of the existing origins within an origin group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_origins', value: 'view', },
        { label: 'afd_origins', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_origin,
deployment_status,
enabled_state,
enforce_certificate_name_check,
host_name,
http_port,
https_port,
originGroupName,
originName,
origin_group_name,
origin_host_header,
priority,
profileName,
provisioning_state,
resourceGroupName,
shared_private_link_resource,
subscriptionId,
weight
FROM azure.cdn.vw_afd_origins
WHERE originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.afd_origins
WHERE originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>afd_origins</code> resource.

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
INSERT INTO azure.cdn.afd_origins (
originGroupName,
originName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ originGroupName }}',
'{{ originName }}',
'{{ profileName }}',
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
        - name: originGroupName
          value: string
        - name: azureOrigin
          value:
            - name: id
              value: string
        - name: hostName
          value: string
        - name: httpPort
          value: integer
        - name: httpsPort
          value: integer
        - name: originHostHeader
          value: string
        - name: priority
          value: integer
        - name: weight
          value: integer
        - name: sharedPrivateLinkResource
          value:
            - name: privateLinkLocation
              value: string
            - name: groupId
              value: string
            - name: requestMessage
              value: string
            - name: status
              value: string
        - name: enabledState
          value: string
        - name: enforceCertificateNameCheck
          value: boolean
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>afd_origins</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.afd_origins
SET 
properties = '{{ properties }}'
WHERE 
originGroupName = '{{ originGroupName }}'
AND originName = '{{ originName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>afd_origins</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.afd_origins
WHERE originGroupName = '{{ originGroupName }}'
AND originName = '{{ originName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
