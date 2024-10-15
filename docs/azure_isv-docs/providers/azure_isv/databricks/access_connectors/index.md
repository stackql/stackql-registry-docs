---
title: access_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - access_connectors
  - databricks
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

Creates, updates, deletes, gets or lists a <code>access_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.access_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_connectors', value: 'view', },
        { label: 'access_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="refered_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Gets an Azure Databricks Access Connector. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Azure Databricks Access Connectors within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Azure Databricks Access Connectors within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Creates or updates Azure Databricks Access Connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Deletes the Azure Databricks Access Connector. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Updates an Azure Databricks Access Connector. |

## `SELECT` examples

Gets all the Azure Databricks Access Connectors within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_connectors', value: 'view', },
        { label: 'access_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectorName,
identity,
location,
provisioning_state,
refered_by,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure_isv.databricks.vw_access_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure_isv.databricks.access_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_connectors</code> resource.

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
INSERT INTO azure_isv.databricks.access_connectors (
connectorName,
resourceGroupName,
subscriptionId,
identity,
systemData,
properties,
tags,
location
)
SELECT 
'{{ connectorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ systemData }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
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
        - name: provisioningState
          value: string
        - name: referedBy
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_connectors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.databricks.access_connectors
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
connectorName = '{{ connectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>access_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.databricks.access_connectors
WHERE connectorName = '{{ connectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
