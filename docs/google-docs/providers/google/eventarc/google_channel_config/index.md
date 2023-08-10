---
title: google_channel_config
hide_title: false
hide_table_of_contents: false
keywords:
  - google_channel_config
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
<tr><td><b>Name</b></td><td><code>google_channel_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.eventarc.google_channel_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the config. Must be in the format of, `projects/&#123;project&#125;/locations/&#123;location&#125;/googleChannelConfig`. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `cryptoKeyName` | `string` | Optional. Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_google_channel_config` | `SELECT` | `locationsId, projectsId` | Get a GoogleChannelConfig |
| `update_google_channel_config` | `EXEC` | `locationsId, projectsId` | Update a single GoogleChannelConfig |
