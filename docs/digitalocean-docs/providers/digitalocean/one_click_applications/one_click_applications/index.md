---
title: one_click_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - one_click_applications
  - one_click_applications
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

Creates, updates, deletes, gets or lists a <code>one_click_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>one_click_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.one_click_applications.one_click_applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="one_clicks_list" /> | `SELECT` | <CopyableCode code="" /> | To list all available 1-Click applications, send a GET request to `/v2/1-clicks`. The `type` may be provided as query paramater in order to restrict results to a certain type of 1-Click, for example: `/v2/1-clicks?type=droplet`. Current supported types are `kubernetes` and `droplet`. The response will be a JSON object with a key called `1_clicks`. This will be set to an array of 1-Click application data, each of which will contain the the slug and type for the 1-Click. |
| <CopyableCode code="one_clicks_install_kubernetes" /> | `EXEC` | <CopyableCode code="data__addon_slugs, data__cluster_uuid" /> | To install a Kubernetes 1-Click application on a cluster, send a POST request to `/v2/1-clicks/kubernetes`. The `addon_slugs` and `cluster_uuid` must be provided as body parameter in order to specify which 1-Click application(s) to install. To list all available 1-Click Kubernetes applications, send a request to `/v2/1-clicks?type=kubernetes`. |

## `SELECT` examples

To list all available 1-Click applications, send a GET request to `/v2/1-clicks`. The `type` may be provided as query paramater in order to restrict results to a certain type of 1-Click, for example: `/v2/1-clicks?type=droplet`. Current supported types are `kubernetes` and `droplet`. The response will be a JSON object with a key called `1_clicks`. This will be set to an array of 1-Click application data, each of which will contain the the slug and type for the 1-Click.


```sql
SELECT
column_anon
FROM digitalocean.one_click_applications.one_click_applications
;
```