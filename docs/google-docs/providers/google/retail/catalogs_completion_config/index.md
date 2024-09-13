---
title: catalogs_completion_config
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_completion_config
  - retail
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

Creates, updates, deletes or gets an <code>catalogs_completion_config</code> resource or lists <code>catalogs_completion_config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs_completion_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.catalogs_completion_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. Fully qualified name `projects/*/locations/*/catalogs/*/completionConfig` |
| <CopyableCode code="allowlistInputConfig" /> | `object` | The input config source for completion data. |
| <CopyableCode code="autoLearning" /> | `boolean` | If set to true, the auto learning function is enabled. Auto learning uses user data to generate suggestions using ML techniques. Default value is false. Only after enabling auto learning can users use `cloud-retail` data in CompleteQueryRequest. |
| <CopyableCode code="denylistInputConfig" /> | `object` | The input config source for completion data. |
| <CopyableCode code="lastAllowlistImportOperation" /> | `string` | Output only. Name of the LRO corresponding to the latest allowlist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. |
| <CopyableCode code="lastDenylistImportOperation" /> | `string` | Output only. Name of the LRO corresponding to the latest denylist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. |
| <CopyableCode code="lastSuggestionsImportOperation" /> | `string` | Output only. Name of the LRO corresponding to the latest suggestion terms list import. Can use GetOperation API method to retrieve the latest state of the Long Running Operation. |
| <CopyableCode code="matchingOrder" /> | `string` | Specifies the matching order for autocomplete suggestions, e.g., a query consisting of 'sh' with 'out-of-order' specified would suggest "women's shoes", whereas a query of 'red s' with 'exact-prefix' specified would suggest "red shoes". Currently supported values: * 'out-of-order' * 'exact-prefix' Default value: 'exact-prefix'. |
| <CopyableCode code="maxSuggestions" /> | `integer` | The maximum number of autocomplete suggestions returned per term. Default value is 20. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. |
| <CopyableCode code="minPrefixLength" /> | `integer` | The minimum number of characters needed to be typed in order to get suggestions. Default value is 2. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. |
| <CopyableCode code="suggestionsInputConfig" /> | `object` | The input config source for completion data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_get_completion_config" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Gets a CompletionConfig. |
| <CopyableCode code="projects_locations_catalogs_update_completion_config" /> | `UPDATE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Updates the CompletionConfigs. |

## `SELECT` examples

Gets a CompletionConfig.

```sql
SELECT
name,
allowlistInputConfig,
autoLearning,
denylistInputConfig,
lastAllowlistImportOperation,
lastDenylistImportOperation,
lastSuggestionsImportOperation,
matchingOrder,
maxSuggestions,
minPrefixLength,
suggestionsInputConfig
FROM google.retail.catalogs_completion_config
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a catalogs_completion_config only if the necessary resources are available.

```sql
UPDATE google.retail.catalogs_completion_config
SET 
name = '{{ name }}',
matchingOrder = '{{ matchingOrder }}',
maxSuggestions = '{{ maxSuggestions }}',
minPrefixLength = '{{ minPrefixLength }}',
autoLearning = true|false,
suggestionsInputConfig = '{{ suggestionsInputConfig }}',
lastSuggestionsImportOperation = '{{ lastSuggestionsImportOperation }}',
denylistInputConfig = '{{ denylistInputConfig }}',
lastDenylistImportOperation = '{{ lastDenylistImportOperation }}',
allowlistInputConfig = '{{ allowlistInputConfig }}',
lastAllowlistImportOperation = '{{ lastAllowlistImportOperation }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
