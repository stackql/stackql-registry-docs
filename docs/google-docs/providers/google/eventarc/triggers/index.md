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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the trigger. Must be unique within the location of the project and must be in `projects/{project}/locations/{location}/triggers/{trigger}` format. |
| `uid` | `string` | Output only. Server-assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `transport` | `object` | Represents the transport intermediaries created for the trigger to deliver events. |
| `destination` | `object` | Represents a target of an invocation over HTTP. |
| `channel` | `string` | Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners. |
| `conditions` | `object` | Output only. The reason(s) why a trigger is in FAILED state. |
| `etag` | `string` | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on create requests to ensure that the client has an up-to-date value before proceeding. |
| `labels` | `object` | Optional. User labels attached to the triggers that can be used to group resources. |
| `createTime` | `string` | Output only. The creation time. |
| `eventFilters` | `array` | Required. null The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `serviceAccount` | `string` | Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The principal who calls this API must have the `iam.serviceAccounts.actAs` permission in the service account. See https://cloud.google.com/iam/docs/understanding-service-accounts?hl=en#sa_common for more information. For Cloud Run destinations, this service account is used to generate identity tokens when invoking the service. See https://cloud.google.com/run/docs/triggering/pubsub-push#create-service-account for information on how to invoke authenticated Cloud Run services. To create Audit Log triggers, the service account should also have the `roles/eventarc.eventReceiver` IAM role. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_triggers_get` | `SELECT` | `locationsId, projectsId, triggersId` | Get a single trigger. |
| `projects_locations_triggers_list` | `SELECT` | `locationsId, projectsId` | List triggers. |
| `projects_locations_triggers_create` | `INSERT` | `locationsId, projectsId` | Create a new trigger in a particular project and location. |
| `projects_locations_triggers_delete` | `DELETE` | `locationsId, projectsId, triggersId` | Delete a single trigger. |
| `projects_locations_triggers_patch` | `EXEC` | `locationsId, projectsId, triggersId` | Update a single trigger. |
