---
title: droplets_associated_resources_delete_status
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets_associated_resources_delete_status
  - droplets
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

Creates, updates, deletes, gets or lists a <code>droplets_associated_resources_delete_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplets_associated_resources_delete_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.droplets_associated_resources_delete_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="completed_at" /> | `string` | A time value given in ISO8601 combined date and time format indicating when the requested action was completed. |
| <CopyableCode code="droplet" /> | `object` | An object containing information about a resource scheduled for deletion. |
| <CopyableCode code="failures" /> | `integer` | A count of the associated resources that failed to be destroyed, if any. |
| <CopyableCode code="resources" /> | `object` | An object containing additional information about resource related to a Droplet requested to be destroyed. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_get_destroy_associated_resources_status" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To check on the status of a request to destroy a Droplet with its associated resources, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint. |

## `SELECT` examples

To check on the status of a request to destroy a Droplet with its associated resources, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint.


```sql
SELECT
completed_at,
droplet,
failures,
resources
FROM digitalocean.droplets.droplets_associated_resources_delete_status
WHERE droplet_id = '{{ droplet_id }}';
```