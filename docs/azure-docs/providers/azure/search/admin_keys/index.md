---
title: admin_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_keys
  - search
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

Creates, updates, deletes, gets or lists a <code>admin_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>admin_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.admin_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryKey" /> | `string` | The primary admin API key of the search service. |
| <CopyableCode code="secondaryKey" /> | `string` | The secondary admin API key of the search service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets the primary and secondary admin API keys for the specified Azure AI Search service. |
| <CopyableCode code="regenerate" /> | `EXEC` | <CopyableCode code="keyKind, resourceGroupName, searchServiceName, subscriptionId" /> | Regenerates either the primary or secondary admin API key. You can only regenerate one key at a time. |

## `SELECT` examples

Gets the primary and secondary admin API keys for the specified Azure AI Search service.


```sql
SELECT
primaryKey,
secondaryKey
FROM azure.search.admin_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```