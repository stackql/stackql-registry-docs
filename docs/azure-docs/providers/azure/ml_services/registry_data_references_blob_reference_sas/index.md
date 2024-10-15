---
title: registry_data_references_blob_reference_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_data_references_blob_reference_sas
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>registry_data_references_blob_reference_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_data_references_blob_reference_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registry_data_references_blob_reference_sas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobReferenceForConsumption" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, registryName, resourceGroupName, subscriptionId, version" /> |  |

## `SELECT` examples




```sql
SELECT
blobReferenceForConsumption
FROM azure.ml_services.registry_data_references_blob_reference_sas
WHERE name = '{{ name }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```