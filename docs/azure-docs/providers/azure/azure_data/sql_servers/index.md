---
title: sql_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_servers
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

Creates, updates, deletes, gets or lists a <code>sql_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_data.sql_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_servers', value: 'view', },
        { label: 'sql_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="property_bag" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerRegistrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The SQL server properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId" /> | Gets a SQL Server. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Gets all SQL Servers in a SQL Server Registration. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId" /> | Creates or updates a SQL Server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlServerName, sqlServerRegistrationName, subscriptionId" /> | Deletes a SQL Server. |

## `SELECT` examples

Gets all SQL Servers in a SQL Server Registration.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_servers', value: 'view', },
        { label: 'sql_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cores,
edition,
property_bag,
registration_id,
resourceGroupName,
sqlServerName,
sqlServerRegistrationName,
subscriptionId,
version
FROM azure.azure_data.vw_sql_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerRegistrationName = '{{ sqlServerRegistrationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.azure_data.sql_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerRegistrationName = '{{ sqlServerRegistrationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_servers</code> resource.

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
INSERT INTO azure.azure_data.sql_servers (
resourceGroupName,
sqlServerName,
sqlServerRegistrationName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlServerName }}',
'{{ sqlServerRegistrationName }}',
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
        - name: cores
          value: integer
        - name: version
          value: string
        - name: edition
          value: string
        - name: registrationID
          value: string
        - name: propertyBag
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_data.sql_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlServerName = '{{ sqlServerName }}'
AND sqlServerRegistrationName = '{{ sqlServerRegistrationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
