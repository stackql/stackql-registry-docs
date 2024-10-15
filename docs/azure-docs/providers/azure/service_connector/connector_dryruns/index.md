---
title: connector_dryruns
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_dryruns
  - service_connector
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

Creates, updates, deletes, gets or lists a <code>connector_dryruns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_dryruns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.connector_dryruns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_dryruns', value: 'view', },
        { label: 'connector_dryruns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dryrunName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_previews" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="prerequisite_results" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the dryrun job |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | get a dryrun job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | list dryrun jobs |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | create a dryrun job to do necessary check before actual creation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | delete a dryrun job |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | update a dryrun job to do necessary check before actual creation |

## `SELECT` examples

list dryrun jobs

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_dryruns', value: 'view', },
        { label: 'connector_dryruns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dryrunName,
location,
operation_previews,
parameters,
prerequisite_results,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.service_connector.vw_connector_dryruns
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.service_connector.connector_dryruns
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector_dryruns</code> resource.

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
INSERT INTO azure.service_connector.connector_dryruns (
dryrunName,
location,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ dryrunName }}',
'{{ location }}',
'{{ resourceGroupName }}',
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
        - name: parameters
          value:
            - name: actionName
              value: []
        - name: prerequisiteResults
          value:
            - - name: type
                value: []
        - name: operationPreviews
          value:
            - - name: name
                value: string
              - name: operationType
                value: string
              - name: description
                value: string
              - name: action
                value: string
              - name: scope
                value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connector_dryruns</code> resource.

```sql
/*+ update */
UPDATE azure.service_connector.connector_dryruns
SET 
properties = '{{ properties }}'
WHERE 
dryrunName = '{{ dryrunName }}'
AND location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connector_dryruns</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_connector.connector_dryruns
WHERE dryrunName = '{{ dryrunName }}'
AND location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
