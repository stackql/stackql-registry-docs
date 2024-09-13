
---
title: hl7_v2_stores_hl7v2_store_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - hl7_v2_stores_hl7v2_store_metrics
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

Creates, updates, deletes or gets an <code>hl7_v2_stores_hl7v2_store_metric</code> resource or lists <code>hl7_v2_stores_hl7v2_store_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hl7_v2_stores_hl7v2_store_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.hl7_v2_stores_hl7v2_store_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the HL7v2 store to get metrics for, in the format `projects/{project_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`. |
| <CopyableCode code="metrics" /> | `array` | List of HL7v2 store metrics by message type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_hl7v2_store_metrics" /> | `SELECT` | <CopyableCode code="datasetsId, hl7V2StoresId, locationsId, projectsId" /> | Gets metrics associated with the HL7v2 store. |

## `SELECT` examples

Gets metrics associated with the HL7v2 store.

```sql
SELECT
name,
metrics
FROM google.healthcare.hl7_v2_stores_hl7v2_store_metrics
WHERE datasetsId = '{{ datasetsId }}'
AND hl7V2StoresId = '{{ hl7V2StoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
