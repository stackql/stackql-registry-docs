---
title: infrastructure_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_resources
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

Creates, updates, deletes, gets or lists a <code>infrastructure_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.infrastructure_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_infrastructure_resources', value: 'view', },
        { label: 'infrastructure_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="infrastructureResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="spaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of infrastructure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Get a InfrastructureResource |
| <CopyableCode code="list_by_space" /> | `SELECT` | <CopyableCode code="resourceGroupName, spaceName, subscriptionId" /> | List InfrastructureResource resources by Space |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Create a InfrastructureResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Delete a InfrastructureResource |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Update a InfrastructureResource |

## `SELECT` examples

List InfrastructureResource resources by Space

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_infrastructure_resources', value: 'view', },
        { label: 'infrastructure_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
infrastructureResourceName,
provisioning_state,
resourceGroupName,
resource_id,
resource_type,
spaceName,
subscriptionId
FROM azure.integration_environment.vw_infrastructure_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.integration_environment.infrastructure_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>infrastructure_resources</code> resource.

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
INSERT INTO azure.integration_environment.infrastructure_resources (
infrastructureResourceName,
resourceGroupName,
spaceName,
subscriptionId,
properties
)
SELECT 
'{{ infrastructureResourceName }}',
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
        - name: resourceType
          value: string
        - name: resourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>infrastructure_resources</code> resource.

```sql
/*+ update */
UPDATE azure.integration_environment.infrastructure_resources
SET 
properties = '{{ properties }}'
WHERE 
infrastructureResourceName = '{{ infrastructureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>infrastructure_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.integration_environment.infrastructure_resources
WHERE infrastructureResourceName = '{{ infrastructureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
