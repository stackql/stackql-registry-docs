---
title: myconfig
hide_title: false
hide_table_of_contents: false
keywords:
  - myconfig
  - books
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
<tr><td><b>Name</b></td><td><code>myconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.myconfig</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `releaseDownloadAccess` | `EXEC` | `cpksver, volumeIds` | Release downloaded content access restriction. |
| `requestAccess` | `EXEC` | `cpksver, nonce, source, volumeId` | Request concurrent and download access restrictions. |
| `syncVolumeLicenses` | `EXEC` | `cpksver, nonce, source` | Request downloaded content access for specified volumes on the My eBooks shelf. |
| `updateUserSettings` | `EXEC` |  | Sets the settings for the user. If a sub-object is specified, it will overwrite the existing sub-object stored in the server. Unspecified sub-objects will retain the existing value. |
