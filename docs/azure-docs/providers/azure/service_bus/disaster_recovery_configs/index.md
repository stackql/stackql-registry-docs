---
title: disaster_recovery_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs
  - service_bus
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

Creates, updates, deletes, gets or lists a <code>disaster_recovery_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disaster_recovery_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.disaster_recovery_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties required to the Create Or Update Alias(Disaster Recovery configurations) |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all Alias(Disaster Recovery configurations) |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a new Alias(Disaster Recovery configuration) |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | Deletes an Alias(Disaster Recovery configuration) |
| <CopyableCode code="break_pairing" /> | `EXEC` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, data__name" /> | Check the give namespace name availability. |
| <CopyableCode code="fail_over" /> | `EXEC` | <CopyableCode code="alias, namespaceName, resourceGroupName, subscriptionId" /> | Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace |

## `SELECT` examples

Gets all Alias(Disaster Recovery configurations)


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.service_bus.disaster_recovery_configs
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disaster_recovery_configs</code> resource.

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
INSERT INTO azure.service_bus.disaster_recovery_configs (
alias,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ alias }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
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
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>disaster_recovery_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_bus.disaster_recovery_configs
WHERE alias = '{{ alias }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
