---
title: publisher_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - publisher_connections
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
<tr><td><b>Name</b></td><td><code>publisher_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.publisher_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the publisher connection. This follows the pattern `bidders/&#123;bidder&#125;/publisherConnections/&#123;publisher&#125;`, where `&#123;bidder&#125;` represents the account ID of the bidder, and `&#123;publisher&#125;` is the ads.txt/app-ads.txt publisher ID. |
| `createTime` | `string` | Output only. The time at which the publisher initiated a connection with the bidder (irrespective of if or when the bidder approves it). This is subsequently updated if the publisher revokes and re-initiates the connection. |
| `displayName` | `string` | Output only. Publisher display name. |
| `publisherPlatform` | `string` | Output only. Whether the publisher is an Ad Manager or AdMob publisher. |
| `biddingState` | `string` | Whether the publisher has been approved by the bidder. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bidders_publisherConnections_get` | `SELECT` | `biddersId, publisherConnectionsId` | Gets a publisher connection. |
| `bidders_publisherConnections_list` | `SELECT` | `biddersId` | Lists publisher connections for a given bidder. |
| `bidders_publisherConnections_batchApprove` | `EXEC` | `biddersId` | Batch approves multiple publisher connections. |
| `bidders_publisherConnections_batchReject` | `EXEC` | `biddersId` | Batch rejects multiple publisher connections. |
