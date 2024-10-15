---
title: kusto_pool_attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_attached_database_configurations
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

Creates, updates, deletes, gets or lists a <code>kusto_pool_attached_database_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pool_attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_attached_database_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pool_attached_database_configurations', value: 'view', },
        { label: 'kusto_pool_attached_database_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachedDatabaseConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="attached_database_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_principals_modification_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="kustoPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_level_sharing_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Class representing the an attached database configuration properties of kind specific. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns an attached database configuration. |
| <CopyableCode code="list_by_kusto_pool" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of attached database configurations of the given Kusto Pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an attached database configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the attached database configuration with the given name. |

## `SELECT` examples

Returns the list of attached database configurations of the given Kusto Pool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pool_attached_database_configurations', value: 'view', },
        { label: 'kusto_pool_attached_database_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
attachedDatabaseConfigurationName,
attached_database_names,
cluster_resource_id,
database_name,
default_principals_modification_kind,
kustoPoolName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
table_level_sharing_properties,
workspaceName
FROM azure.synapse.vw_kusto_pool_attached_database_configurations
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData
FROM azure.synapse.kusto_pool_attached_database_configurations
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kusto_pool_attached_database_configurations</code> resource.

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
INSERT INTO azure.synapse.kusto_pool_attached_database_configurations (
attachedDatabaseConfigurationName,
kustoPoolName,
resourceGroupName,
subscriptionId,
workspaceName,
location,
properties
)
SELECT 
'{{ attachedDatabaseConfigurationName }}',
'{{ kustoPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: databaseName
          value: string
        - name: clusterResourceId
          value: string
        - name: attachedDatabaseNames
          value:
            - string
        - name: defaultPrincipalsModificationKind
          value: string
        - name: tableLevelSharingProperties
          value:
            - name: tablesToInclude
              value:
                - string
            - name: tablesToExclude
              value:
                - string
            - name: externalTablesToInclude
              value:
                - string
            - name: externalTablesToExclude
              value:
                - string
            - name: materializedViewsToInclude
              value:
                - string
            - name: materializedViewsToExclude
              value:
                - string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>kusto_pool_attached_database_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.kusto_pool_attached_database_configurations
WHERE attachedDatabaseConfigurationName = '{{ attachedDatabaseConfigurationName }}'
AND kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
