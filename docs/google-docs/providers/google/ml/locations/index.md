---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - ml
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="capabilities" /> | `array` | Capabilities available in the location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Get the complete list of CMLE capabilities in a location, along with their location-specific properties. |
| <CopyableCode code="projects_locations_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | List all locations that provides at least one type of CMLE capability. |

## `SELECT` examples

List all locations that provides at least one type of CMLE capability.

```sql
SELECT
name,
capabilities
FROM google.ml.locations
WHERE projectsId = '{{ projectsId }}'; 
```
