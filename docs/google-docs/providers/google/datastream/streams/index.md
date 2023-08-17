---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - datastream
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
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The stream's name. |
| `createTime` | `string` | Output only. The creation time of the stream. |
| `backfillNone` | `object` | Backfill strategy to disable automatic backfill for the Stream's objects. |
| `destinationConfig` | `object` | The configuration of the stream destination. |
| `errors` | `array` | Output only. Errors on the Stream. |
| `labels` | `object` | Labels. |
| `sourceConfig` | `object` | The configuration of the stream source. |
| `state` | `string` | The state of the stream. |
| `displayName` | `string` | Required. Display name. |
| `customerManagedEncryptionKey` | `string` | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |
| `updateTime` | `string` | Output only. The last update time of the stream. |
| `backfillAll` | `object` | Backfill strategy to automatically backfill the Stream's objects. Specific objects can be excluded. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, streamsId` | Use this method to get details about a stream. |
| `list` | `SELECT` | `locationsId, projectsId` | Use this method to list streams in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Use this method to create a stream. |
| `delete` | `DELETE` | `locationsId, projectsId, streamsId` | Use this method to delete a stream. |
| `_list` | `EXEC` | `locationsId, projectsId` | Use this method to list streams in a project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, streamsId` | Use this method to update the configuration of a stream. |
| `run` | `EXEC` | `locationsId, projectsId, streamsId` | Use this method to start, resume or recover a stream with a non default CDC strategy. NOTE: This feature is currently experimental. |
