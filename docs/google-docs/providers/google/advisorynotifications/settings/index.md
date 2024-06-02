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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="advisorynotifications.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the settings to retrieve. Format: organizations/&#123;organization&#125;/locations/&#123;location&#125;/settings or projects/&#123;projects&#125;/locations/&#123;location&#125;/settings. |
| <CopyableCode code="etag" /> | `string` | Required. Fingerprint for optimistic concurrency returned in Get requests. Must be provided for Update requests. If the value provided does not match the value known to the server, ABORTED will be thrown, and the client should retry the read-modify-write cycle. |
| <CopyableCode code="notificationSettings" /> | `object` | Required. Map of each notification type and its settings to get/set all settings at once. The server will validate the value for each notification type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_settings" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Get notification settings. |
| <CopyableCode code="update_settings" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Update notification settings. |
