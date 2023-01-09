---
title: countryavailability
hide_title: false
hide_table_of_contents: false
keywords:
  - countryavailability
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>countryavailability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.countryavailability</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `countries` | `array` | A list of one or more countries where artifacts in this track are available. This list includes all countries that are targeted by the track, even if only specific carriers are targeted in that country. |
| `restOfWorld` | `boolean` | Whether artifacts in this track are available to "rest of the world" countries. |
| `syncWithProduction` | `boolean` | Whether this track's availability is synced with the default production track. See https://support.google.com/googleplay/android-developer/answer/7550024 for more information on syncing country availability with production. Note that if this is true, the returned "countries" and "rest_of_world" fields will reflect the values for the default production track. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `edits_countryavailability_get` | `SELECT` | `editId, packageName, track` |
