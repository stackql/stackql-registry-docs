---
title: notification_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_operations
  - marketplace_notifications
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

Creates, updates, deletes, gets or lists a <code>notification_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace_notifications.notification_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the operation |
| <CopyableCode code="display" /> | `object` | Operation display payload |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | operation origin |
| <CopyableCode code="properties" /> | `object` | operation properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> |  |

## `SELECT` examples




```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure_extras.marketplace_notifications.notification_operations
;
```