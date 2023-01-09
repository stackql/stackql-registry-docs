---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - games
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the snapshot. |
| `description` | `string` | The description of this snapshot. |
| `coverImage` | `object` | An image of a snapshot. |
| `driveId` | `string` | The ID of the file underlying this snapshot in the Drive API. Only present if the snapshot is a view on a Drive file and the file is owned by the caller. |
| `type` | `string` | The type of this snapshot. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#snapshot`. |
| `progressValue` | `string` | The progress value (64-bit integer set by developer) associated with this snapshot. |
| `title` | `string` | The title of this snapshot. |
| `lastModifiedMillis` | `string` | The timestamp (in millis since Unix epoch) of the last modification to this snapshot. |
| `uniqueName` | `string` | The unique name provided when the snapshot was created. |
| `durationMillis` | `string` | The duration associated with this snapshot, in millis. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `snapshotId` | Retrieves the metadata for a given snapshot ID. |
| `list` | `SELECT` | `playerId` | Retrieves a list of snapshots created by your application for the player corresponding to the player ID. |
