---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - config
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"` |
| <CopyableCode code="displayName" /> | `string` | The friendly name for this location, typically a nearby city name. For example, "Tokyo". |
| <CopyableCode code="labels" /> | `object` | Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"} |
| <CopyableCode code="locationId" /> | `string` | The canonical id for this location. For example: `"us-east1"`. |
| <CopyableCode code="metadata" /> | `object` | Service-specific metadata. For example the available capacity at the given location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets information about a location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists information about the supported locations for this service. |

## `SELECT` examples

Lists information about the supported locations for this service.

```sql
SELECT
name,
displayName,
labels,
locationId,
metadata
FROM google.config.locations
WHERE projectsId = '{{ projectsId }}'; 
```
