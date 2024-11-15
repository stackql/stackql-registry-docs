---
title: deployments_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_logs
  - apps
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

Creates, updates, deletes, gets or lists a <code>deployments_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.deployments_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="historic_urls" /> | `array` |  |
| <CopyableCode code="live_url" /> | `string` | A URL of the real-time live logs. This URL may use either the `https://` or `wss://` protocols and will keep pushing live logs as they become available. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="apps_get_logs_aggregate" /> | `SELECT` | <CopyableCode code="app_id, deployment_id, type" /> | Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. |

## `SELECT` examples

Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.


```sql
SELECT
historic_urls,
live_url
FROM digitalocean.apps.deployments_logs
WHERE app_id = '{{ app_id }}'
AND deployment_id = '{{ deployment_id }}'
AND type = '{{ type }}';
```