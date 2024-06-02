---
title: management_dns_zone_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - management_dns_zone_bindings
  - vmwareengine
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
<tr><td><b>Name</b></td><td><code>management_dns_zone_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmwareengine.management_dns_zone_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this binding. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding` |
| <CopyableCode code="description" /> | `string` | User-provided description for this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
| <CopyableCode code="vmwareEngineNetwork" /> | `string` | Network to bind is a VMware Engine network. Specify the name in the following form for VMware engine network: `projects/&#123;project&#125;/locations/global/vmwareEngineNetworks/&#123;vmware_engine_network_id&#125;`. `&#123;project&#125;` can either be a project number or a project ID. |
| <CopyableCode code="vpcNetwork" /> | `string` | Network to bind is a standard consumer VPC. Specify the name in the following form for consumer VPC network: `projects/&#123;project&#125;/global/networks/&#123;network_id&#125;`. `&#123;project&#125;` can either be a project number or a project ID. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Retrieves a 'ManagementDnsZoneBinding' resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists Consumer VPCs bound to Management DNS Zone of a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new `ManagementDnsZoneBinding` resource in a private cloud. This RPC creates the DNS binding and the resource that represents the DNS binding of the consumer VPC network to the management DNS zone. A management DNS zone is the Cloud DNS cross-project binding zone that VMware Engine creates for each private cloud. It contains FQDNs and corresponding IP addresses for the private cloud's ESXi hosts and management VM appliances like vCenter and NSX Manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Deletes a `ManagementDnsZoneBinding` resource. When a management DNS zone binding is deleted, the corresponding consumer VPC network is no longer bound to the management DNS zone. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists Consumer VPCs bound to Management DNS Zone of a given private cloud. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Updates a `ManagementDnsZoneBinding` resource. Only fields specified in `update_mask` are applied. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="locationsId, managementDnsZoneBindingsId, privateCloudsId, projectsId" /> | Retries to create a `ManagementDnsZoneBinding` resource that is in failed state. |
