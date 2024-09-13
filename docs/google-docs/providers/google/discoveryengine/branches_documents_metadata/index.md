
---
title: branches_documents_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - branches_documents_metadata
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

Creates, updates, deletes or gets an <code>branches_documents_metadatum</code> resource or lists <code>branches_documents_metadata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>branches_documents_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.branches_documents_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="documentsMetadata" /> | `array` | The metadata of the Documents. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_branches_batch_get_documents_metadata" /> | `SELECT` | <CopyableCode code="branchesId, collectionsId, dataStoresId, locationsId, projectsId" /> | Gets index freshness metadata for Documents. Supported for website search only. |
| <CopyableCode code="projects_locations_data_stores_branches_batch_get_documents_metadata" /> | `SELECT` | <CopyableCode code="branchesId, dataStoresId, locationsId, projectsId" /> | Gets index freshness metadata for Documents. Supported for website search only. |

## `SELECT` examples

Gets index freshness metadata for Documents. Supported for website search only.

```sql
SELECT
documentsMetadata
FROM google.discoveryengine.branches_documents_metadata
WHERE branchesId = '{{ branchesId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
