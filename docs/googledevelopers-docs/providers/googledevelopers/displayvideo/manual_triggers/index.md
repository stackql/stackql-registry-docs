---
title: manual_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - manual_triggers
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
<tr><td><b>Name</b></td><td><code>manual_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.manual_triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the manual trigger. |
| `triggerId` | `string` | Output only. The unique ID of the manual trigger. |
| `activationDurationMinutes` | `string` | Required. The maximum duration of each activation in minutes. Must be between 1 and 360 inclusive. After this duration, the trigger will be automatically deactivated. |
| `advertiserId` | `string` | Required. Immutable. The unique ID of the advertiser that the manual trigger belongs to. |
| `displayName` | `string` | Required. The display name of the manual trigger. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `latestActivationTime` | `string` | Output only. The timestamp of the trigger's latest activation. |
| `state` | `string` | Output only. The state of the manual trigger. Will be set to the `INACTIVE` state upon creation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `advertisers_manualTriggers_get` | `SELECT` | `advertisersId, manualTriggersId` | Gets a manual trigger. |
| `advertisers_manualTriggers_list` | `SELECT` | `advertisersId` | Lists manual triggers that are accessible to the current user for a given advertiser ID. The order is defined by the order_by parameter. A single advertiser_id is required. |
| `advertisers_manualTriggers_create` | `INSERT` | `advertisersId` | Creates a new manual trigger. Returns the newly created manual trigger if successful. |
| `advertisers_manualTriggers_activate` | `EXEC` | `advertisersId, manualTriggersId` | Activates a manual trigger. Each activation of the manual trigger must be at least 5 minutes apart, otherwise an error will be returned. |
| `advertisers_manualTriggers_deactivate` | `EXEC` | `advertisersId, manualTriggersId` | Deactivates a manual trigger. |
| `advertisers_manualTriggers_patch` | `EXEC` | `advertisersId, manualTriggersId` | Updates a manual trigger. Returns the updated manual trigger if successful. |
