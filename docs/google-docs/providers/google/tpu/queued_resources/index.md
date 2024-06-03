---
title: queued_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - queued_resources
  - tpu
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
<tr><td><b>Name</b></td><td><code>queued_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.queued_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Immutable. The name of the QueuedResource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the QueuedResource was created. |
| <CopyableCode code="guaranteed" /> | `object` | Guaranteed tier definition. |
| <CopyableCode code="queueingPolicy" /> | `object` | Defines the policy of the QueuedRequest. |
| <CopyableCode code="reservationName" /> | `string` | Optional. Name of the reservation in which the resource should be provisioned. Format: projects/&#123;project&#125;/locations/&#123;zone&#125;/reservations/&#123;reservation&#125; |
| <CopyableCode code="spot" /> | `object` | Spot tier definition. |
| <CopyableCode code="state" /> | `object` | QueuedResourceState defines the details of the QueuedResource request. |
| <CopyableCode code="tpu" /> | `object` | Details of the TPU resource(s) being requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Gets details of a queued resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists queued resources. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a QueuedResource TPU instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Deletes a QueuedResource TPU instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists queued resources. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, queuedResourcesId" /> | Resets a QueuedResource TPU instance |
