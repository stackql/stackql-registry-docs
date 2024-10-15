---
title: application_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - application_accelerators
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

Creates, updates, deletes, gets or lists a <code>application_accelerators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.application_accelerators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_accelerators', value: 'view', },
        { label: 'application_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationAcceleratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="components" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application accelerator properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Get the application accelerator. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all application accelerator. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Create or update the application accelerator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Delete the application accelerator. |

## `SELECT` examples

Handle requests to list all application accelerator.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_accelerators', value: 'view', },
        { label: 'application_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applicationAcceleratorName,
components,
provisioning_state,
resourceGroupName,
serviceName,
sku,
subscriptionId
FROM azure.spring_apps.vw_application_accelerators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.spring_apps.application_accelerators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_accelerators</code> resource.

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
INSERT INTO azure.spring_apps.application_accelerators (
applicationAcceleratorName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
sku
)
SELECT 
'{{ applicationAcceleratorName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}'
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
          value: string
        - name: components
          value:
            - - name: name
                value: string
              - name: resourceRequests
                value:
                  - name: cpu
                    value: string
                  - name: memory
                    value: string
                  - name: instanceCount
                    value: integer
              - name: instances
                value:
                  - - name: name
                      value: string
                    - name: status
                      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>application_accelerators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.application_accelerators
WHERE applicationAcceleratorName = '{{ applicationAcceleratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
