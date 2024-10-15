---
title: express_route_provider_ports_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_provider_ports_locations
  - network
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

Creates, updates, deletes, gets or lists a <code>express_route_provider_ports_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_provider_ports_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_provider_ports_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of ExpressRouteProviderPort. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all the ExpressRouteProviderPorts in a subscription. |

## `SELECT` examples

Retrieves all the ExpressRouteProviderPorts in a subscription.


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.express_route_provider_ports_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```