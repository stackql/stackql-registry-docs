---
title: compute_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_keys
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

Creates, updates, deletes, gets or lists a <code>compute_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.compute_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="computeType" /> | `string` | The type of compute |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="computeName, resourceGroupName, subscriptionId, workspaceName" /> | Gets secrets related to Machine Learning compute (storage keys, service credentials, etc). |

## `SELECT` examples

Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).


```sql
SELECT
computeType
FROM azure.ml_services.compute_keys
WHERE computeName = '{{ computeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```