---
title: attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_database_configurations
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>attached_database_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.attached_database_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_database_configurations', value: 'view', },
        { label: 'attached_database_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachedDatabaseConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="attached_database_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_principals_modification_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_level_sharing_properties" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Class representing the an attached database configuration properties of kind specific. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Returns an attached database configuration. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of attached database configurations of the given Kusto cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Creates or updates an attached database configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Deletes the attached database configuration with the given name. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the attached database configuration resource name is valid and is not already in use. |

## `SELECT` examples

Returns the list of attached database configurations of the given Kusto cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_database_configurations', value: 'view', },
        { label: 'attached_database_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
attachedDatabaseConfigurationName,
attached_database_names,
clusterName,
cluster_resource_id,
database_name,
database_name_override,
database_name_prefix,
default_principals_modification_kind,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
table_level_sharing_properties
FROM azure.data_explorer.vw_attached_database_configurations
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure.data_explorer.attached_database_configurations
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attached_database_configurations</code> resource.

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
INSERT INTO azure.data_explorer.attached_database_configurations (
attachedDatabaseConfigurationName,
clusterName,
resourceGroupName,
subscriptionId,
location,
properties
)
SELECT 
'{{ attachedDatabaseConfigurationName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
            - name: functionsToInclude
              value:
                - string
            - name: functionsToExclude
              value:
                - string
        - name: databaseNameOverride
          value: string
        - name: databaseNamePrefix
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>attached_database_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.attached_database_configurations
WHERE attachedDatabaseConfigurationName = '{{ attachedDatabaseConfigurationName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
