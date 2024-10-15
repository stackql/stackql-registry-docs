---
title: postgres_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_instances
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>postgres_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgres_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.postgres_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_postgres_instances', value: 'view', },
        { label: 'postgres_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="admin" /> | `text` | field from the `properties` object |
| <CopyableCode code="basic_login_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_controller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="k8s_raw" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_uploaded_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="postgresInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU for Azure Database for PostgresSQL - Azure Arc |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Postgres Instance properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU for Azure Database for PostgresSQL - Azure Arc |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="postgresInstanceName, resourceGroupName, subscriptionId" /> | Retrieves a postgres Instance resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a postgres Instances list by Resource group name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="postgresInstanceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces a postgres Instance resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="postgresInstanceName, resourceGroupName, subscriptionId" /> | Deletes a postgres Instance resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="postgresInstanceName, resourceGroupName, subscriptionId" /> | Updates a postgres Instance resource |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_postgres_instances', value: 'view', },
        { label: 'postgres_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
admin,
basic_login_information,
data_controller_id,
extended_location,
k8s_raw,
last_uploaded_date,
location,
postgresInstanceName,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure.azure_arc_data.vw_postgres_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
sku,
tags
FROM azure.azure_arc_data.postgres_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>postgres_instances</code> resource.

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
INSERT INTO azure.azure_arc_data.postgres_instances (
postgresInstanceName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
extendedLocation,
properties,
sku
)
SELECT 
'{{ postgresInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ sku }}'
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
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: properties
      value:
        - name: dataControllerId
          value: string
        - name: admin
          value: string
        - name: basicLoginInformation
          value:
            - name: username
              value: string
            - name: password
              value: string
        - name: k8sRaw
          value: object
        - name: lastUploadedDate
          value: string
        - name: provisioningState
          value: string
    - name: sku
      value:
        - name: tier
          value: string
        - name: name
          value: string
        - name: dev
          value: boolean
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>postgres_instances</code> resource.

```sql
/*+ update */
UPDATE azure.azure_arc_data.postgres_instances
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
postgresInstanceName = '{{ postgresInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>postgres_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.postgres_instances
WHERE postgresInstanceName = '{{ postgresInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
