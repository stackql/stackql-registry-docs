---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.channels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the channel. Must be unique within the location on the project and must be in `projects/&#123;project&#125;/locations/&#123;location&#125;/channels/&#123;channel_id&#125;` format. |
| `createTime` | `string` | Output only. The creation time. |
| `activationToken` | `string` | Output only. The activation token for the channel. The token must be used by the provider to register the channel for publishing. |
| `provider` | `string` | The name of the event provider (e.g. Eventarc SaaS partner) associated with the channel. This provider will be granted permissions to publish events to the channel. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/providers/&#123;provider_id&#125;`. |
| `cryptoKeyName` | `string` | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| `uid` | `string` | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `pubsubTopic` | `string` | Output only. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/&#123;project&#125;/topics/&#123;topic_id&#125;`. |
| `state` | `string` | Output only. The state of a Channel. |
| `updateTime` | `string` | Output only. The last-modified time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `channelsId, locationsId, projectsId` | Get a single Channel. |
| `list` | `SELECT` | `locationsId, projectsId` | List channels. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new channel in a particular project and location. |
| `delete` | `DELETE` | `channelsId, locationsId, projectsId` | Delete a single channel. |
| `_list` | `EXEC` | `locationsId, projectsId` | List channels. |
| `patch` | `EXEC` | `channelsId, locationsId, projectsId` | Update a single channel. |
