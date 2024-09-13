---
title: custom_models
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_models
  - discoveryengine
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

Creates, updates, deletes, gets or lists a <code>custom_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.custom_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="models" /> | `array` | List of custom tuning models. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_custom_models_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Gets a list of all the custom models. |

## `SELECT` examples

Gets a list of all the custom models.

```sql
SELECT
models
FROM google.discoveryengine.custom_models
WHERE collectionsId = '{{ collectionsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
