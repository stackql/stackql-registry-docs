---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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

Creates, updates, deletes, gets or lists a <code>triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.triggers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_triggers', value: 'view', },
        { label: 'triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="imageTemplateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="triggerName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a trigger |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Get the specified trigger for the specified image template resource |
| <CopyableCode code="list_by_image_template" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | List all triggers for the specified Image Template resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Create or update a trigger for the specified virtual machine image template |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Delete a trigger for the specified virtual machine image template |

## `SELECT` examples

List all triggers for the specified Image Template resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_triggers', value: 'view', },
        { label: 'triggers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
imageTemplateName,
kind,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
triggerName
FROM azure.image_builder.vw_triggers
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.image_builder.triggers
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>triggers</code> resource.

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
INSERT INTO azure.image_builder.triggers (
imageTemplateName,
resourceGroupName,
subscriptionId,
triggerName,
properties
)
SELECT 
'{{ imageTemplateName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ triggerName }}',
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
        - name: kind
          value: string
        - name: status
          value:
            - name: code
              value: string
            - name: message
              value: string
            - name: time
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>triggers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.image_builder.triggers
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}';
```
