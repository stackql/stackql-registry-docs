---
title: custom_bidding_algorithms
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_bidding_algorithms
  - displayvideo
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
<tr><td><b>Name</b></td><td><code>custom_bidding_algorithms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.custom_bidding_algorithms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the custom bidding algorithm. |
| `entityStatus` | `string` | Controls whether or not the custom bidding algorithm can be used as a bidding strategy. Accepted values are: * `ENTITY_STATUS_ACTIVE` * `ENTITY_STATUS_ARCHIVED` |
| `displayName` | `string` | Required. The display name of the custom bidding algorithm. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `sharedAdvertiserIds` | `array` | The IDs of the advertisers who have access to this algorithm. If advertiser_id is set, this field will only consist of that value. This field will not be set if the algorithm [`owner`](/display-video/api/reference/rest/v1/customBiddingAlgorithms#CustomBiddingAlgorithm.FIELDS.oneof_owner) is a partner and is being retrieved using an advertiser [`accessor`](/display-video/api/reference/rest/v1/customBiddingAlgorithms/list#body.QUERY_PARAMETERS.oneof_accessor). |
| `modelDetails` | `array` | Output only. The details of custom bidding models for each advertiser who has access. This field may only include the details of the queried advertiser if the algorithm [`owner`](/display-video/api/reference/rest/v1/customBiddingAlgorithms#CustomBiddingAlgorithm.FIELDS.oneof_owner) is a partner and is being retrieved using an advertiser [`accessor`](/display-video/api/reference/rest/v1/customBiddingAlgorithms/list#body.QUERY_PARAMETERS.oneof_accessor). |
| `advertiserId` | `string` | Immutable. The unique ID of the advertiser that owns the custom bidding algorithm. |
| `customBiddingAlgorithmId` | `string` | Output only. The unique ID of the custom bidding algorithm. Assigned by the system. |
| `customBiddingAlgorithmType` | `string` | Required. Immutable. The type of custom bidding algorithm. |
| `partnerId` | `string` | Immutable. The unique ID of the partner that owns the custom bidding algorithm. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customBiddingAlgorithms_get` | `SELECT` | `customBiddingAlgorithmsId` | Gets a custom bidding algorithm. |
| `customBiddingAlgorithms_list` | `SELECT` |  | Lists custom bidding algorithms that are accessible to the current user and can be used in bidding stratgies. The order is defined by the order_by parameter. |
| `customBiddingAlgorithms_create` | `INSERT` |  | Creates a new custom bidding algorithm. Returns the newly created custom bidding algorithm if successful. |
| `customBiddingAlgorithms_patch` | `EXEC` | `customBiddingAlgorithmsId` | Updates an existing custom bidding algorithm. Returns the updated custom bidding algorithm if successful. |
| `customBiddingAlgorithms_uploadScript` | `EXEC` | `customBiddingAlgorithmsId` | Creates a custom bidding script reference object for a script file. The resulting reference object provides a resource path to which the script file should be uploaded. This reference object should be included in when creating a new custom bidding script object. |
