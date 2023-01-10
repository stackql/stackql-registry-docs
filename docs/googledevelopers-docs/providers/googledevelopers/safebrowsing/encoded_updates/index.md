---
title: encoded_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - encoded_updates
  - safebrowsing
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
<tr><td><b>Name</b></td><td><code>encoded_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.safebrowsing.encoded_updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `minimumWaitDuration` | `string` | The minimum duration the client must wait before issuing any update request. If this field is not set clients may update as soon as they want. |
| `listUpdateResponses` | `array` | The list updates requested by the clients. The number of responses here may be less than the number of requests sent by clients. This is the case, for example, if the server has no updates for a particular list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `encodedUpdates_get` | `SELECT` | `encodedRequest` |
