---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - apphub
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apphub.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of a Service. Format: "projects/&#123;host-project-id&#125;/locations/&#123;location&#125;/applications/&#123;application-id&#125;/services/&#123;service-id&#125;" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of a Service. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="discoveredService" /> | `string` | Required. Immutable. The resource name of the original discovered service. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Service. Can have a maximum length of 63 characters. |
| <CopyableCode code="serviceProperties" /> | `object` | Properties of an underlying cloud resource that can comprise a Service. |
| <CopyableCode code="serviceReference" /> | `object` | Reference to an underlying networking resource that can comprise a Service. |
| <CopyableCode code="state" /> | `string` | Output only. Service state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (UUID) for the `Service` in the UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Gets a Service in an Application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Services in an Application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Creates a Service in an Application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Deletes a Service from an Application. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Services in an Application. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Updates a Service in an Application. |
