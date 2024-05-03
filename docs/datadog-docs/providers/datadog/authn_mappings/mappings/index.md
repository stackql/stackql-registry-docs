---
title: mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - mappings
  - authn_mappings
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
<tr><td><b>Name</b></td><td><code>mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.authn_mappings.mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the AuthN Mapping. |
| <CopyableCode code="attributes" /> | `object` | Attributes of AuthN Mapping. |
| <CopyableCode code="relationships" /> | `object` | All relationships associated with AuthN Mapping. |
| <CopyableCode code="type" /> | `string` | AuthN Mappings resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getauthn_mapping" /> | `SELECT` | <CopyableCode code="authn_mapping_id, dd_site" /> | Get an AuthN Mapping specified by the AuthN Mapping UUID. |
| <CopyableCode code="listauthn_mappings" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all AuthN Mappings in the org. |
| <CopyableCode code="createauthn_mapping" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create an AuthN Mapping. |
| <CopyableCode code="deleteauthn_mapping" /> | `DELETE` | <CopyableCode code="authn_mapping_id, dd_site" /> | Delete an AuthN Mapping specified by AuthN Mapping UUID. |
| <CopyableCode code="_getauthn_mapping" /> | `EXEC` | <CopyableCode code="authn_mapping_id, dd_site" /> | Get an AuthN Mapping specified by the AuthN Mapping UUID. |
| <CopyableCode code="_listauthn_mappings" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all AuthN Mappings in the org. |
| <CopyableCode code="updateauthn_mapping" /> | `EXEC` | <CopyableCode code="authn_mapping_id, data__data, dd_site" /> | Edit an AuthN Mapping. |
