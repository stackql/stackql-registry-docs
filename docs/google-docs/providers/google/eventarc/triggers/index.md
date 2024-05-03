---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - eventarc
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.eventarc.triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the trigger. Must be unique within the location of the project and must be in `projects/&#123;project&#125;/locations/&#123;location&#125;/triggers/&#123;trigger&#125;` format. |
| <CopyableCode code="channel" /> | `string` | Optional. The name of the channel associated with the trigger in `projects/&#123;project&#125;/locations/&#123;location&#125;/channels/&#123;channel&#125;` format. You must provide a channel to receive events from Eventarc SaaS partners. |
| <CopyableCode code="conditions" /> | `object` | Output only. The reason(s) why a trigger is in FAILED state. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="destination" /> | `object` | Represents a target of an invocation over HTTP. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on create requests to ensure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="eventDataContentType" /> | `string` | Optional. EventDataContentType specifies the type of payload in MIME format that is expected from the CloudEvent data field. This is set to `application/json` if the value is not defined. |
| <CopyableCode code="eventFilters" /> | `array` | Required. Unordered list. The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination. |
| <CopyableCode code="labels" /> | `object` | Optional. User labels attached to the triggers that can be used to group resources. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The `iam.serviceAccounts.actAs` permission must be granted on the service account to allow a principal to impersonate the service account. For more information, see the [Roles and permissions](/eventarc/docs/all-roles-permissions) page specific to the trigger destination. |
| <CopyableCode code="transport" /> | `object` | Represents the transport intermediaries created for the trigger to deliver events. |
| <CopyableCode code="uid" /> | `string` | Output only. Server-assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Get a single trigger. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List triggers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new trigger in a particular project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Delete a single trigger. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List triggers. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, triggersId" /> | Update a single trigger. |
