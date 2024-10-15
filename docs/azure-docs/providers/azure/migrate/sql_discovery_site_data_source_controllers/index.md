---
title: sql_discovery_site_data_source_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_discovery_site_data_source_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>sql_discovery_site_data_source_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_discovery_site_data_source_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_discovery_site_data_source_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_discovery_site_data_source_controllers', value: 'view', },
        { label: 'sql_discovery_site_data_source_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="discoverySiteDataSourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_site_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Discovery site data source properties class. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Get a SqlDiscoverySiteDataSource |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | List SqlDiscoverySiteDataSource resources by SqlSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Create a SqlDiscoverySiteDataSource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Delete a SqlDiscoverySiteDataSource |

## `SELECT` examples

List SqlDiscoverySiteDataSource resources by SqlSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_discovery_site_data_source_controllers', value: 'view', },
        { label: 'sql_discovery_site_data_source_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
discoverySiteDataSourceName,
discovery_site_id,
provisioning_state,
resourceGroupName,
siteName,
sqlSiteName,
subscriptionId
FROM azure.migrate.vw_sql_discovery_site_data_source_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.sql_discovery_site_data_source_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_discovery_site_data_source_controllers</code> resource.

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
INSERT INTO azure.migrate.sql_discovery_site_data_source_controllers (
discoverySiteDataSourceName,
resourceGroupName,
siteName,
sqlSiteName,
subscriptionId,
properties
)
SELECT 
'{{ discoverySiteDataSourceName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
'{{ sqlSiteName }}',
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
        - name: discoverySiteId
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_discovery_site_data_source_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.sql_discovery_site_data_source_controllers
WHERE discoverySiteDataSourceName = '{{ discoverySiteDataSourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
