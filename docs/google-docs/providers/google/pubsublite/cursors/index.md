---
title: cursors
hide_title: false
hide_table_of_contents: false
keywords:
  - cursors
  - pubsublite
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

Creates, updates, deletes, gets or lists a <code>cursors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cursors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsublite.cursors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cursor" /> | `object` | A cursor that describes the position of a message within a topic partition. |
| <CopyableCode code="partition" /> | `string` | The partition this is for. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="cursor_projects_locations_subscriptions_cursors_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, subscriptionsId" /> | Returns all committed cursor information for a subscription. |

## `SELECT` examples

Returns all committed cursor information for a subscription.

```sql
SELECT
cursor,
partition
FROM google.pubsublite.cursors
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND subscriptionsId = '{{ subscriptionsId }}'; 
```
