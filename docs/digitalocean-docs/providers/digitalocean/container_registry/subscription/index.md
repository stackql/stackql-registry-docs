---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
  - container_registry
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.subscription" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_at" /> | `string` | The time at which the subscription was created. |
| <CopyableCode code="tier" /> | `object` |  |
| <CopyableCode code="updated_at" /> | `string` | The time at which the subscription was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_get_subscription" /> | `SELECT` |  | A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`. |
| <CopyableCode code="_registry_get_subscription" /> | `EXEC` |  | A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`. |
| <CopyableCode code="registry_update_subscription" /> | `EXEC` |  | After creating your registry, you can switch to a different subscription tier to better suit your needs. To do this, send a POST request to `/v2/registry/subscription`. |
