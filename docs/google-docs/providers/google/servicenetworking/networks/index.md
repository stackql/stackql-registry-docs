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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.networks" /></td></tr>
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
| <CopyableCode code="producerNetwork" /> | `string` | Output only. The VPC host network that is used to host managed service instances. In the format, projects/{project}/global/networks/{network} where {project} is the project number e.g. '12345' and {network} is the network name. |
| <CopyableCode code="reservedRanges" /> | `array` | Output only. The reserved ranges associated with this private service access connection. |
| <CopyableCode code="usedIpRanges" /> | `array` | Output only. The IP ranges already in use by consumer or producer |
| <CopyableCode code="vpcScReferenceArchitectureEnabled" /> | `boolean` | Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> | Service producers use this method to get the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP. |

## `SELECT` examples

Service producers use this method to get the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP.

```sql
SELECT
cloudsqlConfigs,
consumerExportCustomRoutes,
consumerExportSubnetRoutesWithPublicIp,
consumerImportCustomRoutes,
consumerImportSubnetRoutesWithPublicIp,
producerExportCustomRoutes,
producerExportSubnetRoutesWithPublicIp,
producerImportCustomRoutes,
producerImportSubnetRoutesWithPublicIp,
producerNetwork,
reservedRanges,
usedIpRanges,
vpcScReferenceArchitectureEnabled
FROM google.servicenetworking.networks
WHERE networksId = '{{ networksId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
