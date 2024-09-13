---
title: processor_types
hide_title: false
hide_table_of_contents: false
keywords:
  - processor_types
  - documentai
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

Creates, updates, deletes, gets or lists a <code>processor_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>processor_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.processor_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the processor type. Format: `projects/{project}/processorTypes/{processor_type}` |
| <CopyableCode code="allowCreation" /> | `boolean` | Whether the processor type allows creation. If true, users can create a processor of this processor type. Otherwise, users need to request access. |
| <CopyableCode code="availableLocations" /> | `array` | The locations in which this processor is available. |
| <CopyableCode code="category" /> | `string` | The processor category, used by UI to group processor types. |
| <CopyableCode code="launchStage" /> | `string` | Launch stage of the processor type |
| <CopyableCode code="sampleDocumentUris" /> | `array` | A set of Cloud Storage URIs of sample documents for this processor. |
| <CopyableCode code="type" /> | `string` | The processor type, such as: `OCR_PROCESSOR`, `INVOICE_PROCESSOR`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_fetch_processor_types" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated. |
| <CopyableCode code="projects_locations_processor_types_get" /> | `SELECT` | <CopyableCode code="locationsId, processorTypesId, projectsId" /> | Gets a processor type detail. |
| <CopyableCode code="projects_locations_processor_types_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the processor types that exist. |

## `SELECT` examples

Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated.

```sql
SELECT
name,
allowCreation,
availableLocations,
category,
launchStage,
sampleDocumentUris,
type
FROM google.documentai.processor_types
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
