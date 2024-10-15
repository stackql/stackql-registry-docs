---
title: virtual_machine_image_templates_run_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates_run_outputs
  - image_builder
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_image_templates_run_outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates_run_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.virtual_machine_image_templates_run_outputs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_image_templates_run_outputs', value: 'view', },
        { label: 'virtual_machine_image_templates_run_outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifact_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageTemplateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runOutputName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a run output |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, runOutputName, subscriptionId" /> | Get the specified run output for the specified image template resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | List all run outputs for the specified Image Template resource |

## `SELECT` examples

List all run outputs for the specified Image Template resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_image_templates_run_outputs', value: 'view', },
        { label: 'virtual_machine_image_templates_run_outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifact_id,
artifact_uri,
imageTemplateName,
provisioning_state,
resourceGroupName,
runOutputName,
subscriptionId
FROM azure.image_builder.vw_virtual_machine_image_templates_run_outputs
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.image_builder.virtual_machine_image_templates_run_outputs
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

