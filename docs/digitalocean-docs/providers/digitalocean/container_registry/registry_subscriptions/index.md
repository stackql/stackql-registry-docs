---
title: registry_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_subscriptions
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>registry_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_get_subscription" /> | `SELECT` | <CopyableCode code="" /> | A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`. |
| <CopyableCode code="registry_update_subscription" /> | `UPDATE` | <CopyableCode code="" /> | After creating your registry, you can switch to a different subscription tier to better suit your needs. To do this, send a POST request to `/v2/registry/subscription`. |

## `SELECT` examples

A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`.


```sql
SELECT
column_anon
FROM digitalocean.container_registry.registry_subscriptions
;
```
## `UPDATE` example

Updates a <code>registry_subscriptions</code> resource.

```sql
/*+ update */
UPDATE digitalocean.container_registry.registry_subscriptions
SET 
tier_slug = '{{ tier_slug }}'
WHERE 
;
```
