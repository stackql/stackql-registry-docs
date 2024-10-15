---
title: business_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - business_processes
  - integration_environment
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

Creates, updates, deletes, gets or lists a <code>business_processes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.business_processes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_business_processes', value: 'view', },
        { label: 'business_processes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="businessProcessName" /> | `text` | field from the `properties` object |
| <CopyableCode code="business_process_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="business_process_stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracking_data_store_reference_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of business process. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Get a BusinessProcess |
| <CopyableCode code="list_by_application" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcess resources by Application |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Create a BusinessProcess |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Delete a BusinessProcess |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Update a BusinessProcess |

## `SELECT` examples

List BusinessProcess resources by Application

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_business_processes', value: 'view', },
        { label: 'business_processes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
applicationName,
businessProcessName,
business_process_mapping,
business_process_stages,
identifier,
provisioning_state,
resourceGroupName,
spaceName,
subscriptionId,
table_name,
tracking_data_store_reference_name,
version
FROM azure.integration_environment.vw_business_processes
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.integration_environment.business_processes
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>business_processes</code> resource.

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
INSERT INTO azure.integration_environment.business_processes (
applicationName,
businessProcessName,
resourceGroupName,
spaceName,
subscriptionId,
properties
)
SELECT 
'{{ applicationName }}',
'{{ businessProcessName }}',
'{{ resourceGroupName }}',
'{{ spaceName }}',
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
        - name: provisioningState
          value: []
        - name: version
          value: string
        - name: description
          value: string
        - name: tableName
          value: string
        - name: trackingDataStoreReferenceName
          value: string
        - name: identifier
          value:
            - name: propertyName
              value: string
            - name: propertyType
              value: string
        - name: businessProcessStages
          value: object
        - name: businessProcessMapping
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>business_processes</code> resource.

```sql
/*+ update */
UPDATE azure.integration_environment.business_processes
SET 
properties = '{{ properties }}'
WHERE 
applicationName = '{{ applicationName }}'
AND businessProcessName = '{{ businessProcessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>business_processes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.integration_environment.business_processes
WHERE applicationName = '{{ applicationName }}'
AND businessProcessName = '{{ businessProcessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
