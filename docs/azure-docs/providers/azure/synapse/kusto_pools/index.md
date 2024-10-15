---
title: kusto_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools
  - synapse
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

Creates, updates, deletes, gets or lists a <code>kusto_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pools', value: 'view', },
        { label: 'kusto_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_ingestion_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_purge" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_streaming_ingest" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="kustoPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="language_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="optimized_autoscale" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Azure SKU definition. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_uid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Kusto pool properties. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a Kusto pool. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all Kusto pools |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__sku" /> | Create or update a Kusto pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a Kusto pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Update a Kusto Kusto Pool. |
| <CopyableCode code="add_language_extensions" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Add a list of language extensions that can run within KQL queries. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the kusto pool name is valid and is not already in use. |
| <CopyableCode code="detach_follower_databases" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__attachedDatabaseConfigurationName, data__clusterResourceId" /> | Detaches all followers of a database owned by this Kusto Pool. |
| <CopyableCode code="remove_language_extensions" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Remove a list of language extensions that can run within KQL queries. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Starts a Kusto pool. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Stops a Kusto pool. |

## `SELECT` examples

List all Kusto pools

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pools', value: 'view', },
        { label: 'kusto_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_ingestion_uri,
enable_purge,
enable_streaming_ingest,
etag,
kustoPoolName,
language_extensions,
location,
optimized_autoscale,
provisioning_state,
resourceGroupName,
sku,
state,
state_reason,
subscriptionId,
system_data,
tags,
uri,
workspaceName,
workspace_uid
FROM azure.synapse.vw_kusto_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
sku,
systemData,
tags
FROM azure.synapse.kusto_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kusto_pools</code> resource.

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
INSERT INTO azure.synapse.kusto_pools (
kustoPoolName,
resourceGroupName,
subscriptionId,
workspaceName,
data__sku,
sku,
properties,
tags,
location
)
SELECT 
'{{ kustoPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
        - name: size
          value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: provisioningState
          value: []
        - name: uri
          value: string
        - name: dataIngestionUri
          value: string
        - name: stateReason
          value: string
        - name: optimizedAutoscale
          value:
            - name: version
              value: integer
            - name: isEnabled
              value: boolean
            - name: minimum
              value: integer
            - name: maximum
              value: integer
        - name: enableStreamingIngest
          value: boolean
        - name: enablePurge
          value: boolean
        - name: languageExtensions
          value:
            - name: value
              value:
                - - name: languageExtensionName
                    value: []
        - name: workspaceUID
          value: string
    - name: etag
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kusto_pools</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.kusto_pools
SET 
tags = '{{ tags }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>kusto_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.kusto_pools
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
