---
title: global_deleted_web_app_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - global_deleted_web_app_snapshots
  - app_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>global_deleted_web_app_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_deleted_web_app_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.global_deleted_web_app_snapshots" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deletedSiteId, subscriptionId" /> | Description for Get all deleted apps for a subscription. |

## `SELECT` examples

Description for Get all deleted apps for a subscription.


```sql
SELECT

FROM azure.app_service.global_deleted_web_app_snapshots
WHERE deletedSiteId = '{{ deletedSiteId }}'
AND subscriptionId = '{{ subscriptionId }}';
```