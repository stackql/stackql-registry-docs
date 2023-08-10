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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `producerExportCustomRoutes` | `boolean` | Export custom routes flag value for peering from producer to consumer. |
| `vpcScReferenceArchitectureEnabled` | `boolean` | Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network. |
| `consumerExportCustomRoutes` | `boolean` | Export custom routes flag value for peering from consumer to producer. |
| `consumerImportSubnetRoutesWithPublicIp` | `boolean` | Import subnet routes with public ip flag value for peering from consumer to producer. |
| `producerImportSubnetRoutesWithPublicIp` | `boolean` | Import subnet routes with public ip flag value for peering from producer to consumer. |
| `producerNetwork` | `string` | Output only. The VPC host network that is used to host managed service instances. In the format, projects/&#123;project&#125;/global/networks/&#123;network&#125; where &#123;project&#125; is the project number e.g. '12345' and &#123;network&#125; is the network name. |
| `cloudsqlConfigs` | `array` | Represents one or multiple Cloud SQL configurations. |
| `consumerExportSubnetRoutesWithPublicIp` | `boolean` | Export subnet routes with public ip flag value for peering from consumer to producer. |
| `consumerImportCustomRoutes` | `boolean` | Import custom routes flag value for peering from consumer to producer. |
| `reservedRanges` | `array` | Output only. The reserved ranges associated with this private service access connection. |
| `producerExportSubnetRoutesWithPublicIp` | `boolean` | Export subnet routes with public ip flag value for peering from producer to consumer. |
| `producerImportCustomRoutes` | `boolean` | Import custom routes flag value for peering from producer to consumer. |
| `usedIpRanges` | `array` | Output only. The IP ranges already in use by consumer or producer |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networksId, projectsId, servicesId` |
