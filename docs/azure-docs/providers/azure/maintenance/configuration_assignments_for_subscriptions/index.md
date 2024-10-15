---
title: configuration_assignments_for_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_assignments_for_subscriptions
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

Creates, updates, deletes, gets or lists a <code>configuration_assignments_for_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_assignments_for_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.configuration_assignments_for_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_assignments_for_subscriptions', value: 'view', },
        { label: 'configuration_assignments_for_subscriptions', value: 'resource', },
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationAssignmentName, subscriptionId" /> | Get configuration assignment for resource.. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationAssignmentName, subscriptionId" /> | Register configuration for resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationAssignmentName, subscriptionId" /> | Unregister configuration for resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="configurationAssignmentName, subscriptionId" /> | Register configuration for resource. |

## `SELECT` examples

Get configuration assignment for resource..

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_assignments_for_subscriptions', value: 'view', },
        { label: 'configuration_assignments_for_subscriptions', value: 'resource', },
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
resource_id,
subscriptionId,
type
FROM azure.maintenance.vw_configuration_assignments_for_subscriptions
WHERE configurationAssignmentName = '{{ configurationAssignmentName }}'
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
FROM azure.maintenance.configuration_assignments_for_subscriptions
WHERE configurationAssignmentName = '{{ configurationAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_assignments_for_subscriptions</code> resource.

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
INSERT INTO azure.maintenance.configuration_assignments_for_subscriptions (
configurationAssignmentName,
subscriptionId,
location,
properties
)
SELECT 
'{{ configurationAssignmentName }}',
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

## `UPDATE` example

Updates a <code>configuration_assignments_for_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.maintenance.configuration_assignments_for_subscriptions
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
configurationAssignmentName = '{{ configurationAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>configuration_assignments_for_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.maintenance.configuration_assignments_for_subscriptions
WHERE configurationAssignmentName = '{{ configurationAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
