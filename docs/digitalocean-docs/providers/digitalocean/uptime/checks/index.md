---
title: checks
hide_title: false
hide_table_of_contents: false
keywords:
  - checks
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

Creates, updates, deletes, gets or lists a <code>checks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.uptime.checks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the check. |
| <CopyableCode code="name" /> | `string` | A human-friendly display name. |
| <CopyableCode code="enabled" /> | `boolean` | A boolean value indicating whether the check is enabled/disabled. |
| <CopyableCode code="regions" /> | `array` | An array containing the selected regions to perform healthchecks from. |
| <CopyableCode code="target" /> | `string` | The endpoint to perform healthchecks on. |
| <CopyableCode code="type" /> | `string` | The type of health check to perform. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="uptime_get_check" /> | `SELECT` | <CopyableCode code="check_id" /> | To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`. |
| <CopyableCode code="uptime_list_checks" /> | `SELECT` | <CopyableCode code="" /> | To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`. |
| <CopyableCode code="uptime_create_check" /> | `INSERT` | <CopyableCode code="" /> | To create an Uptime check, send a POST request to `/v2/uptime/checks` specifying the attributes in the table below in the JSON body. |
| <CopyableCode code="uptime_delete_check" /> | `DELETE` | <CopyableCode code="check_id" /> | To delete an Uptime check, send a DELETE request to `/v2/uptime/checks/$CHECK_ID`. A 204 status code with no body will be returned in response to a successful request. Deleting a check will also delete alerts associated with the check. |
| <CopyableCode code="uptime_update_check" /> | `EXEC` | <CopyableCode code="check_id" /> | To update the settings of an Uptime check, send a PUT request to `/v2/uptime/checks/$CHECK_ID`. |

## `SELECT` examples

To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`.


```sql
SELECT
id,
name,
enabled,
regions,
target,
type
FROM digitalocean.uptime.checks
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>checks</code> resource.

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
INSERT INTO digitalocean.uptime.checks (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: checks
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>checks</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.uptime.checks
WHERE check_id = '{{ check_id }}';
```
