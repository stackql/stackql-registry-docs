---
title: apms
hide_title: false
hide_table_of_contents: false
keywords:
  - apms
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>apms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.apms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apms', value: 'view', },
        { label: 'apms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apmName" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Properties of an APM |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secrets" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an APM |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Get the APM by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get collection of APMs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Create or update an APM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apmName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete an APM |

## `SELECT` examples

Get collection of APMs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apms', value: 'view', },
        { label: 'apms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apmName,
properties,
provisioning_state,
resourceGroupName,
secrets,
serviceName,
subscriptionId,
type
FROM azure.spring_apps.vw_apms
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.apms
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apms</code> resource.

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
INSERT INTO azure.spring_apps.apms (
apmName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apmName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: type
          value: string
        - name: provisioningState
          value: string
        - name: properties
          value: object
        - name: secrets
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>apms</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.apms
WHERE apmName = '{{ apmName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
