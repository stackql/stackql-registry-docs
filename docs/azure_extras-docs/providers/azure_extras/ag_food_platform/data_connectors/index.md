---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>data_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.data_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_connectors', value: 'view', },
        { label: 'data_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerForAgricultureResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | The ETag value to implement optimistic concurrency. |
| <CopyableCode code="properties" /> | `object` | DataConnector Properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get specific Data Connector resource by DataConnectorName. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Lists the Data Connector Credentials for MADMA instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId, data__properties" /> | Create or update Data Connector For MADMA resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Delete a Data Connectors with given dataConnector name. |

## `SELECT` examples

Lists the Data Connector Credentials for MADMA instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_connectors', value: 'view', },
        { label: 'data_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
credentials,
dataConnectorName,
dataManagerForAgricultureResourceName,
e_tag,
resourceGroupName,
subscriptionId,
system_data
FROM azure_extras.ag_food_platform.vw_data_connectors
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties,
systemData
FROM azure_extras.ag_food_platform.data_connectors
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_connectors</code> resource.

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
INSERT INTO azure_extras.ag_food_platform.data_connectors (
dataConnectorName,
dataManagerForAgricultureResourceName,
resourceGroupName,
subscriptionId,
data__properties,
systemData,
properties
)
SELECT 
'{{ dataConnectorName }}',
'{{ dataManagerForAgricultureResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
        - name: credentials
          value:
            - name: kind
              value: []
    - name: eTag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.ag_food_platform.data_connectors
WHERE dataConnectorName = '{{ dataConnectorName }}'
AND dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
