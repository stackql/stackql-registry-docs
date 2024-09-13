---
title: api_observation_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - api_observation_tags
  - apim
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

Creates, updates, deletes or gets an <code>api_observation_tag</code> resource or lists <code>api_observation_tags</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_observation_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apim.api_observation_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_api_observation_tags" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | ListApiObservationTags lists all extant tags on any observation in the given project. |

## `SELECT` examples

ListApiObservationTags lists all extant tags on any observation in the given project.

```sql
SELECT
column_anon
FROM google.apim.api_observation_tags
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
