---
title: locations_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_settings
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>locations_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.locations_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the settings resource. Format: projects/{project}/locations/{location}/settings |
| `updateTime` | `string` | Output only. The time at which the settings were last updated. |
| `analysisConfig` | `object` | Default configuration when creating Analyses in Insights. |
| `conversationTtl` | `string` | The default TTL for newly-created conversations. If a conversation has a specified expiration, that value will be used instead. Changing this value will not change the expiration of existing conversations. Conversations with no expire time persist until they are deleted. |
| `createTime` | `string` | Output only. The time at which the settings was created. |
| `languageCode` | `string` | A language code to be applied to each transcript segment unless the segment already specifies a language code. Language code defaults to "en-US" if it is neither specified on the segment nor here. |
| `pubsubNotificationSettings` | `object` | A map that maps a notification trigger to a Pub/Sub topic. Each time a specified trigger occurs, Insights will notify the corresponding Pub/Sub topic. Keys are notification triggers. Supported keys are: * "all-triggers": Notify each time any of the supported triggers occurs. * "create-analysis": Notify each time an analysis is created. * "create-conversation": Notify each time a conversation is created. * "export-insights-data": Notify each time an export is complete. * "update-conversation": Notify each time a conversation is updated via UpdateConversation. Values are Pub/Sub topics. The format of each Pub/Sub topic is: projects/{project}/topics/{topic} |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_getSettings` | `SELECT` | `locationsId, projectsId` |
