---
title: configuration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_assignments
  - maintenance
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

Creates, updates, deletes, gets or lists a <code>configuration_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.configuration_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_assignments', value: 'view', },
        { label: 'configuration_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="configurationAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="maintenance_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for configuration assignment |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Get configuration assignment for resource.. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | List configurationAssignments for resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Register configuration for resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Unregister configuration for resource. |

## `SELECT` examples

List configurationAssignments for resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_assignments', value: 'view', },
        { label: 'configuration_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configurationAssignmentName,
filter,
location,
maintenance_configuration_id,
providerName,
resourceGroupName,
resourceName,
resourceType,
resource_id,
subscriptionId,
type
FROM azure.maintenance.vw_configuration_assignments
WHERE providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.maintenance.configuration_assignments
WHERE providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_assignments</code> resource.

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
INSERT INTO azure.maintenance.configuration_assignments (
configurationAssignmentName,
providerName,
resourceGroupName,
resourceName,
resourceType,
subscriptionId,
location,
properties
)
SELECT 
'{{ configurationAssignmentName }}',
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ resourceType }}',
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
        - name: maintenanceConfigurationId
          value: string
        - name: resourceId
          value: string
        - name: filter
          value:
            - name: resourceTypes
              value:
                - string
            - name: resourceGroups
              value:
                - string
            - name: osTypes
              value:
                - string
            - name: locations
              value:
                - string
            - name: tagSettings
              value:
                - name: tags
                  value: object
                - name: filterOperator
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configuration_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.maintenance.configuration_assignments
WHERE configurationAssignmentName = '{{ configurationAssignmentName }}'
AND providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
