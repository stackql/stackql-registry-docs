---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - networkzone
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.networkzone.zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="asns" /> | `array` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="gateways" /> | `array` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="locations" /> | `array` |
| <CopyableCode code="proxies" /> | `array` |
| <CopyableCode code="proxyType" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="system" /> | `boolean` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="usage" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="zoneId, subdomain" /> | Fetches a network zone from your Okta organization by `id`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new network zone to your Okta organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="zoneId, subdomain" /> | Removes network zone. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="zoneId, subdomain" /> | Activate Network Zone |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="zoneId, subdomain" /> | Deactivates a network zone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="zoneId, subdomain" /> | Updates a network zone in your organization. |
