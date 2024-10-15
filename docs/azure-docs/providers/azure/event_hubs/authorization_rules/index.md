---
title: authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_rules
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

Creates, updates, deletes, gets or lists a <code>authorization_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.authorization_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties supplied to create or update AuthorizationRule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets an AuthorizationRule for an Event Hub by rule name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets the authorization rules for an Event Hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates an AuthorizationRule for the specified Event Hub. Creation/update of the AuthorizationRule will take a few seconds to take effect. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationRuleName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes an Event Hub AuthorizationRule. |

## `SELECT` examples

Gets the authorization rules for an Event Hub.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.event_hubs.authorization_rules
WHERE eventHubName = '{{ eventHubName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_rules</code> resource.

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
INSERT INTO azure.event_hubs.authorization_rules (
authorizationRuleName,
eventHubName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationRuleName }}',
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

Deletes the specified <code>authorization_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_hubs.authorization_rules
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND eventHubName = '{{ eventHubName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
