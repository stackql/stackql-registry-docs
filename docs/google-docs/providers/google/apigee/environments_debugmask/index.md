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
| `faultJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON payloads in error flows. |
| `requestXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML request message payloads. |
| `responseJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON response message payloads. |
| `variables` | `array` | List of variables that should be masked from the debug output. |
| `namespaces` | `object` | Map of namespaces to URIs. |
| `responseXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML response message payloads. |
| `faultXPaths` | `array` | List of XPaths that specify the XML elements to be filtered from XML payloads in error flows. |
| `requestJSONPaths` | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON request message payloads. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_get_debugmask` | `SELECT` | `environmentsId, organizationsId` | Gets the debug mask singleton resource for an environment. |
| `organizations_environments_update_debugmask` | `EXEC` | `environmentsId, organizationsId` | Updates the debug mask singleton resource for an environment. |
