---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
  - apigee
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource URI that can be used to identify the scope of the key value map entries. |
| <CopyableCode code="value" /> | `string` | Required. Data or payload that is being retrieved and associated with the unique key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_keyvaluemaps_entries_get" /> | `SELECT` | <CopyableCode code="apisId, entriesId, keyvaluemapsId, organizationsId" /> | Get the key value entry value for a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_apis_keyvaluemaps_entries_list" /> | `SELECT` | <CopyableCode code="apisId, keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_environments_keyvaluemaps_entries_get" /> | `SELECT` | <CopyableCode code="entriesId, environmentsId, keyvaluemapsId, organizationsId" /> | Get the key value entry value for a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_environments_keyvaluemaps_entries_list" /> | `SELECT` | <CopyableCode code="environmentsId, keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_keyvaluemaps_entries_get" /> | `SELECT` | <CopyableCode code="entriesId, keyvaluemapsId, organizationsId" /> | Get the key value entry value for a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_keyvaluemaps_entries_list" /> | `SELECT` | <CopyableCode code="keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_apis_keyvaluemaps_entries_create" /> | `INSERT` | <CopyableCode code="apisId, keyvaluemapsId, organizationsId" /> | Creates key value entries in a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_environments_keyvaluemaps_entries_create" /> | `INSERT` | <CopyableCode code="environmentsId, keyvaluemapsId, organizationsId" /> | Creates key value entries in a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_keyvaluemaps_entries_create" /> | `INSERT` | <CopyableCode code="keyvaluemapsId, organizationsId" /> | Creates key value entries in a key value map scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_apis_keyvaluemaps_entries_delete" /> | `DELETE` | <CopyableCode code="apisId, entriesId, keyvaluemapsId, organizationsId" /> | Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy. **Notes:** * After you delete the key value entry, the policy consuming the entry will continue to function with its cached values for a few minutes. This is expected behavior. * Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_environments_keyvaluemaps_entries_delete" /> | `DELETE` | <CopyableCode code="entriesId, environmentsId, keyvaluemapsId, organizationsId" /> | Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy. **Notes:** * After you delete the key value entry, the policy consuming the entry will continue to function with its cached values for a few minutes. This is expected behavior. * Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_keyvaluemaps_entries_delete" /> | `DELETE` | <CopyableCode code="entriesId, keyvaluemapsId, organizationsId" /> | Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy. **Notes:** * After you delete the key value entry, the policy consuming the entry will continue to function with its cached values for a few minutes. This is expected behavior. * Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="_organizations_apis_keyvaluemaps_entries_list" /> | `EXEC` | <CopyableCode code="apisId, keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="_organizations_environments_keyvaluemaps_entries_list" /> | `EXEC` | <CopyableCode code="environmentsId, keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="_organizations_keyvaluemaps_entries_list" /> | `EXEC` | <CopyableCode code="keyvaluemapsId, organizationsId" /> | Lists key value entries for key values maps scoped to an organization, environment, or API proxy. **Note**: Supported for Apigee hybrid 1.8.x and higher. |
| <CopyableCode code="organizations_apis_keyvaluemaps_entries_update" /> | `EXEC` | <CopyableCode code="apisId, entriesId, keyvaluemapsId, organizationsId" /> | Update key value entry scoped to an organization, environment, or API proxy for an existing key. |
| <CopyableCode code="organizations_environments_keyvaluemaps_entries_update" /> | `EXEC` | <CopyableCode code="entriesId, environmentsId, keyvaluemapsId, organizationsId" /> | Update key value entry scoped to an organization, environment, or API proxy for an existing key. |
| <CopyableCode code="organizations_keyvaluemaps_entries_update" /> | `EXEC` | <CopyableCode code="entriesId, keyvaluemapsId, organizationsId" /> | Update key value entry scoped to an organization, environment, or API proxy for an existing key. |
