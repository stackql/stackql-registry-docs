---
title: sql_server_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_registrations
  - azure_data
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

Creates, updates, deletes, gets or lists a <code>sql_server_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_server_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_data.sql_server_registrations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_registrations', value: 'view', },
        { label: 'sql_server_registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="property_bag" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerRegistrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The SQL server Registration properties. |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Gets a SQL Server registration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL Server registrations in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL Server registrations in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId, data__location" /> | Creates or updates a SQL Server registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Deletes a SQL Server registration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Updates SQL Server Registration tags. |

## `SELECT` examples

Gets all SQL Server registrations in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_server_registrations', value: 'view', },
        { label: 'sql_server_registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
property_bag,
resourceGroupName,
resource_group,
sqlServerRegistrationName,
subscriptionId,
subscription_id,
system_data,
tags
FROM azure.azure_data.vw_sql_server_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.azure_data.sql_server_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_server_registrations</code> resource.

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
INSERT INTO azure.azure_data.sql_server_registrations (
resourceGroupName,
sqlServerRegistrationName,
subscriptionId,
data__location,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlServerRegistrationName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: subscriptionId
          value: string
        - name: resourceGroup
          value: string
        - name: propertyBag
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_server_registrations</code> resource.

```sql
/*+ update */
UPDATE azure.azure_data.sql_server_registrations
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerRegistrationName = '{{ sqlServerRegistrationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_server_registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_data.sql_server_registrations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerRegistrationName = '{{ sqlServerRegistrationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
