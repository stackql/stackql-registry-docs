---
title: dpp_resource_guard_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - dpp_resource_guard_proxies
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>dpp_resource_guard_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dpp_resource_guard_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.dpp_resource_guard_proxies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dpp_resource_guard_proxies', value: 'view', },
        { label: 'dpp_resource_guard_proxies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Resource name associated with the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGuardProxyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | ResourceGuardProxyBase object, used in ResourceGuardProxyBaseResource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> |  |
| <CopyableCode code="unlock_delete" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dpp_resource_guard_proxies', value: 'view', },
        { label: 'dpp_resource_guard_proxies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
last_updated_time,
resourceGroupName,
resourceGuardProxyName,
resource_guard_operation_details,
resource_guard_resource_id,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_protection.vw_dpp_resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_protection.dpp_resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dpp_resource_guard_proxies</code> resource.

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
INSERT INTO azure.data_protection.dpp_resource_guard_proxies (
resourceGroupName,
resourceGuardProxyName,
subscriptionId,
vaultName,
systemData,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceGuardProxyName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ systemData }}',
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
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: resourceGuardResourceId
          value: string
        - name: resourceGuardOperationDetails
          value:
            - - name: vaultCriticalOperation
                value: string
              - name: defaultResourceRequest
                value: string
        - name: lastUpdatedTime
          value: string
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dpp_resource_guard_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_protection.dpp_resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardProxyName = '{{ resourceGuardProxyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
