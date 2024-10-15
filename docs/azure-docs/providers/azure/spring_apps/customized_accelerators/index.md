---
title: customized_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - customized_accelerators
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

Creates, updates, deletes, gets or lists a <code>customized_accelerators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customized_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.customized_accelerators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customized_accelerators', value: 'view', },
        { label: 'customized_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accelerator_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="accelerator_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationAcceleratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="customizedAcceleratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="git_repository" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="imports" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Customized accelerator properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Get the customized accelerator. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all customized accelerators. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Create or update the customized accelerator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Delete the customized accelerator. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, customizedAcceleratorName, resourceGroupName, serviceName, subscriptionId, data__gitRepository" /> | Check the customized accelerator are valid. |

## `SELECT` examples

Handle requests to list all customized accelerators.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_customized_accelerators', value: 'view', },
        { label: 'customized_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accelerator_tags,
accelerator_type,
applicationAcceleratorName,
customizedAcceleratorName,
display_name,
git_repository,
icon_url,
imports,
provisioning_state,
resourceGroupName,
serviceName,
sku,
subscriptionId
FROM azure.spring_apps.vw_customized_accelerators
WHERE applicationAcceleratorName = '{{ applicationAcceleratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.spring_apps.customized_accelerators
WHERE applicationAcceleratorName = '{{ applicationAcceleratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customized_accelerators</code> resource.

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
INSERT INTO azure.spring_apps.customized_accelerators (
applicationAcceleratorName,
customizedAcceleratorName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
sku
)
SELECT 
'{{ applicationAcceleratorName }}',
'{{ customizedAcceleratorName }}',
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
        - name: acceleratorType
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: iconUrl
          value: string
        - name: acceleratorTags
          value:
            - string
        - name: imports
          value:
            - string
        - name: gitRepository
          value:
            - name: url
              value: string
            - name: intervalInSeconds
              value: integer
            - name: branch
              value: string
            - name: commit
              value: string
            - name: gitTag
              value: string
            - name: authSetting
              value:
                - name: authType
                  value: string
            - name: subPath
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

Deletes the specified <code>customized_accelerators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.customized_accelerators
WHERE applicationAcceleratorName = '{{ applicationAcceleratorName }}'
AND customizedAcceleratorName = '{{ customizedAcceleratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
