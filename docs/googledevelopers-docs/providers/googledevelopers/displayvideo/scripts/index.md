---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
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
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.scripts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the custom bidding script. |
| `state` | `string` | Output only. The state of the custom bidding script. |
| `active` | `boolean` | Output only. Whether the script is currently being used for scoring by the parent algorithm. |
| `createTime` | `string` | Output only. The time when the script was created. |
| `customBiddingAlgorithmId` | `string` | Output only. The unique ID of the custom bidding algorithm the script belongs to. |
| `customBiddingScriptId` | `string` | Output only. The unique ID of the custom bidding script. |
| `errors` | `array` | Output only. Error details of a rejected custom bidding script. This field will only be populated when Script.state is REJECTED. |
| `script` | `object` | The reference to the uploaded custom bidding script file. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customBiddingAlgorithms_scripts_get` | `SELECT` | `customBiddingAlgorithmsId, scriptsId` | Gets a custom bidding script. |
| `customBiddingAlgorithms_scripts_list` | `SELECT` | `customBiddingAlgorithmsId` | Lists custom bidding scripts that belong to the given algorithm. The order is defined by the order_by parameter. |
| `customBiddingAlgorithms_scripts_create` | `INSERT` | `customBiddingAlgorithmsId` | Creates a new custom bidding script. Returns the newly created script if successful. |
