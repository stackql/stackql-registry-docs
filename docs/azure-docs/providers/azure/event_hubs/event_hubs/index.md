---
title: event_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_hubs
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>event_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.event_hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties supplied to the Create Or Update Event Hub operation. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets an Event Hubs description for the specified Event Hub. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all the Event Hubs in a Namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a new Event Hub as a nested resource within a Namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes an Event Hub from the specified Namespace and resource group. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the ACS and SAS connection strings for the Event Hub. |

## `SELECT` examples

Gets all the Event Hubs in a Namespace.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.event_hubs.event_hubs
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_hubs</code> resource.

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
INSERT INTO azure.event_hubs.event_hubs (
eventHubName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ eventHubName }}',
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

Deletes the specified <code>event_hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_hubs.event_hubs
WHERE eventHubName = '{{ eventHubName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
