---
title: network_link_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - network_link_endpoints
  - networking
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>network_link_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_link_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.networking.network_link_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | The desired state of the Network Link Endpoint |
| <CopyableCode code="status" /> | `object` | The status of the Network Link Endpoint |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_networking_v1network_link_endpoint" /> | `SELECT` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a network link endpoint. |
| <CopyableCode code="list_networking_v1network_link_endpoints" /> | `SELECT` | <CopyableCode code="environment" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all network link endpoints. |
| <CopyableCode code="create_networking_v1network_link_endpoint" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a network link endpoint. |
| <CopyableCode code="delete_networking_v1network_link_endpoint" /> | `DELETE` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a network link endpoint. |
| <CopyableCode code="update_networking_v1network_link_endpoint" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a network link endpoint. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all network link endpoints.


```sql
SELECT
id,
_spec,
api_version,
kind,
metadata,
spec,
status
FROM confluent.networking.network_link_endpoints
WHERE environment = '{{ environment }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_link_endpoints</code> resource.

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
INSERT INTO confluent.networking.network_link_endpoints (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: network_link_endpoints
  props:
    - name: spec
      props:
        - name: environment
          value: string
        - name: network
          value: string
        - name: network_link_service
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_link_endpoints</code> resource.

```sql
/*+ update */
UPDATE confluent.networking.network_link_endpoints
SET 
spec = '{{ spec }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>network_link_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.networking.network_link_endpoints
WHERE environment = '{{ environment }}'
AND id = '{{ id }}';
```
