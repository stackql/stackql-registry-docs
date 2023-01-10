---
title: place_action_links
hide_title: false
hide_table_of_contents: false
keywords:
  - place_action_links
  - mybusinessplaceactions
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
<tr><td><b>Name</b></td><td><code>place_action_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessplaceactions.place_action_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Optional. The resource name, in the format `locations/&#123;location_id&#125;/placeActionLinks/&#123;place_action_link_id&#125;`. The name field will only be considered in UpdatePlaceActionLink and DeletePlaceActionLink requests for updating and deleting links respectively. However, it will be ignored in CreatePlaceActionLink request, where `place_action_link_id` will be assigned by the server on successful creation of a new link and returned as part of the response. |
| `placeActionType` | `string` | Required. The type of place action that can be performed using this link. |
| `providerType` | `string` | Output only. Specifies the provider type. |
| `updateTime` | `string` | Output only. The time when the place action link was last modified. |
| `uri` | `string` | Required. The link uri. The same uri can be reused for different action types across different locations. However, only one place action link is allowed for each unique combination of (uri, place action type, location). |
| `createTime` | `string` | Output only. The time when the place action link was created. |
| `isEditable` | `boolean` | Output only. Indicates whether this link can be edited by the client. |
| `isPreferred` | `boolean` | Optional. Whether this link is preferred by the merchant. Only one link can be marked as preferred per place action type at a location. If a future request marks a different link as preferred for the same place action type, then the current preferred link (if any exists) will lose its preference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `locations_placeActionLinks_get` | `SELECT` | `locationsId, placeActionLinksId` | Gets the specified place action link. |
| `locations_placeActionLinks_list` | `SELECT` | `locationsId` | Lists the place action links for the specified location. |
| `locations_placeActionLinks_create` | `INSERT` | `locationsId` | Creates a place action link associated with the specified location, and returns it. The request is considered duplicate if the `parent`, `place_action_link.uri` and `place_action_link.place_action_type` are the same as a previous request. |
| `locations_placeActionLinks_delete` | `DELETE` | `locationsId, placeActionLinksId` | Deletes a place action link from the specified location. |
| `locations_placeActionLinks_patch` | `EXEC` | `locationsId, placeActionLinksId` | Updates the specified place action link and returns it. |
