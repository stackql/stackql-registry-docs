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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.eventarc.channels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the channel. Must be unique within the location on the project and must be in `projects/&#123;project&#125;/locations/&#123;location&#125;/channels/&#123;channel_id&#125;` format. |
| <CopyableCode code="activationToken" /> | `string` | Output only. The activation token for the channel. The token must be used by the provider to register the channel for publishing. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="cryptoKeyName" /> | `string` | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| <CopyableCode code="provider" /> | `string` | The name of the event provider (e.g. Eventarc SaaS partner) associated with the channel. This provider will be granted permissions to publish events to the channel. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/providers/&#123;provider_id&#125;`. |
| <CopyableCode code="pubsubTopic" /> | `string` | Output only. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/&#123;project&#125;/topics/&#123;topic_id&#125;`. |
| <CopyableCode code="state" /> | `string` | Output only. The state of a Channel. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Get a single Channel. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List channels. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new channel in a particular project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Delete a single channel. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List channels. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="channelsId, locationsId, projectsId" /> | Update a single channel. |
