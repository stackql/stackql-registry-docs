---
title: gateways_capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways_capacities
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>gateways_capacities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways_capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.gateways_capacities" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Spring Cloud Gateway capacity. |

## `UPDATE` example

Updates a <code>gateways_capacities</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.gateways_capacities
SET 
sku = '{{ sku }}'
WHERE 
gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
