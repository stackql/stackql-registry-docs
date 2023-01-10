---
title: chains
hide_title: false
hide_table_of_contents: false
keywords:
  - chains
  - mybusinessbusinessinformation
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinessinformation.chains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The chain's resource name, in the format `chains/&#123;chain_id&#125;`. |
| `chainNames` | `array` | Names of the chain. |
| `locationCount` | `integer` | Number of locations that are part of this chain. |
| `websites` | `array` | Websites of the chain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `chainsId` | Gets the specified chain. Returns `NOT_FOUND` if the chain does not exist. |
| `search` | `EXEC` |  | Searches the chain based on chain name. |
