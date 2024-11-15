---
title: sinks_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks_destinations
  - monitoring
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sinks_destinations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sinks_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.sinks_destinations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_destination" /> | `SELECT` | <CopyableCode code="destination_uuid" /> | To get the details of a destination, send a GET request to `/v2/monitoring/sinks/destinations/${destination_uuid}`. |
| <CopyableCode code="monitoring_list_destinations" /> | `SELECT` | <CopyableCode code="" /> | To list all logging destinations, send a GET request to `/v2/monitoring/sinks/destinations`. |
| <CopyableCode code="monitoring_create_destination" /> | `INSERT` | <CopyableCode code="data__config, data__type" /> | To create a new destination, send a POST request to `/v2/monitoring/sinks/destinations`. |
| <CopyableCode code="monitoring_delete_destination" /> | `DELETE` | <CopyableCode code="destination_uuid" /> | To delete a destination and all associated sinks, send a DELETE request to `/v2/monitoring/sinks/destinations/${destination_uuid}`. |
| <CopyableCode code="monitoring_update_destination" /> | `UPDATE` | <CopyableCode code="destination_uuid, data__config, data__type" /> | To update the details of a destination, send a PATCH request to `/v2/monitoring/sinks/destinations/${destination_uuid}`. |

## `SELECT` examples

To list all logging destinations, send a GET request to `/v2/monitoring/sinks/destinations`.


```sql
SELECT
column_anon
FROM digitalocean.monitoring.sinks_destinations
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sinks_destinations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.monitoring.sinks_destinations (
data__name,
data__type,
data__config
)
SELECT 
'{{ name }}',
'{{ type }}',
'{{ config }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.monitoring.sinks_destinations (
data__config,
data__type
)
SELECT 
'{{ config }}',
'{{ type }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: sinks_destinations
  props:
    - name: data__config
      value: string
    - name: data__type
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: config
      props:
        - name: credentials
          props:
            - name: username
              value: string
            - name: password
              value: string
        - name: endpoint
          value: string
        - name: cluster_uuid
          value: string
        - name: cluster_name
          value: string
        - name: index_name
          value: string
        - name: retention_days
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sinks_destinations</code> resource.

```sql
/*+ update */
UPDATE digitalocean.monitoring.sinks_destinations
SET 
name = '{{ name }}',
type = '{{ type }}',
config = '{{ config }}'
WHERE 
destination_uuid = '{{ destination_uuid }}'
AND data__config = '{{ data__config }}'
AND data__type = '{{ data__type }}';
```

## `DELETE` example

Deletes the specified <code>sinks_destinations</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.monitoring.sinks_destinations
WHERE destination_uuid = '{{ destination_uuid }}';
```
