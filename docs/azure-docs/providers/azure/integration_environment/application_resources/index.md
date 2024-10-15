---
title: application_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - application_resources
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

Creates, updates, deletes, gets or lists a <code>application_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.application_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_resources', value: 'view', },
        { label: 'application_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="spaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of application resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Get a ApplicationResource |
| <CopyableCode code="list_by_application" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List ApplicationResource resources by Application |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Create a ApplicationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Delete a ApplicationResource |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Update a ApplicationResource |

## `SELECT` examples

List ApplicationResource resources by Application

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_resources', value: 'view', },
        { label: 'application_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applicationName,
provisioning_state,
resourceGroupName,
resourceName,
resource_id,
resource_kind,
resource_type,
spaceName,
subscriptionId
FROM azure.integration_environment.vw_application_resources
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
FROM azure.integration_environment.application_resources
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_resources</code> resource.

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
INSERT INTO azure.integration_environment.application_resources (
applicationName,
resourceGroupName,
resourceName,
spaceName,
subscriptionId,
properties
)
SELECT 
'{{ applicationName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: resourceType
          value: string
        - name: resourceId
          value: string
        - name: resourceKind
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>application_resources</code> resource.

```sql
/*+ update */
UPDATE azure.integration_environment.application_resources
SET 
properties = '{{ properties }}'
WHERE 
applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>application_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.integration_environment.application_resources
WHERE applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
