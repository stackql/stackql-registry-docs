---
title: fhir_stores_fhirstore_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_stores_fhirstore_metrics
  - healthcare
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

Creates, updates, deletes or gets an <code>fhir_stores_fhirstore_metric</code> resource or lists <code>fhir_stores_fhirstore_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_stores_fhirstore_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.fhir_stores_fhirstore_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the FHIR store to get metrics for, in the format `projects/{project_id}/datasets/{dataset_id}/fhirStores/{fhir_store_id}`. |
| <CopyableCode code="metrics" /> | `array` | List of FhirStoreMetric by resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_fhirstore_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, fhirStoresId, locationsId, projectsId" /> | Gets metrics associated with the FHIR store. |

## `SELECT` examples

Gets metrics associated with the FHIR store.

```sql
SELECT
name,
metrics
FROM google.healthcare.fhir_stores_fhirstore_metrics
WHERE datasetsId = '{{ datasetsId }}'
AND fhirStoresId = '{{ fhirStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
