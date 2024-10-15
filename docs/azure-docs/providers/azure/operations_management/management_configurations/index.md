---
title: management_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_configurations
  - operations_management
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

Creates, updates, deletes, gets or lists a <code>management_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.management_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_configurations', value: 'view', },
        { label: 'management_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="managementConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="template" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | ManagementConfiguration properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Retrieves the user ManagementConfiguration. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the ManagementConfigurations list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Creates or updates the ManagementConfiguration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Deletes the ManagementConfiguration in the subscription. |

## `SELECT` examples

Retrieves the ManagementConfigurations list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_configurations', value: 'view', },
        { label: 'management_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
application_id,
location,
managementConfigurationName,
parameters,
parent_resource_type,
provisioning_state,
resourceGroupName,
subscriptionId,
template,
type
FROM azure.operations_management.vw_management_configurations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.operations_management.management_configurations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_configurations</code> resource.

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
INSERT INTO azure.operations_management.management_configurations (
managementConfigurationName,
resourceGroupName,
subscriptionId,
location,
properties
)
SELECT 
'{{ managementConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: applicationId
          value: string
        - name: parentResourceType
          value: string
        - name: parameters
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: provisioningState
          value: string
        - name: template
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>management_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.operations_management.management_configurations
WHERE managementConfigurationName = '{{ managementConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
