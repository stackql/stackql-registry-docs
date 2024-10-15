---
title: site_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - site_containers
  - app_service
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

Creates, updates, deletes, gets or lists a <code>site_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>site_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.site_containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | SiteContainer resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerName, name, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.site_containers
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>site_containers</code> resource.

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
INSERT INTO azure.app_service.site_containers (
containerName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ containerName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: image
          value: string
        - name: targetPort
          value: string
        - name: isMain
          value: boolean
        - name: startUpCommand
          value: string
        - name: authType
          value: string
        - name: userName
          value: string
        - name: passwordSecret
          value: string
        - name: userManagedIdentityClientId
          value: string
        - name: createdTime
          value: string
        - name: lastModifiedTime
          value: string
        - name: volumeMounts
          value:
            - - name: volumeSubPath
                value: string
              - name: containerMountPath
                value: string
              - name: data
                value: string
              - name: readOnly
                value: boolean
        - name: environmentVariables
          value:
            - - name: name
                value: string
              - name: value
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>site_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.site_containers
WHERE containerName = '{{ containerName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
