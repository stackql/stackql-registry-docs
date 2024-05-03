---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - key_management
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.key_management.api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the API key. |
| <CopyableCode code="attributes" /> | `object` | Attributes of a full API key. |
| <CopyableCode code="relationships" /> | `object` | Resources related to the API key. |
| <CopyableCode code="type" /> | `string` | API Keys resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_api_key" /> | `SELECT` | <CopyableCode code="api_key_id, dd_site" /> | Get an API key. |
| <CopyableCode code="list_api_keys" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all API keys available for your account. |
| <CopyableCode code="create_api_key" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create an API key. |
| <CopyableCode code="delete_api_key" /> | `DELETE` | <CopyableCode code="api_key_id, dd_site" /> | Delete an API key. |
| <CopyableCode code="_get_api_key" /> | `EXEC` | <CopyableCode code="api_key_id, dd_site" /> | Get an API key. |
| <CopyableCode code="_list_api_keys" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all API keys available for your account. |
| <CopyableCode code="update_api_key" /> | `EXEC` | <CopyableCode code="api_key_id, data__data, dd_site" /> | Update an API key. |
