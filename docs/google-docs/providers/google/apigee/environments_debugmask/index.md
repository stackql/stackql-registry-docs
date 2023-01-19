---
title: environments_debugmask
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_debugmask
  - apigee
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
<tr><td><b>Name</b></td><td><code>environments_debugmask</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments_debugmask</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the debug mask. |
| `requestJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON request message payloads. |
| `requestXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML request message payloads. |
| `faultXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML payloads in error flows. |
| `namespaces` | `object` | Map of namespaces to URIs. |
| `faultJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON payloads in error flows. |
| `variables` | `array` | List of variables that should be masked from the debug output. |
| `responseJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON response message payloads. |
| `responseXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML response message payloads. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_getDebugmask` | `SELECT` | `environmentsId, organizationsId` |
