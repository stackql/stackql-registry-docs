---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.destinations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Destination display name. |
| `fingerprint` | `string` | The fingerprint of the Google Tag Destination as computed at storage time. This value is recomputed whenever the destination is modified. |
| `path` | `string` | Destination's API relative path. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI. |
| `accountId` | `string` | GTM Account ID. |
| `containerId` | `string` | GTM Container ID. |
| `destinationId` | `string` | Destination ID. |
| `destinationLinkId` | `string` | The Destination link ID uniquely identifies the Destination. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_destinations_get` | `SELECT` | `accountsId, containersId, destinationsId` | Gets a Destination. |
| `accounts_containers_destinations_list` | `SELECT` | `accountsId, containersId` | Lists all Destinations linked to a GTM Container. |
| `accounts_containers_destinations_link` | `EXEC` | `accountsId, containersId` | Adds a Destination to this Container and removes it from the Container to which it is currently linked. |
