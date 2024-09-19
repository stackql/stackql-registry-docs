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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>environments_debugmask</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_debugmask</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_debugmask" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the debug mask. |
| <CopyableCode code="faultJSONPaths" /> | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON payloads in error flows. |
| <CopyableCode code="faultXPaths" /> | `array` | List of XPaths that specify the XML elements to be filtered from XML payloads in error flows. |
| <CopyableCode code="namespaces" /> | `object` | Map of namespaces to URIs. |
| <CopyableCode code="requestJSONPaths" /> | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON request message payloads. |
| <CopyableCode code="requestXPaths" /> | `array` | List of XPaths that specify the XML elements to be filtered from XML request message payloads. |
| <CopyableCode code="responseJSONPaths" /> | `array` | List of JSON paths that specify the JSON elements to be filtered from JSON response message payloads. |
| <CopyableCode code="responseXPaths" /> | `array` | List of XPaths that specify the XML elements to be filtered from XML response message payloads. |
| <CopyableCode code="variables" /> | `array` | List of variables that should be masked from the debug output. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_get_debugmask" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Gets the debug mask singleton resource for an environment. |
| <CopyableCode code="organizations_environments_update_debugmask" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId" /> | Updates the debug mask singleton resource for an environment. |

## `SELECT` examples

Gets the debug mask singleton resource for an environment.

```sql
SELECT
name,
faultJSONPaths,
faultXPaths,
namespaces,
requestJSONPaths,
requestXPaths,
responseJSONPaths,
responseXPaths,
variables
FROM google.apigee.environments_debugmask
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a <code>environments_debugmask</code> resource.

```sql
/*+ update */
UPDATE google.apigee.environments_debugmask
SET 
name = '{{ name }}',
variables = '{{ variables }}',
requestJSONPaths = '{{ requestJSONPaths }}',
requestXPaths = '{{ requestXPaths }}',
faultXPaths = '{{ faultXPaths }}',
namespaces = '{{ namespaces }}',
responseXPaths = '{{ responseXPaths }}',
responseJSONPaths = '{{ responseJSONPaths }}',
faultJSONPaths = '{{ faultJSONPaths }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
