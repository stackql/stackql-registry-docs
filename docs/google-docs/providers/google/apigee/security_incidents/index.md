---
title: security_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - security_incidents
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
<tr><td><b>Name</b></td><td><code>security_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.security_incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the security incident resource. Format: organizations/&#123;org&#125;/environments/&#123;environment&#125;/securityIncidents/&#123;incident&#125; Example: organizations/apigee-org/environments/dev/securityIncidents/1234-5678-9101-1111 |
| `riskLevel` | `string` | Output only. Risk level of the incident. |
| `trafficCount` | `string` | Total traffic detected as part of the incident. |
| `detectionTypes` | `array` | Output only. Detection types which are part of the incident. Examples: Flooder, OAuth Abuser, Static Content Scraper, Anomaly Detection. |
| `displayName` | `string` | Display name of the security incident. |
| `firstDetectedTime` | `string` | Output only. The time when events associated with the incident were first detected. |
| `lastDetectedTime` | `string` | Output only. The time when events associated with the incident were last detected. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_security_incidents_get` | `SELECT` | `environmentsId, organizationsId, securityIncidentsId` | GetSecurityIncident gets the specified security incident. Returns NOT_FOUND if security incident is not present for the specified organization and environment. |
| `organizations_environments_security_incidents_list` | `SELECT` | `environmentsId, organizationsId` | ListSecurityIncidents lists all the security incident associated with the environment. |
| `_organizations_environments_security_incidents_list` | `EXEC` | `environmentsId, organizationsId` | ListSecurityIncidents lists all the security incident associated with the environment. |
