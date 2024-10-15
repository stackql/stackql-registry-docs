---
title: hybrid_connections_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections_authorization_rules
  - relay
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

Creates, updates, deletes, gets or lists a <code>hybrid_connections_authorization_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_connections_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.hybrid_connections_authorization_rules" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Hybrid connection authorization rule for a hybrid connection by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Authorization rules for a hybrid connection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates an authorization rule for a hybrid connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a hybrid connection authorization rule. |

## `SELECT` examples

Authorization rules for a hybrid connection.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.relay.hybrid_connections_authorization_rules
WHERE hybridConnectionName = '{{ hybridConnectionName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hybrid_connections_authorization_rules</code> resource.

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
INSERT INTO azure.relay.hybrid_connections_authorization_rules (
authorizationRuleName,
hybridConnectionName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ authorizationRuleName }}',
'{{ hybridConnectionName }}',
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

Deletes the specified <code>hybrid_connections_authorization_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.relay.hybrid_connections_authorization_rules
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND hybridConnectionName = '{{ hybridConnectionName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
