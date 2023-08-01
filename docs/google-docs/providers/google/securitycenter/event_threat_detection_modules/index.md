---
title: event_threat_detection_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - event_threat_detection_modules
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>event_threat_detection_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.event_threat_detection_modules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eventThreatDetectionCustomModules` | `array` | Custom modules belonging to the requested parent. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_event_threat_detection_settings_custom_modules_list` | `SELECT` | `organizationsId` | Lists Event Threat Detection custom modules. |
| `organizations_event_threat_detection_settings_custom_modules_create` | `INSERT` | `organizationsId` | Creates an Event Threat Detection custom module. |
| `organizations_event_threat_detection_settings_custom_modules_delete` | `DELETE` | `customModulesId, organizationsId` | Deletes an Event Threat Detection custom module. |
