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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs_completion_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.catalogs_completion_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Immutable. Fully qualified name `projects/*/locations/*/catalogs/*/completionConfig` |
| `minPrefixLength` | `integer` | The minimum number of characters needed to be typed in order to get suggestions. Default value is 2. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. |
| `maxSuggestions` | `integer` | The maximum number of autocomplete suggestions returned per term. Default value is 20. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. |
| `lastSuggestionsImportOperation` | `string` | Output only. Name of the LRO corresponding to the latest suggestion terms list import. Can use GetOperation API method to retrieve the latest state of the Long Running Operation. |
| `allowlistInputConfig` | `object` | The input config source for completion data. |
| `suggestionsInputConfig` | `object` | The input config source for completion data. |
| `lastAllowlistImportOperation` | `string` | Output only. Name of the LRO corresponding to the latest allowlist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. |
| `matchingOrder` | `string` | Specifies the matching order for autocomplete suggestions, e.g., a query consisting of 'sh' with 'out-of-order' specified would suggest "women's shoes", whereas a query of 'red s' with 'exact-prefix' specified would suggest "red shoes". Currently supported values: * 'out-of-order' * 'exact-prefix' Default value: 'exact-prefix'. |
| `autoLearning` | `boolean` | If set to true, the auto learning function is enabled. Auto learning uses user data to generate suggestions using ML techniques. Default value is false. Only after enabling auto learning can users use `cloud-retail` data in CompleteQueryRequest. |
| `lastDenylistImportOperation` | `string` | Output only. Name of the LRO corresponding to the latest denylist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. |
| `denylistInputConfig` | `object` | The input config source for completion data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_get_completion_config` | `SELECT` | `catalogsId, locationsId, projectsId` | Gets a CompletionConfig. |
| `projects_locations_catalogs_update_completion_config` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates the CompletionConfigs. |
