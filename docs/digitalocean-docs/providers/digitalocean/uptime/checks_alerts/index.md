---
title: checks_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - checks_alerts
  - uptime
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

Creates, updates, deletes, gets or lists a <code>checks_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>checks_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.uptime.checks_alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the alert. |
| <CopyableCode code="name" /> | `string` | A human-friendly display name. |
| <CopyableCode code="comparison" /> | `string` | The comparison operator used against the alert's threshold. |
| <CopyableCode code="notifications" /> | `object` | The notification settings for a trigger alert. |
| <CopyableCode code="period" /> | `string` | Period of time the threshold must be exceeded to trigger the alert. |
| <CopyableCode code="threshold" /> | `integer` | The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. |
| <CopyableCode code="type" /> | `string` | The type of alert. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="uptime_get_alert" /> | `SELECT` | <CopyableCode code="alert_id, check_id" /> | To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |
| <CopyableCode code="uptime_list_alerts" /> | `SELECT` | <CopyableCode code="check_id" /> | To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`. |
| <CopyableCode code="uptime_create_alert" /> | `INSERT` | <CopyableCode code="check_id" /> | To create an Uptime alert, send a POST request to `/v2/uptime/checks/$CHECK_ID/alerts` specifying the attributes in the table below in the JSON body. |
| <CopyableCode code="uptime_delete_alert" /> | `DELETE` | <CopyableCode code="alert_id, check_id" /> | To delete an Uptime alert, send a DELETE request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. A 204 status code with no body will be returned in response to a successful request. |
| <CopyableCode code="uptime_update_alert" /> | `EXEC` | <CopyableCode code="alert_id, check_id" /> | To update the settings of an Uptime alert, send a PUT request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |

## `SELECT` examples

To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`.


```sql
SELECT
id,
name,
comparison,
notifications,
period,
threshold,
type
FROM digitalocean.uptime.checks_alerts
WHERE check_id = '{{ check_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>checks_alerts</code> resource.

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
INSERT INTO digitalocean.uptime.checks_alerts (
check_id
)
SELECT 
'{{ check_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: checks_alerts
  props:
    - name: check_id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>checks_alerts</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.uptime.checks_alerts
WHERE alert_id = '{{ alert_id }}'
AND check_id = '{{ check_id }}';
```
