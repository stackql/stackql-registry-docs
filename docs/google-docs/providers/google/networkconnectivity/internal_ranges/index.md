---
title: internal_ranges
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_ranges
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
<tr><td><b>Name</b></td><td><code>internal_ranges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.internal_ranges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of an internal range. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/internalRanges/&#123;internal_range&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| <CopyableCode code="description" /> | `string` | A description of this resource. |
| <CopyableCode code="createTime" /> | `string` | Time when the internal range was created. |
| <CopyableCode code="ipCidrRange" /> | `string` | The IP range that this internal range defines. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | The URL or resource ID of the network in which to reserve the internal range. The network cannot be deleted if there are any reserved internal ranges referring to it. Legacy networks are not supported. For example: https://www.googleapis.com/compute/v1/projects/&#123;project&#125;/locations/global/networks/&#123;network&#125; projects/&#123;project&#125;/locations/global/networks/&#123;network&#125; &#123;network&#125; |
| <CopyableCode code="overlaps" /> | `array` | Optional. Types of resources that are allowed to overlap with the current internal range. |
| <CopyableCode code="peering" /> | `string` | The type of peering set for this internal range. |
| <CopyableCode code="prefixLength" /> | `integer` | An alternate to ip_cidr_range. Can be set when trying to create a reservation that automatically finds a free range of the given size. If both ip_cidr_range and prefix_length are set, there is an error if the range sizes do not match. Can also be used during updates to change the range size. |
| <CopyableCode code="targetCidrRange" /> | `array` | Optional. Can be set to narrow down or pick a different address space while searching for a free range. If not set, defaults to the "10.0.0.0/8" address space. This can be used to search in other rfc-1918 address spaces like "172.16.0.0/12" and "192.168.0.0/16" or non-rfc-1918 address spaces used in the VPC. |
| <CopyableCode code="updateTime" /> | `string` | Time when the internal range was updated. |
| <CopyableCode code="usage" /> | `string` | The type of usage set for this InternalRange. |
| <CopyableCode code="users" /> | `array` | Output only. The list of resources that refer to this internal range. Resources that use the internal range for their range allocation are referred to as users of the range. Other resources mark themselves as users while doing so by creating a reference to this internal range. Having a user, based on this reference, prevents deletion of the internal range referred to. Can be empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internalRangesId, locationsId, projectsId" /> | Gets details of a single internal range. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists internal ranges in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new internal range in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internalRangesId, locationsId, projectsId" /> | Deletes a single internal range. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="internalRangesId, locationsId, projectsId" /> | Updates the parameters of a single internal range. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists internal ranges in a given project and location. |
