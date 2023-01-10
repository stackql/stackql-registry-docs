---
title: third_party_links
hide_title: false
hide_table_of_contents: false
keywords:
  - third_party_links
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
<tr><td><b>Name</b></td><td><code>third_party_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.third_party_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `snippet` | `object` | Basic information about a third party account link, including its type and type-specific information. |
| `status` | `object` | The third-party link status object contains information about the status of the link. |
| `etag` | `string` | Etag of this resource |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "youtube#thirdPartyLink". |
| `linkingToken` | `string` | The linking_token identifies a YouTube account and channel with which the third party account is linked. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `thirdPartyLinks_list` | `SELECT` | `part` | Retrieves a list of resources, possibly filtered. |
| `thirdPartyLinks_delete` | `DELETE` | `linkingToken, type` | Deletes a resource. |
| `thirdPartyLinks_insert` | `EXEC` | `part` | Inserts a new resource into this collection. |
| `thirdPartyLinks_update` | `EXEC` | `part` | Updates an existing resource. |
