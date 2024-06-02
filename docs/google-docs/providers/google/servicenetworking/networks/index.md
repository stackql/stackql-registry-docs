---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
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
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="servicenetworking.networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloudsqlConfigs" /> | `array` | Represents one or multiple Cloud SQL configurations. |
| <CopyableCode code="consumerExportCustomRoutes" /> | `boolean` | Export custom routes flag value for peering from consumer to producer. |
| <CopyableCode code="consumerExportSubnetRoutesWithPublicIp" /> | `boolean` | Export subnet routes with public ip flag value for peering from consumer to producer. |
| <CopyableCode code="consumerImportCustomRoutes" /> | `boolean` | Import custom routes flag value for peering from consumer to producer. |
| <CopyableCode code="consumerImportSubnetRoutesWithPublicIp" /> | `boolean` | Import subnet routes with public ip flag value for peering from consumer to producer. |
| <CopyableCode code="producerExportCustomRoutes" /> | `boolean` | Export custom routes flag value for peering from producer to consumer. |
| <CopyableCode code="producerExportSubnetRoutesWithPublicIp" /> | `boolean` | Export subnet routes with public ip flag value for peering from producer to consumer. |
| <CopyableCode code="producerImportCustomRoutes" /> | `boolean` | Import custom routes flag value for peering from producer to consumer. |
| <CopyableCode code="producerImportSubnetRoutesWithPublicIp" /> | `boolean` | Import subnet routes with public ip flag value for peering from producer to consumer. |
| <CopyableCode code="producerNetwork" /> | `string` | Output only. The VPC host network that is used to host managed service instances. In the format, projects/&#123;project&#125;/global/networks/&#123;network&#125; where &#123;project&#125; is the project number e.g. '12345' and &#123;network&#125; is the network name. |
| <CopyableCode code="reservedRanges" /> | `array` | Output only. The reserved ranges associated with this private service access connection. |
| <CopyableCode code="usedIpRanges" /> | `array` | Output only. The IP ranges already in use by consumer or producer |
| <CopyableCode code="vpcScReferenceArchitectureEnabled" /> | `boolean` | Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> |
