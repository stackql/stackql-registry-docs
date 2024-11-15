---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - snapshots
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.snapshots.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="snapshots_get" /> | `SELECT` | <CopyableCode code="snapshot_id" /> | To retrieve information about a snapshot, send a GET request to `/v2/snapshots/$SNAPSHOT_ID`. The response will be a JSON object with a key called `snapshot`. The value of this will be an snapshot object containing the standard snapshot attributes. |
| <CopyableCode code="snapshots_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the snapshots available on your account, send a GET request to `/v2/snapshots`. The response will be a JSON object with a key called `snapshots`. This will be set to an array of `snapshot` objects, each of which will contain the standard snapshot attributes. ### Filtering Results by Resource Type It's possible to request filtered results by including certain query parameters. #### List Droplet Snapshots To retrieve only snapshots based on Droplets, include the `resource_type` query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`. #### List Volume Snapshots To retrieve only snapshots based on volumes, include the `resource_type` query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`. |
| <CopyableCode code="snapshots_delete" /> | `DELETE` | <CopyableCode code="snapshot_id" /> | Both Droplet and volume snapshots are managed through the `/v2/snapshots/` endpoint. To delete a snapshot, send a DELETE request to `/v2/snapshots/$SNAPSHOT_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |

## `SELECT` examples

To list all of the snapshots available on your account, send a GET request to `/v2/snapshots`. The response will be a JSON object with a key called `snapshots`. This will be set to an array of `snapshot` objects, each of which will contain the standard snapshot attributes. ### Filtering Results by Resource Type It's possible to request filtered results by including certain query parameters. #### List Droplet Snapshots To retrieve only snapshots based on Droplets, include the `resource_type` query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`. #### List Volume Snapshots To retrieve only snapshots based on volumes, include the `resource_type` query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.


```sql
SELECT
column_anon
FROM digitalocean.snapshots.snapshots
;
```
## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.snapshots.snapshots
WHERE snapshot_id = '{{ snapshot_id }}';
```
