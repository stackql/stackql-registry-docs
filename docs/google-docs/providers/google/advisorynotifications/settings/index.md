---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - advisorynotifications
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.advisorynotifications.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the settings to retrieve. Format: organizations/{organization}/locations/{location}/settings or projects/{projects}/locations/{location}/settings. |
| <CopyableCode code="etag" /> | `string` | Required. Fingerprint for optimistic concurrency returned in Get requests. Must be provided for Update requests. If the value provided does not match the value known to the server, ABORTED will be thrown, and the client should retry the read-modify-write cycle. |
| <CopyableCode code="notificationSettings" /> | `object` | Required. Map of each notification type and its settings to get/set all settings at once. The server will validate the value for each notification type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_settings" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Get notification settings. |
| <CopyableCode code="update_settings" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId" /> | Update notification settings. |

## `SELECT` examples

Get notification settings.

```sql
SELECT
name,
etag,
notificationSettings
FROM google.advisorynotifications.settings
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a <code>settings</code> resource.

```sql
/*+ update */
UPDATE google.advisorynotifications.settings
SET 
etag = '{{ etag }}',
name = '{{ name }}',
notificationSettings = '{{ notificationSettings }}'
WHERE 
locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```
