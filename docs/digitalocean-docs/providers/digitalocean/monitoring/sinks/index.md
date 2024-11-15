---
title: sinks
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks
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

Creates, updates, deletes, gets or lists a <code>sinks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.sinks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_sink" /> | `SELECT` | <CopyableCode code="sink_uuid" /> | To get the details of a sink (resources and destination), send a GET request to `/v2/monitoring/sinks/${sink_uuid}`. |
| <CopyableCode code="monitoring_list_sinks" /> | `SELECT` | <CopyableCode code="" /> | To list all sinks, send a GET request to `/v2/monitoring/sinks`. |
| <CopyableCode code="monitoring_create_sink" /> | `INSERT` | <CopyableCode code="" /> | To create a new sink, send a POST request to `/v2/monitoring/sinks`. Forwards logs from the resources identified in `resources` to the specified pre-existing destination. |
| <CopyableCode code="monitoring_delete_sink" /> | `DELETE` | <CopyableCode code="sink_uuid" /> | To delete a sink, send a DELETE request to `/v2/monitoring/sinks/${sink_uuid}`. |

## `SELECT` examples

To list all sinks, send a GET request to `/v2/monitoring/sinks`.


```sql
SELECT
column_anon
FROM digitalocean.monitoring.sinks
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sinks</code> resource.

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
INSERT INTO digitalocean.monitoring.sinks (
data__destination_uuid,
data__resources
)
SELECT 
'{{ destination_uuid }}',
'{{ resources }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: sinks
  props:
    - name: destination_uuid
      value: string
    - name: resources
      value: array
      props:
        - name: urn
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sinks</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.monitoring.sinks
WHERE sink_uuid = '{{ sink_uuid }}';
```
