---
title: regional_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - regional_endpoints
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>regional_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="networkconnectivity.regional_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a RegionalEndpoint. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/regionalEndpoints/&#123;regional_endpoint&#125;`. |
| <CopyableCode code="description" /> | `string` | Optional. A description of this resource. |
| <CopyableCode code="accessType" /> | `string` | Required. The access type of this regional endpoint. This field is reflected in the PSC Forwarding Rule configuration to enable global access. |
| <CopyableCode code="address" /> | `string` | Optional. The IP Address of the Regional Endpoint. When no address is provided, an IP from the subnetwork is allocated. Use one of the following formats: * IPv4 address as in `10.0.0.1` * Address resource URI as in `projects/&#123;project&#125;/regions/&#123;region&#125;/addresses/&#123;address_name&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the RegionalEndpoint was created. |
| <CopyableCode code="ipAddress" /> | `string` | Output only. The literal IP address of the PSC Forwarding Rule created on behalf of the customer. This field is deprecated. Use address instead. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | The name of the VPC network for this private regional endpoint. Format: `projects/&#123;project&#125;/global/networks/&#123;network&#125;` |
| <CopyableCode code="pscForwardingRule" /> | `string` | Output only. The resource reference of the PSC Forwarding Rule created on behalf of the customer. Format: `//compute.googleapis.com/projects/&#123;project&#125;/regions/&#123;region&#125;/forwardingRules/&#123;forwarding_rule_name&#125;` |
| <CopyableCode code="subnetwork" /> | `string` | The name of the subnetwork from which the IP address will be allocated. Format: `projects/&#123;project&#125;/regions/&#123;region&#125;/subnetworks/&#123;subnetwork&#125;` |
| <CopyableCode code="targetGoogleApi" /> | `string` | Required. The service endpoint this private regional endpoint connects to. Format: `&#123;apiname&#125;.&#123;region&#125;.p.rep.googleapis.com` Example: "cloudkms.us-central1.p.rep.googleapis.com". |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the RegionalEndpoint was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, regionalEndpointsId" /> | Gets details of a single RegionalEndpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists RegionalEndpoints in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new RegionalEndpoint in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, regionalEndpointsId" /> | Deletes a single RegionalEndpoint. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists RegionalEndpoints in a given project and location. |
