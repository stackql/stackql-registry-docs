---
title: migration_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_configs
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

Creates, updates, deletes, gets or lists a <code>migration_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.migration_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties required to the Create Migration Configuration |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configName, namespaceName, resourceGroupName, subscriptionId" /> | Retrieves Migration Config |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all migrationConfigurations |
| <CopyableCode code="create_and_start_migration" /> | `INSERT` | <CopyableCode code="configName, namespaceName, resourceGroupName, subscriptionId" /> | Creates Migration configuration and starts migration of entities from Standard to Premium namespace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a MigrationConfiguration |
| <CopyableCode code="complete_migration" /> | `EXEC` | <CopyableCode code="configName, namespaceName, resourceGroupName, subscriptionId" /> | This operation Completes Migration of entities by pointing the connection strings to Premium namespace and any entities created after the operation will be under Premium Namespace. CompleteMigration operation will fail when entity migration is in-progress. |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="configName, namespaceName, resourceGroupName, subscriptionId" /> | This operation reverts Migration |

## `SELECT` examples

Gets all migrationConfigurations


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.service_bus.migration_configs
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>migration_configs</code> resource.

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
INSERT INTO azure.service_bus.migration_configs (
configName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ configName }}',
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

Deletes the specified <code>migration_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_bus.migration_configs
WHERE configName = '{{ configName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
