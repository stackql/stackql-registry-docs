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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>security_incident</code> resource or lists <code>security_incidents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.security_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the security incident resource. Format: organizations/{org}/environments/{environment}/securityIncidents/{incident} Example: organizations/apigee-org/environments/dev/securityIncidents/1234-5678-9101-1111 |
| <CopyableCode code="detectionTypes" /> | `array` | Output only. Detection types which are part of the incident. Examples: Flooder, OAuth Abuser, Static Content Scraper, Anomaly Detection. |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name of the security incident. |
| <CopyableCode code="firstDetectedTime" /> | `string` | Output only. The time when events associated with the incident were first detected. |
| <CopyableCode code="lastDetectedTime" /> | `string` | Output only. The time when events associated with the incident were last detected. |
| <CopyableCode code="lastObservabilityChangeTime" /> | `string` | Output only. The time when the incident observability was last changed. |
| <CopyableCode code="observability" /> | `string` | Optional. Indicates if the user archived this incident. |
| <CopyableCode code="riskLevel" /> | `string` | Output only. Risk level of the incident. |
| <CopyableCode code="trafficCount" /> | `string` | Total traffic detected as part of the incident. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_security_incidents_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, securityIncidentsId" /> | GetSecurityIncident gets the specified security incident. Returns NOT_FOUND if security incident is not present for the specified organization and environment. |
| <CopyableCode code="organizations_environments_security_incidents_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | ListSecurityIncidents lists all the security incident associated with the environment. |
| <CopyableCode code="organizations_environments_security_incidents_batch_update" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId" /> | BatchUpdateSecurityIncident updates multiple existing security incidents. |
| <CopyableCode code="organizations_environments_security_incidents_patch" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId, securityIncidentsId" /> | UpdateSecurityIncidents updates an existing security incident. |

## `SELECT` examples

ListSecurityIncidents lists all the security incident associated with the environment.

```sql
SELECT
name,
detectionTypes,
displayName,
firstDetectedTime,
lastDetectedTime,
lastObservabilityChangeTime,
observability,
riskLevel,
trafficCount
FROM google.apigee.security_incidents
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a security_incident only if the necessary resources are available.

```sql
UPDATE google.apigee.security_incidents
SET 
requests = '{{ requests }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
