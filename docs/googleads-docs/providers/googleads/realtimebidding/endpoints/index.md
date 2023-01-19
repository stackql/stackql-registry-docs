---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - realtimebidding
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the endpoint resource that must follow the pattern `bidders/&#123;bidderAccountId&#125;/endpoints/&#123;endpointId&#125;`, where &#123;bidderAccountId&#125; is the account ID of the bidder who operates this endpoint, and &#123;endpointId&#125; is a unique ID assigned by the server. |
| `maximumQps` | `string` | The maximum number of queries per second allowed to be sent to this server. |
| `tradingLocation` | `string` | The trading location that bid requests should be sent from. See https://developers.google.com/authorized-buyers/rtb/peer-guide#trading-locations for further information. |
| `url` | `string` | Output only. The URL that bid requests should be sent to. |
| `bidProtocol` | `string` | The protocol that the bidder endpoint is using. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_endpoints_get` | `SELECT` | `biddersId, endpointsId` | Gets a bidder endpoint by its name. |
| `bidders_endpoints_list` | `SELECT` | `biddersId` | Lists all the bidder's endpoints. |
| `bidders_endpoints_patch` | `EXEC` | `biddersId, endpointsId` | Updates a bidder's endpoint. |
