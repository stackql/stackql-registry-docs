---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - account
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.account.account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="droplet_limit" /> | `integer` | The total number of Droplets current user or team may have active at one time. |
| <CopyableCode code="email" /> | `string` | The email address used by the current user to register for DigitalOcean. |
| <CopyableCode code="email_verified" /> | `boolean` | If true, the user has verified their account via email. False otherwise. |
| <CopyableCode code="floating_ip_limit" /> | `integer` | The total number of Floating IPs the current user or team may have. |
| <CopyableCode code="status" /> | `string` | This value is one of "active", "warning" or "locked". |
| <CopyableCode code="status_message" /> | `string` | A human-readable message giving more details about the status of the account. |
| <CopyableCode code="team" /> | `object` | When authorized in a team context, includes information about the current team. |
| <CopyableCode code="uuid" /> | `string` | The unique universal identifier for the current user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` |  |
| <CopyableCode code="_get" /> | `EXEC` |  |
