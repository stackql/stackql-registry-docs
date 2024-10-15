---
title: predefined_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - predefined_accelerators
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

Creates, updates, deletes, gets or lists a <code>predefined_accelerators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predefined_accelerators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.predefined_accelerators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_predefined_accelerators', value: 'view', },
        { label: 'predefined_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accelerator_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationAcceleratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="predefinedAcceleratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Predefined accelerator properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Get the predefined accelerator. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all predefined accelerators. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Disable predefined accelerator. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="applicationAcceleratorName, predefinedAcceleratorName, resourceGroupName, serviceName, subscriptionId" /> | Enable predefined accelerator. |

## `SELECT` examples

Handle requests to list all predefined accelerators.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_predefined_accelerators', value: 'view', },
        { label: 'predefined_accelerators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accelerator_tags,
applicationAcceleratorName,
display_name,
icon_url,
predefinedAcceleratorName,
provisioning_state,
resourceGroupName,
serviceName,
sku,
state,
subscriptionId
FROM azure.spring_apps.vw_predefined_accelerators
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
FROM azure.spring_apps.predefined_accelerators
WHERE applicationAcceleratorName = '{{ applicationAcceleratorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

