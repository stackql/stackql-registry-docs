---
title: videos
hide_title: false
hide_table_of_contents: false
keywords:
  - videos
  - youtube
  - youtube    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/youtube/stackql-youtube-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>videos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.videos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube uses to uniquely identify the video. |
| `ageGating` | `object` |  |
| `snippet` | `object` | Basic details about a video, including title, description, uploader, thumbnails and category. |
| `processingDetails` | `object` | Describes processing status and progress and availability of some other Video resource parts. |
| `status` | `object` | Basic details about a video category, such as its localized title. Next Id: 18 |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#video". |
| `contentDetails` | `object` | Details about the content of a YouTube Video. |
| `fileDetails` | `object` | Describes original video file properties, including technical details about audio and video streams, but also metadata information like content length, digitization time, or geotagging information. |
| `liveStreamingDetails` | `object` | Details about the live streaming metadata. |
| `player` | `object` | Player to be used for a video playback. |
| `projectDetails` | `object` | DEPRECATED. b/157517979: This part was never populated after it was added. However, it sees non-zero traffic because there is generated client code in the wild that refers to it [1]. We keep this field and do NOT remove it because otherwise V3 would return an error when this part gets requested [2]. [1] https://developers.google.com/resources/api-libraries/documentation/youtube/v3/csharp/latest/classGoogle_1_1Apis_1_1YouTube_1_1v3_1_1Data_1_1VideoProjectDetails.html [2] http://google3/video/youtube/src/python/servers/data_api/common.py?l=1565-1569&rcl=344141677 |
| `recordingDetails` | `object` | Recording information associated with the video. |
| `suggestions` | `object` | Specifies suggestions on how to improve video content, including encoding hints, tag suggestions, and editor suggestions. |
| `monetizationDetails` | `object` | Details about monetization of a YouTube Video. |
| `topicDetails` | `object` | Freebase topic information related to the video. |
| `localizations` | `object` | The localizations object contains localized versions of the basic details about the video, such as its title and description. |
| `statistics` | `object` | Statistics about the video, such as the number of times the video was viewed or liked. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `insert` | `INSERT` | `part` | Inserts a new resource into this collection. |
| `delete` | `DELETE` | `id` | Deletes a resource. |
| `rate` | `EXEC` | `id, rating` | Adds a like or dislike rating to a video or removes a rating from a video. |
| `reportAbuse` | `EXEC` |  | Report abuse for a video. |
| `update` | `EXEC` | `part` | Updates an existing resource. |
