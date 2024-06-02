---
title: dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones
  - servicenetworking
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="servicenetworking.dns_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="consumerPeeringZone" /> | `object` |
| <CopyableCode code="producerPrivateZone" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsZonesId, networksId, projectsId, servicesId" /> | Service producers can use this method to retrieve a DNS zone in the shared producer host project and the matching peering zones in consumer project |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> | * Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project. * |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="servicesId" /> | Service producers can use this method to add private DNS zones in the shared producer host project and matching peering zones in the consumer project. |
| <CopyableCode code="remove" /> | `EXEC` | <CopyableCode code="servicesId" /> | Service producers can use this method to remove private DNS zones in the shared producer host project and matching peering zones in the consumer project. |
