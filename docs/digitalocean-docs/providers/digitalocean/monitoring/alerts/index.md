---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.monitoring.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="monitoring_get_alert_policy" /> | `SELECT` | <CopyableCode code="alert_uuid" /> | To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/{alert_uuid}` |
| <CopyableCode code="monitoring_list_alert_policy" /> | `SELECT` | <CopyableCode code="" /> | Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`. |
| <CopyableCode code="monitoring_create_alert_policy" /> | `INSERT` | <CopyableCode code="data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window" /> | To create a new alert, send a POST request to `/v2/monitoring/alerts`. |
| <CopyableCode code="monitoring_delete_alert_policy" /> | `DELETE` | <CopyableCode code="alert_uuid" /> | To delete an alert policy, send a DELETE request to `/v2/monitoring/alerts/{alert_uuid}` |
| <CopyableCode code="monitoring_update_alert_policy" /> | `EXEC` | <CopyableCode code="alert_uuid, data__alerts, data__compare, data__description, data__enabled, data__entities, data__tags, data__type, data__value, data__window" /> | To update en existing policy, send a PUT request to `v2/monitoring/alerts/{alert_uuid}`. |

## `SELECT` examples

Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`.


```sql
SELECT
column_anon
FROM digitalocean.monitoring.alerts
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alerts</code> resource.

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
INSERT INTO digitalocean.monitoring.alerts (
data__alerts,
data__compare,
data__description,
data__enabled,
data__entities,
data__tags,
data__type,
data__value,
data__window
)
SELECT 
'{{ alerts }}',
'{{ compare }}',
'{{ description }}',
'{{ enabled }}',
'{{ entities }}',
'{{ tags }}',
'{{ type }}',
'{{ value }}',
'{{ window }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: alerts
  props:
    - name: data__alerts
      value: string
    - name: data__compare
      value: string
    - name: data__description
      value: string
    - name: data__enabled
      value: string
    - name: data__entities
      value: string
    - name: data__tags
      value: string
    - name: data__type
      value: string
    - name: data__value
      value: string
    - name: data__window
      value: string
    - name: alerts
      props:
        - name: email
          value: array
        - name: slack
          value: array
          props:
            - name: channel
              value: string
            - name: url
              value: string
    - name: compare
      value: string
    - name: description
      value: string
    - name: enabled
      value: boolean
    - name: entities
      value: array
    - name: tags
      value: array
    - name: type
      value: string
    - name: value
      value: number
    - name: window
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>alerts</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.monitoring.alerts
WHERE alert_uuid = '{{ alert_uuid }}';
```
